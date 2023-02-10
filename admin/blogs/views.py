#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json, random
from aiohttp_session import get_session
from aiohttp import web

from es.db import blogs
from api.api import ya_translate

async def deleteBlogs(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	data = await request.post()
	async with request.app['db'].acquire() as conn:
	
		for _, v in data.items():
		
			object = await conn.execute(blogs.select().where(blogs.c.id == v))
			object = await object.fetchone()
			
			await conn.execute(blogs.delete().where(blogs.c.id == v))
			
			
		return web.json_response({'delete': True})

	return web.json_response({'delete': False})

async def addBlogs(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})

	data 			= await request.post()
	
	name			= data.get('name', False)
	content			= data.get('content', False)
	pre_content		= data.get('pre_content', False)
	poster			= data.get('poster', False)
	slug			= data.get('slug', False)
	seo_title		= data.get('seo_title', False)
	seo_desc		= data.get('seo_desc', False)
	
	async with request.app['db'].acquire() as conn:
	
		#если короткий адрес не установлен то переводим наименование товара
		if not len(slug):
			slug = ya_translate(name)
				
		objectID = await conn.execute(
			blogs.insert().values(
				name		= name,
				content		= content,
				pre_content = pre_content,
				poster		= poster,
				slug 		= slug,
				seo_title 	= seo_title,
				seo_desc 	= seo_desc,
			).returning(blogs.c.id)
		)
		
		objectID = await objectID.fetchone()
		objectID = objectID[0]
		
	return web.json_response({'response': True, 'id': objectID})

async def getBlogs(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	async with request.app['db'].acquire() as conn:
	
		objects = await conn.execute(blogs.select())
		objects = await objects.fetchall()
		
		return web.json_response({'objects': json.dumps([{'id': obj.id, 'name': obj.name, 'checked': False} for obj in objects])})
		
	return web.json_response({'data': ''})
	
	
async def getBlog(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	id = request.match_info['id']
	async with request.app['db'].acquire() as conn:
		object = await conn.execute(blogs.select().where(blogs.c.id == id))
		object = await object.fetchone()
	
		return web.json_response({
			'name': 		object.name,
			'content': 		object.content,
			'pre_content':	object.pre_content,
			'poster': 		object.poster,
			'slug': 		object.slug,
			'seo_title':	object.seo_title,
			'seo_desc':		object.seo_desc,
		})

	return web.json_response({'': ''})
	
async def updateBlogs(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})

	id 	= request.match_info['id']
	
	data 			= await request.post()
	
	name			= data.get('name', False)
	content			= data.get('content', False)
	pre_content		= data.get('pre_content', False)
	poster			= data.get('poster', False)
	slug			= data.get('slug', False)
	seo_title		= data.get('seo_title', False)
	seo_desc		= data.get('seo_desc', False)
	
	async with request.app['db'].acquire() as conn:
		
		#если короткий адрес не установлен то переводим наименование товара
		if not len(slug):
			slug = ya_translate(name)

		await conn.execute(
			blogs.update().values(
			
				name		= name,
				content		= content,
				pre_content	= pre_content,
				poster		= poster,
				slug 		= slug,
				seo_title 	= seo_title,
				seo_desc 	= seo_desc,
				
			).where(blogs.c.id == id)
		)
		
		return web.json_response({'response': True})
		
	return web.json_response({'response': False})
