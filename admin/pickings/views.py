#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from aiohttp import web
from aiohttp_session import get_session

from es.db import pickings
from es.db import pickings_assoc_products

async def deletePickings(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	data = await request.post()
	async with request.app['db'].acquire() as conn:
	
		for _, v in data.items():
		
			await conn.execute(pickings_assoc_products.delete().where(pickings_assoc_products.c.picking_id == v))
			await conn.execute(pickings.delete().where(pickings.c.id == v))

		return web.json_response({'delete': True})

	return web.json_response({'delete': False})

async def addPickings(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	data = await request.post()
	
	name	= data.get('name', False)
	img		= data.get('poster', False)
	
	async with request.app['db'].acquire() as conn:

		objectID = await conn.execute(
			pickings.insert().values(
				name = name,
				img	 = img,
			).returning(pickings.c.id)
		)
		
		objectID = await objectID.fetchone()
		objectID = objectID[0]

	return web.json_response({'response': True, 'id': objectID})

async def getPickings(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	async with request.app['db'].acquire() as conn:
		objects = await conn.execute(pickings.select())
		objects = await objects.fetchall()
		return web.json_response({'objects': json.dumps([{'id': obj.id, 'name': obj.name, 'checked': False, 'active': False} for obj in objects])})
	return web.json_response({'data': ''})
	
	
async def getPicking(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	id = request.match_info['id']
	async with request.app['db'].acquire() as conn:
		object = await conn.execute(pickings.select().where(pickings.c.id == id))
		object = await object.fetchone()

		return web.json_response({
			'name': object.name,
			'img':  object.img, 
		})

	return web.json_response({'': ''})
	
async def updatePickings(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	id		= request.match_info['id']
	data 	= await request.post()
	
	name	= data.get('name', False)
	img		= data.get('poster', False)
	
	async with request.app['db'].acquire() as conn:
	
		object = await conn.execute(pickings.select().where(pickings.c.id == id))
		object = await object.fetchone()

		await conn.execute(pickings.update().values(name=name, img=img).where(pickings.c.id == id))
		
		return web.json_response({'response': True})
		
	return web.json_response({'response': False})
	