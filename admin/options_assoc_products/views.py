#!/usr/bin/env python
# -*- coding: utf-8 -*-

from aiohttp import web
from aiohttp_session import get_session
import json
from es.db import options_assoc_products
	
async def addOaps(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	data = await request.post()
	
	pid	= data.get('pid', False)
	oid = data.get('oid', False)
	
	async with request.app['db'].acquire() as conn:
		await conn.execute(options_assoc_products.insert().values(product_id=pid, option_id=oid))
	return web.json_response({'response': True})
	
async def getOaps(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	id = request.match_info['id']
	async with request.app['db'].acquire() as conn:
		objs = await conn.execute(options_assoc_products.select().where(options_assoc_products.c.product_id == id))
		objs = await objs.fetchall()
		return web.json_response({'objects': json.dumps([{'id': obj.id, 'pid': obj.product_id, 'oid': obj.option_id} for obj in objs])})
	return web.json_response({'': ''})
	
async def deleteOaps(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})

	id = request.match_info['id']
	async with request.app['db'].acquire() as conn:
		await conn.execute(options_assoc_products.delete().where(options_assoc_products.c.id == id))
		return web.json_response({'objects': True})
	
