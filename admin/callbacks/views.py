#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json, psycopg2
from aiohttp import web
from aiohttp_session import get_session

from es.db import callbacks


async def deleteCallbacks(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	data = await request.post()
	async with request.app['db'].acquire() as conn:
		for _, v in data.items():
			await conn.execute(callbacks.delete().where(callbacks.c.id == v))
		return web.json_response({'delete': False})

	return web.json_response({'delete': False})

async def getCallbacks(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	async with request.app['db'].acquire() as conn:
		objects = await conn.execute(callbacks.select())
		return web.json_response({'objects': json.dumps([{'id': obj.id, 'name': obj.created.strftime("%Y-%m-%d %H:%M:%S"), 'checked': False} for obj in await objects.fetchall()])})
		
	return web.json_response({'data': ''})

async def getCallback(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	id = request.match_info['id']
	async with request.app['db'].acquire() as conn:
		object = await conn.execute(callbacks.select().where(callbacks.c.id == id))
		object = await object.fetchone()

		return web.json_response({
			'name': 	object.name,
			'phone': 	object.phone,
			'call_time':object.call_time,
			'status': 	object.status,
			'created': 	object.created.strftime("%Y-%m-%d %H:%M:%S"),
		})

	return web.json_response({'': ''})

async def updateCallbacks(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	id 	= request.match_info['id']
	data = await request.post()
	
	status = data.get('status', False)
	
	async with request.app['db'].acquire() as conn:

		await conn.execute(callbacks.update().values(
			status = status,
		).where(callbacks.c.id == id))
		
		return web.json_response({'response': True})

	return web.json_response({'response': False, "err": ""})
