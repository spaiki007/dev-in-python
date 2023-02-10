#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json, psycopg2
from aiohttp import web
from aiohttp_session import get_session
from es.db import manufacturers
from api.api import ya_translate


async def getManufacturer(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	id = request.match_info['id']
	async with request.app['db'].acquire() as conn:
		object = await conn.execute(manufacturers.select().where(manufacturers.c.id == id))
		object = await object.fetchone()
		return web.json_response({
			'id': object.id,
			'name': object.name,
			'content': object.content,
			'slug': object.slug,
			'seo_title': object.seo_title,
			'seo_desc': object.seo_desc,
		})
		
	return web.json_response({'': ''})
	
async def getManufacturers(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	async with request.app['db'].acquire() as conn:
		objects = await conn.execute(manufacturers.select())
		objects = await objects.fetchall()
		return web.json_response({'objects': json.dumps([{'id': obj.id, 'name': obj.name, 'checked': False} for obj in objects])})
		
	return web.json_response({'data': ''})

async def addManufacturers(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	data 		= await request.post()
	
	name 		= data.get('name', False)	
	content 	= data.get('content', False)
	slug 		= data.get('slug', False)
	seo_title 	= data.get('seo_title', False)
	seo_desc 	= data.get('seo_desc', False)
	
	if slug and len(slug):
		slug = ya_translate(slug)
	else:
		slug = ya_translate(name)
		
	async with request.app['db'].acquire() as conn:
		try:
			await conn.execute(manufacturers.insert().values(
				name		= name,
				content		= content,
				slug		= slug,
				seo_title	= seo_title,
				seo_desc	= seo_desc,
			))
			return web.json_response({'response': True})
		except psycopg2.IntegrityError:
			return web.json_response({'response': False, "err": "Такое знаечение уже существует!"})
	return web.json_response({'response': False, "err": ""})
	
async def updateManufacturers(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	id		= request.match_info['id']
	data	= await request.post()
	
	name		= data.get('name', False)
	content 	= data.get('content', False)
	slug 		= data.get('slug', False)
	seo_title 	= data.get('seo_title', False)
	seo_desc 	= data.get('seo_desc', False)
	
	if slug and len(slug):
		slug = ya_translate(slug)
	else:
		slug = ya_translate(name)
		
	async with request.app['db'].acquire() as conn:
		try:
			await conn.execute(manufacturers.update().values(
				name		= name,
				content		= content,
				slug		= slug,
				seo_title	= seo_title,
				seo_desc	= seo_desc,
			).where(manufacturers.c.id == id))
			return web.json_response({'response': True})
		except psycopg2.IntegrityError:
			return web.json_response({'response': False, "err": "Такое знаечение уже существует!"})
	return web.json_response({'response': False, "err": "Такое знаечение уже существует!"})


async def deleteManufacturers(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	data = await request.post()
	async with request.app['db'].acquire() as conn:
		for _, v in data.items():
			await conn.execute(manufacturers.delete().where(manufacturers.c.id == v))
		objects = await conn.execute(manufacturers.select())
		objects = await objects.fetchall()
		return web.json_response({'objects': json.dumps([{'id': obj.id, 'name': obj.name, 'checked': False} for obj in objects])})
		
	return web.json_response({'delete': False})
