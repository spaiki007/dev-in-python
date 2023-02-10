#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json, psycopg2
from aiohttp import web
from aiohttp_session import get_session

from es.db import roles
from es.db import users
from es.db import comments


async def deleteComments(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	data = await request.post()
	async with request.app['db'].acquire() as conn:
		for _, v in data.items():
			await conn.execute(comments.delete().where(comments.c.id == v))
		return web.json_response({'delete': False})

	return web.json_response({'delete': False})

async def getComments(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	async with request.app['db'].acquire() as conn:
	
		objects = await conn.execute("SELECT * FROM comments ORDER BY status, created")
		
		return web.json_response({'objects': json.dumps([{'id': obj.id, 'name': obj.name, 'created': obj.created.strftime("%d.%m.%Y %H:%M:%S"), 'status': obj.status, 'checked': False} for obj in await objects.fetchall()])})
		
	return web.json_response({'data': ''})
	
	
async def addCommentsAdmin(request):
	
	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})

	data	= await request.post()
	name	= data.get('name', False)
	cid		= data.get('cid', False)
	pid		= data.get('pid', False)
	
	async with request.app['db'].acquire() as conn:
	
		role = await conn.execute(roles.select().where(roles.c.name == "admin"))
		role = await role.fetchone()
		
		user = await conn.execute(users.select().where(users.c.role == role.id))
		user = await user.fetchone()

		async with request.app['db'].acquire() as conn:

			await conn.execute(comments.insert().values(
				name		= name,
				status		= True,
				cid			= cid,
				uid			= user.id,
				pid			= pid,
			))
			
			return web.json_response({'response': True})


	return web.json_response({'response': False, "err": ""})
	
async def addComments(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	data		= await request.post()
	
	name 		= data.get('name', False)
	positive 	= data.get('positive', False)
	negative 	= data.get('negative', False)
	rating 		= data.get('rating', False)
	cid 		= data.get('cid', False)
	uid 		= data.get('uid', False)
	pid 		= data.get('pid', False)
	
	async with request.app['db'].acquire() as conn:

		await conn.execute(comments.insert().values(
			name		= name,
			positive	= positive,
			negative	= negative,
			rating		= rating,
			status		= True,
			cid			= cid,
			uid			= uid,
			pid			= pid,
		))
		
		return web.json_response({'response': True})


	return web.json_response({'response': False, "err": ""})

async def getComment(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	id = request.match_info['id']
	async with request.app['db'].acquire() as conn:
		object = await conn.execute(comments.select().where(comments.c.id == id))
		object = await object.fetchone()

		return web.json_response({
			'id': 		object.id,
			'name': 	object.name,
			'positive': object.positive,
			'negative': object.negative,
			'rating': 	object.rating,
			'status':	object.status,
			'cid': 		object.cid,
			'uid': 		object.uid,
			'pid': 		object.pid,
		})

	return web.json_response({'': ''})
	
async def updateComments(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	id 	= request.match_info['id']
	data = await request.post()
	
	name 		= data.get('name', False)
	positive 	= data.get('positive', False)
	negative 	= data.get('negative', False)
	rating 		= data.get('rating', False)
	status 		= data.get('status', False)

	if status == "true":
		status = True
	else:
		status = False
		
	cid 		= data.get('cid', False)
	uid 		= data.get('uid', False)
	pid 		= data.get('pid', False)
	
	async with request.app['db'].acquire() as conn:
		try:
		
			await conn.execute(comments.update().values(
				name		= name,
				positive	= positive,
				negative	= negative,
				rating		= rating,
				status		= status,
				cid			= cid,
				uid			= uid,
				pid			= pid,
			).where(comments.c.id == id))
			
			return web.json_response({'response': True})
		except psycopg2.IntegrityError:
			return web.json_response({'response': False, "err": "Такое значение уже существует, Короткий адресс!"})
			
	return web.json_response({'response': False, "err": "Такое значение уже существует, Короткий адресс!"})
