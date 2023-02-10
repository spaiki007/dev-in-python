#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json, psycopg2
from aiohttp import web
from es.db import manufacturers

async def getManufacturer(request):
	
	id = request.match_info['id']
	async with request.app['db'].acquire() as conn:
		object = await conn.execute(manufacturers.select().where(manufacturers.c.id == id))
		object = await object.fetchone()
		return web.json_response({'name': object.name})
		
	return web.json_response({'': ''})
	
async def getManufacturers(request):

	async with request.app['db'].acquire() as conn:
		objects = await conn.execute(manufacturers.select())
		objects = await objects.fetchall()
		return web.json_response({'objects': json.dumps([{'id': obj.id, 'name': obj.name, 'checked': False} for obj in objects])})
		
	return web.json_response({'data': ''})

async def addManufacturers(request):

	data = await request.post()
	name = data.get('name', False)
	
	async with request.app['db'].acquire() as conn:
		try:
			await conn.execute(manufacturers.insert().values(name=name))
			return web.json_response({'response': True})
		except psycopg2.IntegrityError:
			return web.json_response({'response': False, "err": "Такое знаечение уже существует!"})
	return web.json_response({'response': False, "err": ""})
	
async def updateManufacturers(request):

	id		= request.match_info['id']
	data	= await request.post()
	name	= data.get('name', False)
	
	async with request.app['db'].acquire() as conn:
		try:
			await conn.execute(manufacturers.update().values(name=name).where(manufacturers.c.id == id))
			return web.json_response({'response': True})
		except psycopg2.IntegrityError:
			return web.json_response({'response': False, "err": "Такое знаечение уже существует!"})
	return web.json_response({'response': False, "err": "Такое знаечение уже существует!"})


async def deleteManufacturers(request):

	data = await request.post()
	async with request.app['db'].acquire() as conn:
		for _, v in data.items():
			await conn.execute(manufacturers.delete().where(manufacturers.c.id == v))
		objects = await conn.execute(manufacturers.select())
		objects = await objects.fetchall()
		return web.json_response({'objects': json.dumps([{'id': obj.id, 'name': obj.name, 'checked': False} for obj in objects])})
		
	return web.json_response({'delete': False})
