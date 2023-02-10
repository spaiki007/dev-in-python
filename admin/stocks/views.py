#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json, psycopg2, shutil
from aiohttp import web
from aiohttp_session import get_session

from es.db import stocks

async def deleteStocks(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	data = await request.post()
	async with request.app['db'].acquire() as conn:
	
		for _, v in data.items():
			await conn.execute(stocks.delete().where(stocks.c.id == v))
		return web.json_response({'delete': True})

	return web.json_response({'delete': False})


async def getStocks(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	async with request.app['db'].acquire() as conn:
		objects = await conn.execute(stocks.select())
		return web.json_response({'objects': json.dumps([{'id': obj.id, 'name': obj.name, 'checked': False} for obj in await objects.fetchall()])})
		
	return web.json_response({'data': ''})
	
	
async def addStocks(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	data		= await request.post()
	
	name 		= data.get('name', False)
	start 		= data.get('start', False)
	end 		= data.get('end', False)

	async with request.app['db'].acquire() as conn:
		await conn.execute(stocks.insert().values(
			name		= name,
			start		= start,
			end			= end,
		))
		return web.json_response({'response': True})

	return web.json_response({'response': False, "err": ""})

async def getStock(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	id = request.match_info['id']
	async with request.app['db'].acquire() as conn:
		object = await conn.execute(stocks.select().where(stocks.c.id == id))
		object = await object.fetchone()
		
		return web.json_response({
			'id': 		object.id,
			'name': 	object.name,
			'start': 	object.start.isoformat(),
			'end': 		object.end.isoformat(),
		})

	return web.json_response({'': ''})
	
async def updateStocks(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	id 			= request.match_info['id']
	data 		= await request.post()
	
	name 		= data.get('name', False)
	start 		= data.get('start', False)
	end 		= data.get('end', False)

	async with request.app['db'].acquire() as conn:
		await conn.execute(stocks.update().values(
			name		= name,
			start		= start,
			end			= end,
		).where(stocks.c.id == id))
		
		return web.json_response({'response': True})

	return web.json_response({'response': False,})
