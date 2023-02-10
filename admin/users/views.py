#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json, psycopg2
from aiohttp_session import get_session
from aiohttp import web
from es.db import users


async def getUsers(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	async with request.app['db'].acquire() as conn:

		objects = await conn.execute(users.select())
		objects = await objects.fetchall()
		objects = json.dumps([{'id': obj.id, 'name': obj.login, 'checked': False} for obj in objects])
		
		return web.json_response({'objects': objects})
		
	return web.json_response({'data': ''})
	
async def getUser(request):
	
	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
	
	id = request.match_info['id']
	async with request.app['db'].acquire() as conn:
		object = await conn.execute(users.select().where(users.c.id == id))
		object = await object.fetchone()
		return web.json_response({'role': object.role, 'login': object.login, 'name': object.user_name, 'passw': object.passw, 'city': object.city})

	return web.json_response({'': ''})
	
async def addUsers(request):
	
	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
	
	data 	= await request.post()
	
	role_id = data.get('role', False)
	login 	= data.get('login', False)
	name 	= data.get('name', False)
	passw 	= data.get('passw', False)
	city 	= data.get('city', False)

	
	async with request.app['db'].acquire() as conn:
	
		try:
			await conn.execute(users.insert().values(
				role  = role_id,
				login = login,
				user_name = name,
				passw = passw,
				city = city,
			))
			return web.json_response({'response': True})
		except psycopg2.IntegrityError:
			return web.json_response({'response': False, "err": "Такое значение уже существует, login!"})

	return web.json_response({'response': False, "err": ""})
	
async def updateUsers(request):
	
	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
	
	id		= request.match_info['id']
	data	= await request.post()
	
	role_id = data.get('role', False)
	login 	= data.get('login', False)
	name 	= data.get('name', False)
	passw 	= data.get('passw', False)
	city 	= data.get('city', False)
	
	async with request.app['db'].acquire() as conn:
		try:
			await conn.execute(users.update().values(
				role  = role_id,
				login = login,
				user_name = name,
				passw = passw,
				city = city,
			).where(users.c.id == id))
			return web.json_response({'response': True})
		except psycopg2.IntegrityError:
			return web.json_response({'response': False, "err": "Такое знаечение уже существует!"})
			
	return web.json_response({'response': False, "err": "Такое знаечение уже существует!"})


async def deleteUsers(request):
	
	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
	
	data = await request.post()
	async with request.app['db'].acquire() as conn:
	
		for _, v in data.items():
			await conn.execute(users.delete().where(users.c.id == v))
			
		objects = await conn.execute(users.select())
		objects = await objects.fetchall()

		return web.json_response({'objects': json.dumps([{'id': obj.id, 'name': obj.login, 'checked': False} for obj in objects])})

	return web.json_response({'delete': False})
