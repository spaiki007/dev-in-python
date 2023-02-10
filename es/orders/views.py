#!/usr/bin/env python
# -*- coding: utf-8 -*-

from aiohttp import web
import aiohttp_jinja2, json
from aiohttp_session import get_session
from sqlalchemy import and_

from es.db import orders
from es.db import quickOrders
from es.db import products
from es.db import gifts
from es.db import options


async def quickOrder(request):

	data	= await request.post()
	
	pid 		= data.get('pid', False)
	cid 		= data.get('cid', False)
	name 		= data.get('name', False)
	phone 		= data.get('phone', False)
	comment 	= data.get('comments', False)
	
	async with request.app['db'].acquire() as conn:
	
		article 	= data.get('article', False)
		if article:
			#достаем артикул
			article = await conn.execute(articles.select().where(articles.c.id == article))
			article = await article.fetchone()
			
			pid = str(article.pds_id)
			cid = str(article.cls_id)
		
		
		if pid and cid and name and phone:
			if len(pid) > 0 and len(cid) > 0 and len(name) > 0 and len(phone) > 0:
			
				#достаем артикул
				article = await conn.execute(articles.select().where(and_(articles.c.pds_id == pid, articles.c.cls_id == cid)))
				article = await article.fetchone()

				if article is not None:
				
					product = await conn.execute(products.select().where(products.c.id == article.pds_id))
					product = await product.fetchone()
					
					info = "({}) {} {}р.\n" . format(article.name, product.name, product.price)
					
					await conn.execute(quickOrders.insert().values(
						name	= name,
						phone	= phone,
						comment	= comment,
						info	= info,
					))
					
					return web.json_response({'response': json.dumps(True)})
			
	return web.json_response({'response': json.dumps(False)})


async def order(request):
	
	session = await get_session(request)
	ses_products = session.get('products', False)
	ses_products = json.loads(ses_products)
	
	data 		= await request.post()
	firtName 	= data.get('firtName', False)
	lastName 	= data.get('lastName', False)
	phone 		= data.get('phone', False)
	email 		= data.get('email', False)
	adress 		= data.get('adress', False)
	comment 	= data.get('comment', False)
	
	payment 	= data.get('payment', False)
	delivery 	= data.get('delivery', False)
	raw_products= data.get('products', False)

	if firtName and lastName and phone and email and adress and payment and delivery and raw_products:
		if len(firtName) > 0 and len(lastName) > 0 and len(phone) > 0 and len(email) > 0 and len(adress) > 0 and len(payment) > 0 and len(delivery) > 0 and len(raw_products) > 0:
			raw_products = json.loads(raw_products)
			
			async with request.app['db'].acquire() as conn:
		
				#достаем артикулы
				article_objects = await conn.execute(articles.select().where(articles.c.id.in_([article['id'] for article in raw_products])))
				article_objects = await article_objects.fetchall()
				if article_objects is not None:
				
					product_objects = await conn.execute(products.select().where(products.c.id.in_([article.pds_id for article in article_objects])))
					product_objects = await product_objects.fetchall()
					
					info = ''
					for article in article_objects:
						for product in product_objects:
							for rarticle in raw_products:
								if article.pds_id == product.id and rarticle['id'] == article.id:
									
									info += "({}) {} {}р. кол-во: {}\n" . format(article.name, product.name, product.price, rarticle['count'])
									article_ses = ses_products.get(str(article.id), False)
									
									giftID = ses_products[str(article.id)]['giftID']
									if len(giftID):
									
										gift = await conn.execute(gifts.select().where(gifts.c.id == giftID))
										gift = await gift.fetchone()
										info += "Подарок:\n"
										info += "  -{}\n" . format(gift.name)
										
									optionIDS = ses_products[str(article.id)]['optionIDS']
									if len(optionIDS):
										
										options_objects = await conn.execute(options.select().where(options.c.id.in_(optionIDS)))
										options_objects = await options_objects.fetchall()
										
										info += "Опции:\n"
										for option in options_objects:
											info += "  -{}: {}р.\n" . format(option.name, option.price)

					await conn.execute(orders.insert().values(
						firtName= firtName,
						lastName= lastName,
						phone	= phone,
						email	= email,
						adress	= adress,
						comment	= comment,
						info	= info,
					))
					
					session['products'] = json.dumps({})
					
					return web.json_response({'response': json.dumps(True)})
			
	return web.json_response({'response': json.dumps(False)})
	