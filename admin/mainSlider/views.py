#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from aiohttp_session import get_session
from aiohttp import web

from es.db import main_slider

async def deleteMainSlider(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	data = await request.post()
	async with request.app['db'].acquire() as conn:
	
		for _, v in data.items():
			await conn.execute(main_slider.delete().where(main_slider.c.id == v))


		return web.json_response({'delete': True})

	return web.json_response({'delete': False})

async def addMainSlider(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	data 			= await request.post()
	
	name	= data.get('name', False)
	desc	= data.get('desc', False)
	link	= data.get('link', False)
	price	= data.get('price', False)
	poster	= data.get('poster', False)

	async with request.app['db'].acquire() as conn:
		await conn.execute(main_slider.insert().values(
				name		= name,
				desc		= desc,
				link 		= link,
				price 		= price,
				poster 		= poster,
			)
		)
		
	return web.json_response({'response': True})

async def getMainSliders(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	async with request.app['db'].acquire() as conn:
	
		objects = await conn.execute(main_slider.select())
		objects = await objects.fetchall()
		
		return web.json_response({'objects': json.dumps([{'id': obj.id, 'name': obj.name, 'checked': False} for obj in objects])})
		
	return web.json_response({'data': ''})
	
	
async def getMainSlider(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	id = request.match_info['id']
	async with request.app['db'].acquire() as conn:
	
		object = await conn.execute(main_slider.select().where(main_slider.c.id == id))
		object = await object.fetchone()

		return web.json_response({
		
			'name': 	object.name, 
			'desc': 	object.desc,
			'link': 	object.link,
			'price':	object.price,
			'poster':	object.poster,
			
		})

	return web.json_response({'': ''})
	
async def updateMainSlider(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	id 		= request.match_info['id']
	data 	= await request.post()
	
	name	= data.get('name', False)
	desc	= data.get('desc', False)
	link	= data.get('link', False)
	price	= data.get('price', False)
	poster	= data.get('poster', False)
	
	async with request.app['db'].acquire() as conn:
		await conn.execute(main_slider.update().values(
				name		= name,
				desc		= desc,
				link 		= link,
				price 		= price,
				poster 		= poster,
			).where(main_slider.c.id == id)
		)
		
		return web.json_response({'response': True})
		
	return web.json_response({'response': False})
