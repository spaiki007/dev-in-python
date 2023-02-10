#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json, os, shutil, random
from aiohttp import web
from aiohttp_session import get_session

from es.db import pages

from api.api import ya_translate


async def deletePages(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	data = await request.post()
	async with request.app['db'].acquire() as conn:
	
		for _, v in data.items():
			await conn.execute(pages.delete().where(pages.c.id == v))
			
		return web.json_response({'delete': True})

	return web.json_response({'delete': False})

async def addPages(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	data 	= await request.post()
	
	name	= data.get('name', False)
	text	= data.get('content', False)
	slug	= data.get('slug', False)
	seo_title = data.get('seo_title', False)
	seo_desc = data.get('seo_desc', False)

	async with request.app['db'].acquire() as conn:
	
		#если короткий адрес не установлен то переводим наименование товара
		if not len(slug):
			slug = ya_translate(name)
		
		await conn.execute(
			pages.insert().values(
			
				name		= name,
				content		= text,
				slug 		= slug,
				seo_title 	= seo_title,
				seo_desc 	= seo_desc,
				
			)
		)
		
	return web.json_response({'response': True})

async def getPages(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	async with request.app['db'].acquire() as conn:
	
		objects = await conn.execute(pages.select())
		objects = await objects.fetchall()
		
		return web.json_response({'objects': json.dumps([{'id': obj.id, 'name': obj.name, 'checked': False} for obj in objects])})
		
	return web.json_response({'data': ''})
	
	
async def getPage(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	id = request.match_info['id']
	async with request.app['db'].acquire() as conn:
		object = await conn.execute(pages.select().where(pages.c.id == id))
		object = await object.fetchone()
	
		return web.json_response({
		
			'name': 		object.name,
			'content': 		object.content, 
			'slug': 		object.slug,
			'seo_title':	object.seo_title,
			'seo_desc':		object.seo_desc,
			
		})

	return web.json_response({'': ''})
	
async def updatePages(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	id = request.match_info['id']
	
	data 	= await request.post()
	
	name	= data.get('name', False)
	text	= data.get('content', False)
	slug	= data.get('slug', False)
	seo_title = data.get('seo_title', False)
	seo_desc = data.get('seo_desc', False)
	
	async with request.app['db'].acquire() as conn:
		
		#если короткий адрес не установлен то переводим наименование товара
		if not len(slug):
			slug = ya_translate(name)

		await conn.execute(
			pages.update().values(
			
				name		= name,
				content		= text,
				slug 		= slug,
				seo_title 	= seo_title,
				seo_desc 	= seo_desc,
				
			).where(pages.c.id == objectID)
		)
		
		return web.json_response({'response': True})
		
	return web.json_response({'response': False})
