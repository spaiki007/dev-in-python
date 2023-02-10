#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json, psycopg2
from aiohttp import web
from aiohttp_session import get_session

from es.db import menus


def sortMenu(parent, temp, objects):
	for object in objects:
		if object.parent == parent:
			temp.append(object)
			sortMenu(object.id, temp, objects)

def setLevel(level, parent, objects):

	if parent:
		level += 1
		for object in objects:
			if parent == object.id:
				if object.parent:
					level = setLevel(level, object.parent, objects)
				else:
					break

	return level


async def getMenus(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
		
	async with request.app['db'].acquire() as conn:
	
		objects = await conn.execute(menus.select().order_by(menus.c.order))
		objects = await objects.fetchall()
		
		temp = []
		for object in objects:
			if object.parent == 0:
				temp.append(object)
				sortMenu(object.id, temp, objects)
				
		return web.json_response({'objects': [{'id': obj.id, 'name': obj.name, 'level': obj.level, 'pid': obj.pid, 'checked': False} for obj in temp]})
		
	return web.json_response({'data': ''})
	
	
async def addMenus(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	data 	= await request.post()
	
	parent 	= int(data.get('parent', False))
	name 	= data.get('name', False)
	icon 	= data.get('icon', False)
	order 	= data.get('order', False)
	pid 	= data.get('pid', False)

	async with request.app['db'].acquire() as conn:
	
		objects = await conn.execute(menus.select())
		objects = await objects.fetchall()
		level 	= setLevel(0, parent, objects)
		
		try:
		
			await conn.execute(menus.insert().values(
				parent	= parent,
				pid		= pid,
				name	= name,
				icon	= icon,
				level	= level,
				order	= order,
			))
			
			return web.json_response({'response': True})
			
		except psycopg2.IntegrityError:
			return web.json_response({'response': False, "err": "Такое значение уже существует, Короткий адресс!"})

	return web.json_response({'response': False, "err": ""})

async def getMenu(request):

	if not request.app['debug']:
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
			
	id = request.match_info['id']
	async with request.app['db'].acquire() as conn:
		object = await conn.execute(menus.select().where(menus.c.id == id))
		object = await object.fetchone()
		
		return web.json_response({
			'id': 		object.id,
			'parent': 	object.parent,
			'pid':		object.pid,
			'name': 	object.name, 
			'icon': 	object.icon,
			'order': 	object.order,
		})

	return web.json_response({'': ''})
	
async def updateMenus(request):

	if not request.app['debug']:
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	id 		= request.match_info['id']
	data 	= await request.post()
	
	parent 	= int(data.get('parent', False))
	name 	= data.get('name', False)
	icon 	= data.get('icon', False)
	order 	= data.get('order', False)
	pid 	= data.get('pid', False)

	async with request.app['db'].acquire() as conn:
	
		objects = await conn.execute(menus.select())
		objects = await objects.fetchall()
		level 	= setLevel(0, parent, objects)
		
		await conn.execute(menus.update().values(
		
			parent	= parent,
			pid		= pid,
			name	= name,
			icon	= icon,
			level	= level,
			order	= order,
			
		).where(menus.c.id == id))
		return web.json_response({'response': True})

			
	return web.json_response({'response': False, "err": "Такое значение уже существует, Короткий адресс!"})


async def deleteMenus(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	data = await request.post()
	async with request.app['db'].acquire() as conn:
	
		for _, v in data.items():
			await conn.execute(menus.delete().where(menus.c.id == v))
			
		objects = await conn.execute(menus.select())
		objects = await objects.fetchall()

		return web.json_response({'objects': json.dumps([{'id': obj.id, 'name': obj.name, 'checked': False} for obj in objects])})

	return web.json_response({'delete': False})
