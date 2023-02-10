#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json, psycopg2
from aiohttp import web
from aiohttp_session import get_session
from es.db import roles

async def getRole(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	id = request.match_info['id']
	async with request.app['db'].acquire() as conn:
		object = await conn.execute(roles.select().where(roles.c.id == id))
		object = await object.fetchone()
		return web.json_response({'name': object.name})
		
	return web.json_response({'': ''})
	
async def getRoles(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	async with request.app['db'].acquire() as conn:
		objects = await conn.execute(roles.select())
		objects = await objects.fetchall()
		return web.json_response({'objects': json.dumps([{'id': obj.id, 'name': obj.name, 'checked': False} for obj in objects])})
		
	return web.json_response({'data': ''})

async def addRoles(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	data = await request.post()
	name = data.get('name', False)
	
	async with request.app['db'].acquire() as conn:
		try:
			await conn.execute(roles.insert().values(name=name))
			return web.json_response({'response': True})
		except psycopg2.IntegrityError:
			return web.json_response({'response': False, "err": "Такое знаечение уже существует!"})
	return web.json_response({'response': False, "err": ""})
	
async def updateRoles(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	id		= request.match_info['id']
	data	= await request.post()
	name	= data.get('name', False)
	
	async with request.app['db'].acquire() as conn:
		try:
			await conn.execute(roles.update().values(name=name).where(roles.c.id == id))
			return web.json_response({'response': True})
		except psycopg2.IntegrityError:
			return web.json_response({'response': False, "err": "Такое знаечение уже существует!"})
	return web.json_response({'response': False, "err": "Такое знаечение уже существует!"})


async def deleteRoles(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	data = await request.post()
	async with request.app['db'].acquire() as conn:
		for _, v in data.items():
			await conn.execute(roles.delete().where(roles.c.id == v))
		objects = await conn.execute(roles.select())
		objects = await objects.fetchall()
		return web.json_response({'objects': json.dumps([{'id': obj.id, 'name': obj.name, 'checked': False} for obj in objects])})
		
	return web.json_response({'delete': False})
