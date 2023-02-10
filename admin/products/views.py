#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from aiohttp_session import get_session

from aiohttp import web

from es.db import categories
from es.db import manufacturers
from es.db import products
from es.db import product_images
from es.db import pickings_assoc_products
from es.db import options_assoc_products
from es.db import cvalues_assoc_products
from es.db import accessories

from api.api import ya_translate

async def deleteProducts(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	data = await request.post()
	async with request.app['db'].acquire() as conn:
	
		for _, v in data.items():
			
			#достаем продукт
			object = await conn.execute(products.select().where(products.c.id == v))
			object = await object.fetchone()
			
			#удаляем фотки из базы
			await conn.execute(product_images.delete().where(product_images.c.product_id == object.id))
			
			#удаляем связи с комплектациями
			await conn.execute(pickings_assoc_products.delete().where(pickings_assoc_products.c.product_id == object.id))
			
			#удаляем связи с опциями
			await conn.execute(options_assoc_products.delete().where(options_assoc_products.c.product_id == object.id))
			
			#удаляем связи с значениями характеристик
			await conn.execute(cvalues_assoc_products.delete().where(cvalues_assoc_products.c.product_id == object.id))
			
			#удаляем связи с аксессуарами
			await conn.execute(accessories.delete().where(accessories.c.parent == object.id))
			
			#удаляем продукт
			await conn.execute(products.delete().where(products.c.id == object.id))
			

		return web.json_response({'delete': True})

	return web.json_response({'delete': False})

async def addProducts(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	data 			= await request.post()
	
	parent			= data.get('parent', False)
	manufacturer	= data.get('manufacturer', False)
	name			= data.get('name', False)
	slug			= data.get('slug', False)
	content			= data.get('content', False)
	
	price			= data.get('price', False)
	old_price		= data.get('old_price', False)
	
	poster			= data.get('poster', False)
	thumbnail		= data.get('thumbnail', False)
	seo_title		= data.get('seo_title', False)
	seo_desc		= data.get('seo_desc', False)
	
	market			= data.get('market', False)
	if market == "true":
		market = True
	else:
		market = False
		
	avalible		= data.get('avalible', False)
	if avalible == "true":
		avalible = True
	else:
		avalible = False
		
	stocksID		= data.get('stocksID', False)

	async with request.app['db'].acquire() as conn:

		#если короткий адрес не установлен то переводим наименование товара
		if not len(slug):
			slug = ya_translate(name)

		productID = await conn.execute(
			products.insert().values(
			
				parent		= parent,
				manufacturer= manufacturer,
				name 		= name,
				content 	= content,
				slug 		= slug,
				price 		= price,
				old_price	= old_price,
				seo_title 	= seo_title,
				seo_desc 	= seo_desc,
				poster 		= poster,
				thumbnail 	= thumbnail,
				market 		= market,
				avalible 	= avalible,
				stocks_id	= stocksID,
				
			).returning(products.c.id)
		)
		
		productID = await productID.fetchone()
		productID = productID[0]
		
	return web.json_response({'response': True, 'id': productID})

async def getProducts(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	async with request.app['db'].acquire() as conn:
	
		objects = await conn.execute(products.select())
		objects = await objects.fetchall()
		
		return web.json_response({'objects': json.dumps([{'id': obj.id, 'name': obj.name, 'checked': False} for obj in objects])})
		
	return web.json_response({'data': ''})
	
	
async def getProduct(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	id = request.match_info['id']
	async with request.app['db'].acquire() as conn:
		object = await conn.execute(products.select().where(products.c.id == id))
		object = await object.fetchone()

		return web.json_response({
		
			'name': 		object.name, 
			'content': 		object.content,
			'slug': 		object.slug,
			'price':		object.price,
			'old_price':	object.old_price,
			'seo_title': 	object.seo_title,
			'seo_desc': 	object.seo_desc,
			'poster': 		object.poster,
			'thumbnail': 	object.thumbnail,
			'market': 		object.market,
			'avalible': 	object.avalible,
			'cid': 			object.parent,
			'mid': 			object.manufacturer,
			'sid':			object.stocks_id,
			
		})

	return web.json_response({'': ''})
	
async def updateProducts(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	id 				= request.match_info['id']
	data 			= await request.post()
	
	parent			= data.get('cid', False)
	manufacturer	= data.get('mid', False)
	stocksID		= data.get('sid', False)
	
	name			= data.get('name', False)
	slug			= data.get('slug', False)
	content			= data.get('content', False)
	price			= data.get('price', False)
	old_price		= data.get('old_price', False)	
	poster			= data.get('poster', False)
	thumbnail		= data.get('thumbnail', False)
	seo_title		= data.get('seo_title', False)
	seo_desc		= data.get('seo_desc', False)
	
	market			= data.get('market', False)
	if market == "true":
		market = True
	else:
		market = False
		
	avalible		= data.get('avalible', False)
	if avalible == "true":
		avalible = True
	else:
		avalible = False
	
	async with request.app['db'].acquire() as conn:
		
		#если короткий адрес не установлен то переводим наименование товара
		if not len(slug):
			slug = ya_translate(name)
			
		await conn.execute(
			products.update().values(
			
				parent		= parent,
				manufacturer= manufacturer,
				name 		= name,
				content 	= content,
				slug 		= slug,
				price 		= price,
				old_price	= old_price,
				poster		= poster,
				thumbnail	= thumbnail,
				seo_title 	= seo_title,
				seo_desc 	= seo_desc,
				market 		= market,
				avalible 	= avalible,
				stocks_id	= stocksID,
				
			).where(products.c.id == id)
		)
		
		return web.json_response({'response': True})
		
	return web.json_response({'response': False})
