#!/usr/bin/env python
# -*- coding: utf-8 -*-

from aiohttp import web
import aiohttp_jinja2, json, math, random
from aiohttp_session import get_session

from es.db import categories

from es.db import products
from es.db import manufacturers

from es.db import accessories

from es.db import colors
from es.db import product_images

from es.db import pickings
from es.db import pickings_assoc_products

from es.db import options
from es.db import options_assoc_products

from es.db import stocks
from es.db import gifts

from es.db import characteristics
from es.db import cvalues
from es.db import cvalues_assoc_products

from es.db import roles
from es.db import users
from es.db import comments


async def delBasket(request):
	
	id = request.query.get('id', False)
	if not id:
		return web.json_response({'response': False})
		
	session = await get_session(request)
	ses_products = session.get('products', False)
	ses_products = json.loads(ses_products)

	ses_products.pop(id, False) 
	session['products'] = json.dumps(ses_products)

	return web.json_response({'response': json.dumps(True)})
	
async def addBasket(request):
	
	data    = await request.post()
	order 	= data.get('order', False)
	if order:
		order = json.loads(order)

	async with request.app['db'].acquire() as conn:
		
		#достаем артикул
		color = await conn.execute(colors.select().where(colors.c.id == order['id']))
		color = await color.fetchone()
		
		if color is not None:
			
			session = await get_session(request)
			ses_products = session.get('products', False)
			if not ses_products:
			
				ses_products = {}
				ses_products[color.id] = {'giftID': order['giftID'], 'optionIDS': order['optionIDS']}
				session['products'] = json.dumps(ses_products)
				
			else:
				ses_products = json.loads(ses_products)
				if len(ses_products) < 50:
					if not ses_products.get(color.id, False):
						ses_products[color.id] = {'giftID': order['giftID'], 'optionIDS': order['optionIDS']}
						session['products'] = json.dumps(ses_products)

	return web.json_response({'response': json.dumps(True)})


async def getBasket(request):
	
	session = await get_session(request)
	objects = session.get('products', False)
	if objects:
		
		colorsIDS = json.loads(objects)
		async with request.app['db'].acquire() as conn:
			
			#достаем артикул
			color_objects = await conn.execute(colors.select().where(colors.c.id.in_(colorsIDS.keys())))
			color_objects = await color_objects.fetchall()
			
			images_objects = await conn.execute(product_images.select().where(product_images.c.cid.in_(colorsIDS.keys())))
			images_objects = await images_objects.fetchall()
			
			product_objects = await conn.execute(products.select().where(products.c.id.in_([color.pid for color in color_objects])))
			product_objects = await product_objects.fetchall()

			listObjects = []
			
			for product in product_objects:
				for color in color_objects:
					for image in images_objects:
					
						if product.id == color.pid and color.id == image.cid:
						
							listObjects.append({
								'cid': color.id,
								'product': {
									'name': product.name,
									'slug': product.slug,
									'price': product.price,
									'image': image.name,
									'count': 1,
								},
							})
							break
									
				return web.json_response({'response': json.dumps(listObjects)})
				
			#session['products'] = json.dumps(ses_products)
			
	return web.json_response({'response': json.dumps([])})


async def similarProducts(request):

	slug = request.query.get('slug', False)
	if not slug:
		return web.json_response({'objects': json.dumps([])})

	#достаем продукт
	async with request.app['db'].acquire() as conn:
		
		#product
		product = await conn.execute(products.select().where(products.c.slug == slug))
		product = await product.fetchone()

		min = product.price - 10000
		max = product.price + 10000
		
		if product is None:
			return web.json_response({'objects': json.dumps([])})

		#products
		products_objects = await conn.execute(products.select().where(products.c.parent == product.parent))
		products_objects = await products_objects.fetchall()

		#удаляем уже имеющийся
		products_objects.remove(product)
		
		prdIDS = tuple(p.id for p in products_objects)

		productList = []
		for product in products_objects:
			if product.price > min and product.price < max:
				productList.append(product)

		product_objects = []
		for product in productList:
			product_objects.append({
				'id': 				product.id,
				'name': 			product.name,
				'slug':	 			product.slug,
				'poster':			product.poster,
				'price':			product.price,
				'old_price':		product.old_price,
				'characteristics': 	[],
				'colors': 			[],
			})
			
		#colors
		colors_objects = []
		colors_objects = await conn.execute(colors.select().where(colors.c.pid.in_(prdIDS)))
		colors_objects = await colors_objects.fetchall()
		
		for product in product_objects:
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
				
		#характеристики
		caps = await conn.execute(cvalues_assoc_products.select().where(cvalues_assoc_products.c.product_id.in_(prdIDS)))
		caps = await caps.fetchall()
		
		cvalues_object = await conn.execute(cvalues.select().where(cvalues.c.id.in_([cap.cvalue_id for cap in caps])))
		cvalues_object = await cvalues_object.fetchall()
		
		characteristics_object = await conn.execute(characteristics.select().where(characteristics.c.id.in_([cvalue.parent for cvalue in cvalues_object])))
		characteristics_object = await characteristics_object.fetchall()
		
		for product in product_objects:
			for characteristic in characteristics_object:
				for cvalue in cvalues_object:
					for cap in caps:
						if product.id == cap.product_id and cap.cvalue_id == cvalue.id and cvalue.parent == characteristic.id:
							product['characteristics'].append({'key': characteristic.name, 'value': cvalue.name})

		return web.json_response({'objects': json.dumps(product_objects)})
	

async def productSliderGet(request):

	objects = []
	
	slug = request.query.get('slug', False)
	if not slug:
		return web.json_response({'objects': json.dumps(objects)})

	#достаем продукт
	async with request.app['db'].acquire() as conn:
		
		#product
		product = await conn.execute(products.select().where(products.c.slug == slug))
		product = await product.fetchone()
		
		if product is None:
			return web.json_response({'objects': json.dumps(objects)})

		#accessories
		accessories_objects = await conn.execute(accessories.select().where(accessories.c.parent == product.id))
		accessories_objects = await accessories_objects.fetchall()
		listAcessID = [p.pid for p in accessories_objects]
		
		#products acessories
		productList = await conn.execute(products.select().where(products.c.id.in_(listAcessID)))
		productList = await productList.fetchall()
		
		prdIDS = tuple(p.id for p in productList)
		
		product_objects = []
		for prd in productList:
			product_objects.append({
				'id': 				prd.id,
				'name': 			prd.name,
				'slug':	 			prd.slug,
				'poster':			prd.poster,
				'price':			prd.price,
				'old_price':		prd.old_price,
				'colors': 			[],
			})
			
		#colors
		colors_objects = []
		colors_objects = await conn.execute(colors.select().where(colors.c.pid.in_(prdIDS)))
		colors_objects = await colors_objects.fetchall()

		for prd in product_objects:
			for color in colors_objects:
				if prd['id'] == color.pid:
					if color.img == "":
						prd['colors'].append({
							'id': 		color.id, 
							'name': 	color.name,
							'article':	color.article,
							'poster': 	"",
							'code': 	color.code,
							'default': 	color.default,
						})

					else:
						prd['colors'].append({
							'id': 		color.id, 
							'name': 	color.name,
							'article':	color.article,
							'poster': 	color.img,
							'code': 	color.code,
							'default': 	color.default,
						})
		
	return web.json_response({'objects': json.dumps(product_objects)})

async def addProductsComments(request):
	
	data		= await request.post()
	productID	= data.get('productID', False)
	if not productID:
		return web.json_response(json.dumps({'response': False}))
		
	#достаем продукт
	async with request.app['db'].acquire() as conn:
		
		#product
		product = await conn.execute(products.select().where(products.c.id == productID))
		product = await product.fetchone()
		
		if product is None:
			return web.json_response(json.dumps({'response': False}))

		user_name 		= data.get('user_name', False)
		user_city 		= data.get('user_city', False)
		rating 			= data.get('rating', False)
		user_positive 	= data.get('user_positive', False)
		user_negative 	= data.get('user_negative', False)
		user_comment 	= data.get('user_comment', False)

		if not(user_name and user_city and rating and user_comment):
			return web.json_response(json.dumps({'response': False, 'err': 'Заполните все поля помеченные *.'}))

		if len(user_name) < 0 or len(user_name) > 255:
			return web.json_response(json.dumps({'response': False, 'err': 'Поле имя не может быть менее 0 и не должно превышать 255 символов.'}))

		if len(user_city) < 0 or len(user_city) > 255:
			return web.json_response(json.dumps({'response': False, 'err': 'Поле город не может быть менее 0 и не должно превышать 255 символов.'}))
			
		if int(rating) < 0 or int(rating) > 5:
			return web.json_response(json.dumps({'response': False, 'err': 'Рейтинг не может быть менее 0 и более 5.'}))
			
		if len(user_positive) < 0 or len(user_positive) > 250:
			return web.json_response(json.dumps({'response': False, 'err': 'Поле плюсы не должно превышать 250 символов.'}))
			
		if len(user_negative) < 0 or len(user_negative) > 250:
			return web.json_response(json.dumps({'response': False, 'err': 'Поле минусы не должно превышать 250 символов.'}))

		if len(user_comment) < 0 or len(user_comment) > 1000:
			return web.json_response(json.dumps({'response': False, 'err': 'Поле комментарий не может быть менее 0 и не должно превышать 1000 символов.'}))
			

		async with request.app['db'].acquire() as conn:

			sum = "qwertyuiopasdfghjklzxcvbnm"
			
			#генерируем логин юзера
			user_login = ''.join([random.choice(sum) for _ in range(10)])
			
			#генерируем пароль юзера
			user_pass = ''.join([random.choice(sum) for _ in range(10)])
			
			role = await conn.execute(roles.select().where(roles.c.name == "user"))
			role = await role.fetchone()
			
			userID = await conn.execute(
				users.insert().values(
					role  		= role.id,
					login 		= user_login,
					user_name 	= user_name,
					passw 		= user_pass,
					city 		= user_city,
				).returning(users.c.id)
			)
			userID = await userID.fetchone()
			userID = userID[0]

			await conn.execute(comments.insert().values(
				name		= user_comment,
				positive	= user_positive,
				negative	= user_negative,
				rating		= rating,
				pid			= product.id,
				uid			= userID,
				
			))

		return web.json_response(json.dumps({'response': True}))

@aiohttp_jinja2.template('product.html')
async def productViews(request):

	slug = request.match_info.get('slug', False)
	if not slug:
		web.HTTPNotFound()
	
	context = {}
	
	#достаем продукт
	async with request.app['db'].acquire() as conn:
		
		#product
		product = await conn.execute(products.select().where(products.c.slug == slug))
		product = await product.fetchone()
		
		if product is None:
			raise web.HTTPNotFound()
		context['product'] = product
		
		#procent
		procent = False
		if product.old_price:
			procent = ((product.old_price - product.price) * 100) / product.old_price
			procent = math.ceil(procent)
		context['procent'] = procent
		
		#categories
		category = await conn.execute(categories.select().where(categories.c.id == product.parent))
		category = await category.fetchone()
		context['category'] = category

		#manufacturer
		manufacturer = await conn.execute(manufacturers.select().where(manufacturers.c.id == product.manufacturer))
		manufacturer = await manufacturer.fetchone()
		context['manufacturer'] = manufacturer
		
		#colors
		color_objects = await conn.execute(colors.select().where(colors.c.pid == product.id))
		color_objects = await color_objects.fetchall()
		context['colors'] = color_objects

		#images
		product_image_objects = await conn.execute(product_images.select().where(product_images.c.cid.in_(tuple(c.id for c in color_objects))))
		product_image_objects = await product_image_objects.fetchall()
		context['images'] = product_image_objects

		#подарки
		paps = await conn.execute(pickings_assoc_products.select().where(pickings_assoc_products.c.product_id == product.id))
		paps = await paps.fetchall()
		
		pickings_object = await conn.execute(pickings.select().where(pickings.c.id.in_(tuple(pap.picking_id for pap in paps))))
		pickings_object = await pickings_object.fetchall()
		context['pickings'] = pickings_object
		
		#опции
		oaps = await conn.execute(options_assoc_products.select().where(options_assoc_products.c.product_id == product.id))
		oaps = await oaps.fetchall()

		options_object = False
		if oaps is not None:
			options_object = await conn.execute(options.select().where(options.c.id.in_([oap.option_id for oap in oaps])))
			options_object = await options_object.fetchall()
		context['options'] = options_object


		stock_object = False
		if product.stocks_id:
			#акции
			stock_object = {}
			stock = await conn.execute(stocks.select().where(stocks.c.id == product.stocks_id))
			stock = await stock.fetchone()
			stock_object['stock'] = stock
			
			gifts_objects = await conn.execute(gifts.select().where(gifts.c.parent == stock.id))
			gifts_objects = await gifts_objects.fetchall()
			stock_object['gifts'] = gifts_objects
			
		context['stock'] = stock_object
		
		#характеристики
		ids_assoc_caps = []
		caps = await conn.execute(cvalues_assoc_products.select().where(cvalues_assoc_products.c.product_id == product.id))
		caps = await caps.fetchall()
		
		cvalues_object = await conn.execute(cvalues.select().where(cvalues.c.id.in_([cap.cvalue_id for cap in caps])))
		cvalues_object = await cvalues_object.fetchall()
		
		characteristics_object = await conn.execute(characteristics.select().where(characteristics.c.id.in_([cvalue.parent for cvalue in cvalues_object])))
		characteristics_object = await characteristics_object.fetchall()
		
		characteristics_list = []
		for cvalue in cvalues_object:
			for characteristic in characteristics_object:
				if cvalue.parent == characteristic.id:
					characteristics_list.append(
						{
							'characteristic': characteristic,
							'cvalue': cvalue,
						}
					)
					
		context['characteristics'] = characteristics_list
		
		comments_sql = """
			SELECT r.name AS role_name, u.user_name, u.city, c.* 
			FROM roles r, users u, comments c 
			WHERE c.pid={} AND u.id=c.uid AND status=true AND u.role=r.id 
			ORDER BY created DESC
		""" . format(product.id)
		
		comments_objs = await conn.execute(comments_sql)
		comments_objs = await comments_objs.fetchall()
		
		context['comments'] = comments_objs
		
	return context
