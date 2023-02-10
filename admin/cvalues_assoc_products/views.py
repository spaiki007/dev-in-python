#!/usr/bin/env python
# -*- coding: utf-8 -*-

from aiohttp import web
from aiohttp_session import get_session
import json

import sqlalchemy as sa

from es.db import cvalues_assoc_products
	
	
async def addCaps(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	data = await request.post()
	
	pid	= data.get('pid', False)
	cid = data.get('cid', False)

	async with request.app['db'].acquire() as conn:
		await conn.execute(
			cvalues_assoc_products.insert().values(
				product_id	= pid,
				cvalue_id	= cid,
			)
		)

	return web.json_response({'response': True})
	
async def getCaps(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	id = request.match_info['id']
	async with request.app['db'].acquire() as conn:
	
		objs = await conn.execute(cvalues_assoc_products.select().where(cvalues_assoc_products.c.product_id == id))
		objs = await objs.fetchall()
		
		return web.json_response({'objects': json.dumps([{'id': obj.id, 'pid': obj.product_id, 'cvid': obj.cvalue_id,} for obj in objs])})

	return web.json_response({'': ''})
	
async def deleteCaps(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	id = request.match_info['id']
	
	async with request.app['db'].acquire() as conn:
		await conn.execute(cvalues_assoc_products.delete().where(cvalues_assoc_products.c.id == id))
		return web.json_response({'objects': True})

	return web.json_response({'delete': False})
