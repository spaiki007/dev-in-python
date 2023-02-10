#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json, time
from aiohttp import web
import aiohttp_jinja2
from sqlalchemy.sql import select

from es.db import categories
from es.db import manufacturers
from es.db import products
from es.db import colors
from es.db import product_images
from es.db import characteristics
from es.db import cvalues
from es.db import cvalues_assoc_products

async def getProducts(request):
	
	slug = request.query.get('slug', False)
	if not slug:
		web.HTTPNotFound()
		
	min = request.query.get('min', False)
	if not min:
		web.HTTPNotFound()
	min = int(min)
		
	max = request.query.get('max', False)
	if not max:
		web.HTTPNotFound()
	max = int(max)
	
	avalible = request.query.get('avalible', False)
	if not avalible:
		web.HTTPNotFound()

	manufacturer = request.query.get('manufacturer', False)
	if not manufacturer:
		web.HTTPNotFound()

	data = {'products': [], 'constMin': 0, 'constMax': 0, "manufacturers": [], "categories": {}}
	
	async with request.app['db'].acquire() as conn:
	
		cat = ""
		
		category_objects = await conn.execute(select([categories.c.id, categories.c.name, categories.c.slug, categories.c.parent]))
		category_objects = await category_objects.fetchall()
		
		jcats = {}
		for category in category_objects:
		
			if slug == category.slug:
				cat = category
				
			if category.parent == 0:
				jcats[category.id] = {
					'category': {'name': category.name, 'slug': category.slug},
					'subCat':	[],
					'active':	False,
				}

		for category in category_objects:
			if category.parent != 0:
				jcats[category.parent]['subCat'].append({'id': category.id, 'name': category.name, 'slug': category.slug,})
				
		data["categories"] = jcats
		
		
		sql_expression 	= "SELECT min(price), max(price) FROM products WHERE parent=(%s)"
		minMax = await conn.execute(sql_expression, (cat.id,))
		minMax = await minMax.fetchone()
		
		data['constMin'] = minMax[0]
		data['constMax'] = minMax[1]
		
		sqlMin = "AND price >= {0}" . format(min)
		if min <= 0 or min > data['constMax']:
			sqlMin = ""
			
		sqlMax = "AND price <= {0}" . format(max)
		if max <= 0 or max > data['constMax']:
			sqlMax = ""

		sqlAvalible = ""
		if avalible == "true":
			sqlAvalible = "AND avalible=true"
		
		sqlManufacturer = ""
		if manufacturer != "false":
			sqlManufacturer = "AND manufacturer={0}" . format(manufacturer)

		sql_expression 	= "SELECT * FROM products WHERE parent=(%s) " + sqlManufacturer + " " + sqlAvalible + " " + sqlMin + " " + sqlMax

		product_objs = await conn.execute(sql_expression, (cat.id,))
		product_objs = await product_objs.fetchall()
		
		prdIDS = tuple(p.id for p in product_objs)
	
		#достаем производителей
		manufacturer_objects  = await conn.execute(select([manufacturers.c.id, manufacturers.c.name]).where(manufacturers.c.id.in_([p.manufacturer for p in product_objs])))
		manufacturer_objects  = await manufacturer_objects.fetchall()
		data["manufacturers"] = [{'id': o.id, 'name': o.name} for o in manufacturer_objects]
		
		for product in product_objs:
			
			data['products'].append({
				'id': 				product.id,
				'name': 			product.name,
				'slug':	 			product.slug,
				'poster':			product.poster,
				'price':			product.price,
				'old_price':		product.old_price,
				'avalible':			product.avalible,
				'characteristics': 	[],
				'colors': 			[],
				'active':			True,
			})

		#colors
		colors_objects = []
		colors_objects = await conn.execute(colors.select().where(colors.c.pid.in_(prdIDS)))
		colors_objects = await colors_objects.fetchall()
		
		for product in data['products']:
			for color in colors_objects:
				if product['id'] == color.pid:
					if color.img == "":
						product['colors'].append({
							'id': 		color.id, 
							'name': 	color.name,
							'article':	color.article,
							'poster': 	"",
							'code': 	color.code,
							'default': 	color.default,
						})

					else:
					
						product['colors'].append({
							'id': 		color.id, 
							'name': 	color.name,
							'article':	color.article,
							'poster': 	color.img,
							'code': 	color.code,
							'default': 	color.default,
						})
			
			
			
			# start = time.time()
			
			# #характеристики
			# caps = await conn.execute(cvalues_assoc_products.select().where(cvalues_assoc_products.c.product_id == product.id))
			# caps = await caps.fetchall()
			
			# cvalues_object = await conn.execute(cvalues.select().where(cvalues.c.id.in_([cap.cvalue_id for cap in caps])))
			# cvalues_object = await cvalues_object.fetchall()
			
			# characteristics_object = await conn.execute(characteristics.select().where(characteristics.c.id.in_([cvalue.parent for cvalue in cvalues_object])))
			# characteristics_object = await characteristics_object.fetchall()
			
			# for cvalue in cvalues_object:
				# for characteristic in characteristics_object:
					# if cvalue.parent == characteristic.id:
						# products_info['characteristics'].append({'key': characteristic.name, 'value': cvalue.name})
			
			# end = time.time()
			
			# print(end - start)

	return web.json_response(json.dumps(data))
	

@aiohttp_jinja2.template('catalog.html')
async def categoriesViews(request):

	slug = request.match_info.get('slug', False)
	if not slug:
		web.HTTPNotFound()
	
	context = {}
	
	
	return context
