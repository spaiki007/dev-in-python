#!/usr/bin/env python
# -*- coding: utf-8 -*-

from aiohttp import web
import json
from aiohttp_session import get_session

from es.db import characteristics
from es.db import cvalues
from es.db import cvalues_assoc_products


async def deleteCharacteristics(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	data = await request.post()
	async with request.app['db'].acquire() as conn:
	
		for _, v in data.items():
			
			#находим значения характеристик
			objects = await conn.execute(cvalues.select().where(cvalues.c.parent == v))
			objects = await objects.fetchall()
			
			#удаляем связи значений характеристик
			for object in objects:
				await conn.execute(cvalues_assoc_products.delete().where(cvalues_assoc_products.c.cvalue_id == object.id))
				
			#удаляем связи значения
			await conn.execute(cvalues.delete().where(cvalues.c.parent == v))
			
			#удаляем характеристику
			await conn.execute(characteristics.delete().where(characteristics.c.id == v))

		return web.json_response({'delete': True})

	return web.json_response({'delete': False})


async def addCharacteristics(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	data 	= await request.post()
	name	= data.get('name', False)
	
	async with request.app['db'].acquire() as conn:
		await conn.execute(characteristics.insert().values(name=name))
	return web.json_response({'response': True})

async def getCharacteristics(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	async with request.app['db'].acquire() as conn:
		objects = await conn.execute(characteristics.select())
		objects = await objects.fetchall()
		return web.json_response({'objects': json.dumps([{'id': obj.id, 'name': obj.name, 'checked': False} for obj in objects])})
	return web.json_response({'data': ''})
	
async def getCharacteristic(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	id = request.match_info['id']
	async with request.app['db'].acquire() as conn:
		object = await conn.execute(characteristics.select().where(characteristics.c.id == id))
		object = await object.fetchone()
		return web.json_response({'name': object.name})
	return web.json_response({'': ''})
	
async def updateCharacteristics(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	id	= request.match_info['id']
	data		= await request.post()
	name		= data.get('name', False)
	
	async with request.app['db'].acquire() as conn:
		await conn.execute(characteristics.update().values(name=name).where(characteristics.c.id == id))
		return web.json_response({'response': True})
	return web.json_response({'response': False})

	