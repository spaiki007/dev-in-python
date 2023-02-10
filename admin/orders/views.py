#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json, psycopg2
from aiohttp import web
from aiohttp_session import get_session

from es.db import orders


async def deleteOrders(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	data = await request.post()
	async with request.app['db'].acquire() as conn:
		for _, v in data.items():
			await conn.execute(orders.delete().where(orders.c.id == v))
		return web.json_response({'delete': False})

	return web.json_response({'delete': False})

async def getOrders(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	async with request.app['db'].acquire() as conn:
		objects = await conn.execute(orders.select())
		return web.json_response({'objects': json.dumps([{'id': obj.id, 'name': obj.created.strftime("%Y-%m-%d %H.%M.%S"), 'checked': False} for obj in await objects.fetchall()])})
		
	return web.json_response({'data': ''})

async def getOrder(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	id = request.match_info['id']
	async with request.app['db'].acquire() as conn:
		object = await conn.execute(orders.select().where(orders.c.id == id))
		object = await object.fetchone()

		return web.json_response({
			'firtName': object.firtName,
			'lastName': object.lastName,
			'phone': 	object.phone,
			'email': 	object.email,
			'comment': 	object.comment,
			'adress': 	object.adress,
			'info': 	object.info,
			'status': 	object.status,
			'created': 	object.created.strftime("%Y-%m-%d %H.%M.%S"),
		})

	return web.json_response({'': ''})

async def updateOrders(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	id 	= request.match_info['id']
	data = await request.post()
	
	status = data.get('status', False)
	
	async with request.app['db'].acquire() as conn:

		await conn.execute(orders.update().values(
			status = status,
		).where(orders.c.id == id))
		
		return web.json_response({'response': True})

	return web.json_response({'response': False, "err": ""})
