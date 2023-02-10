#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from aiohttp import web
from aiohttp_session import get_session

from es.db import products
from es.db import product_images
	
async def deleteImage(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	id = request.match_info['id']
	async with request.app['db'].acquire() as conn:
	
		await conn.execute(product_images.delete().where(product_images.c.id == id))
		return web.json_response({'delete': True})
		
	return web.json_response({'delete': False})

async def getImages(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
	
	id = request.match_info['id']
	async with request.app['db'].acquire() as conn:
	
		objects = await conn.execute(product_images.select().where(product_images.c.cid == id))
		objects = await objects.fetchall()
		
		return web.json_response({
			'objects': json.dumps([{'id': obj.id, 'name': obj.name, "cid": obj.cid} for obj in objects])
		})
		
	return web.json_response({'data': ''})


async def addImages(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	data = await request.post()
	
	name = data.get('name', False)
	cid	 = data.get('cid', False)

	async with request.app['db'].acquire() as conn:
		await conn.execute(
			product_images.insert().values(
				name	= name,
				cid 	= cid,
			)
		)

	return web.json_response({'response': True})
