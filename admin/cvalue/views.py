#!/usr/bin/env python
# -*- coding: utf-8 -*-

from aiohttp import web
from aiohttp_session import get_session
import json

from es.db import cvalues
from es.db import cvalues_assoc_products


async def deleteCvalues(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	data = await request.post()
	async with request.app['db'].acquire() as conn:
	
		for _, v in data.items():

			#удаляем связи со значениями характеристик
			await conn.execute(cvalues_assoc_products.delete().where(cvalues_assoc_products.c.cvalue_id == v))
			
			#удаляем связи со значения
			await conn.execute(cvalues.delete().where(cvalues.c.id == v))

		return web.json_response({'delete': True})

	return web.json_response({'delete': False})
	

async def addCvalues(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	data 	= await request.post()
	
	name	= data.get('name', False)
	parent	= data.get('parent', False)
	
	async with request.app['db'].acquire() as conn:
		await conn.execute(cvalues.insert().values(name=name, parent=parent))
	return web.json_response({'response': True})

async def getCvalues(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	async with request.app['db'].acquire() as conn:
		objects = await conn.execute(cvalues.select())
		objects = await objects.fetchall()
		return web.json_response({'objects': json.dumps([{'id': obj.id, 'name': obj.name, 'cid': obj.parent, 'checked': False} for obj in objects])})
	return web.json_response({'data': ''})
	
async def getCvalue(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	id = request.match_info['id']
	async with request.app['db'].acquire() as conn:
		object = await conn.execute(cvalues.select().where(cvalues.c.id == id))
		object = await object.fetchone()
		return web.json_response({'name': object.name, 'parent': object.parent})
	return web.json_response({'': ''})
	
async def updateCvalues(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	id	= request.match_info['id']
	data		= await request.post()
	name		= data.get('name', False)
	parent		= data.get('parent', False)
	
	async with request.app['db'].acquire() as conn:
		await conn.execute(cvalues.update().values(name=name, parent=parent).where(cvalues.c.id == id))
		return web.json_response({'response': True})
	return web.json_response({'response': False})
	

