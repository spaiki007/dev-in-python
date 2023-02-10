#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from aiohttp import web
from aiohttp_session import get_session

from es.db import gifts

async def deleteGifts(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	data = await request.post()
	async with request.app['db'].acquire() as conn:
	
		for _, v in data.items():
			await conn.execute(gifts.delete().where(gifts.c.id == v))

		return web.json_response({'delete': True})

	return web.json_response({'delete': False})
	

async def addGifts(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	data = await request.post()
	
	name	= data.get('name', False)
	img		= data.get('poster', False)
	parent	= data.get('parent', False)
	
	async with request.app['db'].acquire() as conn:

		objectID = await conn.execute(
			gifts.insert().values(

				name	= name,
				img		= img,
				parent	= parent,
				
			).returning(gifts.c.id)
		)
		
		objectID = await objectID.fetchone()
		objectID = objectID[0]

	return web.json_response({'response': True, 'id': objectID})

async def getGifts(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	async with request.app['db'].acquire() as conn:
		objects = await conn.execute(gifts.select())
		objects = await objects.fetchall()
		return web.json_response({'objects': json.dumps([{'id': obj.id, 'name': obj.name, 'checked': False, 'active': False} for obj in objects])})
	return web.json_response({'data': ''})
	
	
async def getGift(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	id = request.match_info['id']
	async with request.app['db'].acquire() as conn:
		object = await conn.execute(gifts.select().where(gifts.c.id == id))
		object = await object.fetchone()

		return web.json_response({
		
			'name':		object.name,
			'img':		object.img, 
			'parent':	object.parent,
			
		})

	return web.json_response({'': ''})
	
async def updateGifts(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	id		= request.match_info['id']
	data	= await request.post()
	
	name	= data.get('name', False)
	img		= data.get('poster', False)
	parent	= data.get('parent', False)
	
	async with request.app['db'].acquire() as conn:
	
		object = await conn.execute(gifts.select().where(gifts.c.id == id))
		object = await object.fetchone()

		await conn.execute(
			gifts.update().values(
				name 	= name,
				img		= img,
				parent	= parent,
			).where(gifts.c.id == id)
		)

		return web.json_response({'response': True})
		
	return web.json_response({'response': False})