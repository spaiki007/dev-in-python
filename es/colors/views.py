#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json, psycopg2
from aiohttp import web
from es.db import colors

async def getColor(request):
	
	objectID = request.match_info['objectID']
	async with request.app['db'].acquire() as conn:
		object = await conn.execute(colors.select().where(colors.c.id == objectID))
		object = await object.fetchone()
		return web.json_response({'name': object.name, 'code': object.code})
		
	return web.json_response({'': ''})
	
async def getColors(request):

	async with request.app['db'].acquire() as conn:
		objects = await conn.execute(colors.select())
		objects = await objects.fetchall()
		return web.json_response({'objects': json.dumps([{'id': obj.id, 'name': obj.name, 'code': obj.code, 'checked': False, 'active': False, 'images': []} for obj in objects])})
		
	return web.json_response({'data': ''})

async def addColors(request):

	data = await request.post()
	name = data.get('name', False)
	code = data.get('code', False)
	
	async with request.app['db'].acquire() as conn:
		try:
			await conn.execute(colors.insert().values(
					name=name,
					code=code,
				)
			)
			return web.json_response({'response': True})
		except psycopg2.IntegrityError:
			return web.json_response({'response': False, "err": "Такое знаечение уже существует!"})
	return web.json_response({'response': False, "err": ""})
	
async def updateColors(request):

	objectID 	= request.match_info['objectID']
	data		= await request.post()
	name		= data.get('name', False)
	code 		= data.get('code', False)
	
	async with request.app['db'].acquire() as conn:
		try:
			await conn.execute(colors.update().values(
				name=name,
				code=code,
			).where(colors.c.id == objectID))
			return web.json_response({'response': True})
		except psycopg2.IntegrityError:
			return web.json_response({'response': False, "err": "Такое знаечение уже существует!"})
	return web.json_response({'response': False, "err": "Такое знаечение уже существует!"})


async def deleteColors(request):

	data = await request.post()
	async with request.app['db'].acquire() as conn:
		for _, v in data.items():
			await conn.execute(colors.delete().where(colors.c.id == v))
		objects = await conn.execute(colors.select())
		objects = await objects.fetchall()
		return web.json_response({'objects': json.dumps([{'id': obj.id, 'name': obj.name, 'checked': False} for obj in objects])})
		
	return web.json_response({'delete': False})
