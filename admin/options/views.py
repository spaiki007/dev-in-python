#!/usr/bin/env python
# -*- coding: utf-8 -*-

from aiohttp import web
from aiohttp_session import get_session
import json
from es.db import options
from es.db import options_assoc_products

async def addOptions(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	data 	= await request.post()
	name	= data.get('name', False)
	price	= data.get('price', False)
	
	async with request.app['db'].acquire() as conn:
		await conn.execute(options.insert().values(name=name, price=price))
	return web.json_response({'response': True})

async def getOptions(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	async with request.app['db'].acquire() as conn:
		objects = await conn.execute(options.select())
		objects = await objects.fetchall()
		return web.json_response({'objects': json.dumps([{'id': obj.id, 'name': obj.name, 'checked': False, 'active': False} for obj in objects])})
	return web.json_response({'data': ''})
	
async def getOption(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	id = request.match_info['id']
	async with request.app['db'].acquire() as conn:
		object = await conn.execute(options.select().where(options.c.id == id))
		object = await object.fetchone()
		return web.json_response({
			'name': 		object.name,
			'price': 		object.price, 
		})
	return web.json_response({'': ''})
	
async def updateOptions(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	id	= request.match_info['id']
	data		= await request.post()
	name		= data.get('name', False)
	price		= data.get('price', False)
	
	async with request.app['db'].acquire() as conn:
		await conn.execute(options.update().values(name=name, price=price).where(options.c.id == id))
		return web.json_response({'response': True})
	return web.json_response({'response': False})
	
async def deleteOptions(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	data = await request.post()
	async with request.app['db'].acquire() as conn:
	
		for _, v in data.items():

			await conn.execute(options_assoc_products.delete().where(options_assoc_products.c.option_id == v))
			await conn.execute(options.delete().where(options.c.id == v))

		return web.json_response({'delete': False})

	return web.json_response({'delete': False})

	