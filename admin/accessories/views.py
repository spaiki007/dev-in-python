#!/usr/bin/env python
# -*- coding: utf-8 -*-

from aiohttp import web
from aiohttp_session import get_session
import json
from es.db import accessories


async def deleteAccessories(request):
	
	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
	
	id = request.match_info['id']
	async with request.app['db'].acquire() as conn:
		await conn.execute(accessories.delete().where(accessories.c.id == id))
		return web.json_response({'objects': True})
	

async def addAccessories(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	data 	= await request.post()
	
	parent	= data.get('parent', False)
	pid		= data.get('pid', False)
	
	async with request.app['db'].acquire() as conn:
		await conn.execute(accessories.insert().values(
			parent	= parent,
			pid		= pid,
		)
	)
	return web.json_response({'response': True})

async def getAccessories(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
			
	id = request.match_info['id']
	async with request.app['db'].acquire() as conn:
		objects = await conn.execute(accessories.select().where(accessories.c.parent == id))
		objects = await objects.fetchall()
		return web.json_response({'objects': json.dumps([{'id': obj.id, 'pid': obj.pid, 'checked': False} for obj in objects])})
		
	return web.json_response({'data': ''})
	