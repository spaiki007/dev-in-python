#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json, random, psycopg2
from aiohttp import web
from aiohttp_session import get_session

from es.db import colors
from es.db import product_images
	
async def deleteColors(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})

	id = request.match_info['id']
	async with request.app['db'].acquire() as conn:

		#удаляем фотки из базы
		await conn.execute(product_images.delete().where(product_images.c.cid == id))
		
		#удаляем цвет
		await conn.execute(colors.delete().where(colors.c.id == id))

		return web.json_response({'response': True})
		
	return web.json_response({'delete': False})
	

async def getColor(request):
	
	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	id = request.match_info['id']
	async with request.app['db'].acquire() as conn:
		object = await conn.execute(colors.select().where(colors.c.id == id))
		object = await object.fetchone()
		return web.json_response({
			'name': 	object.name,
			'article': 	object.article,
			'img': 		object.img,
			'code':		object.code,
			'default':	obj.default,
			'pid':		object.pid,
		})
		
	return web.json_response({'': ''})
	
async def getColors(request):

	if not request.app['debug']:
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})

	id = request.match_info['id']
	async with request.app['db'].acquire() as conn:
	
		objects = await conn.execute(colors.select().where(colors.c.pid == id))
		objects = await objects.fetchall()
		
		return web.json_response({'objects': json.dumps([{
			'id': 			obj.id, 
			'name': 		obj.name, 
			'article': 		obj.article,
			'img': 			obj.img,
			'code':			obj.code,
			'default':		obj.default,
			'pid':			obj.pid,
			'checked': 		False,
			'active': 		False,
			'images': 		[]
		} for obj in objects])})

	return web.json_response({'data': ''})

async def addColors(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	data 	= await request.post()
	
	pid 	= data.get('pid', False)
	name 	= data.get('name', False)
	article	= data.get('article', False)
	img 	= data.get('img', False)
	code 	= data.get('code', False)
	default	= data.get('default', False)
	if default == "true":
		default = True
	else:
		default = False

	async with request.app['db'].acquire() as conn:
		
		try:
			await conn.execute(colors.insert().values(
					name	= name,
					article	= article,
					img 	= img,
					code 	= code,
					default = default,
					pid 	= pid,
				)
			)
			return web.json_response({'response': True})
		except psycopg2.IntegrityError:
			return web.json_response({'response': False, "err": "Такой артикуль уже существует!"})
		
	return web.json_response({'response': False, "err": ""})
	
async def updateColors(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})

	id = request.match_info['id']
	data = await request.post()
	
	name 	= data.get('name', False)
	article	= data.get('article', False)
	img 	= data.get('img', False)
	code 	= data.get('code', False)
	default	= data.get('default', False)
	if default == "true":
		default = True
	else:
		default = False

	async with request.app['db'].acquire() as conn:
	
		try:
			await conn.execute(colors.update().values(
				name	= name,
				article	= article,
				img		= img,
				code	= code,
				default = default,
			).where(colors.c.id == id))
			
			return web.json_response({'response': True})
			
		except psycopg2.IntegrityError:
			return web.json_response({'response': False, "err": "Такой артикуль уже существует!"})

