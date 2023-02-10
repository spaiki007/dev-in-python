#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json, psycopg2
from aiohttp import web
from aiohttp_session import get_session

from es.db import categories
from api.api import ya_translate

async def deleteCategories(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	data = await request.post()
	async with request.app['db'].acquire() as conn:
	
		for _, v in data.items():

			#достаем категорию
			object = await conn.execute(categories.select().where(categories.c.id == v))
			object = await object.fetchone()
			
			#удаляем категорию
			await conn.execute(categories.delete().where(categories.c.id == object.id))

		objects = await conn.execute(categories.select())
		objects = await objects.fetchall()

		return web.json_response({'objects': json.dumps([{'id': obj.id, 'name': obj.name, 'checked': False} for obj in objects])})

	return web.json_response({'delete': False})

def sortMenu(parent, temp, objects):
	for obj in objects:
		if obj.parent == parent:
			temp.append(obj)
			sortMenu(obj.id, temp, objects)
	
async def getCategories(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	async with request.app['db'].acquire() as conn:
		objects = await conn.execute(categories.select())
		objects = await objects.fetchall()
		
		temp = []
		for obj in objects:
			if obj.parent == 0:
				temp.append(obj)
				sortMenu(obj.id, temp, objects)
		
		list = []
		for obj in temp:
			if obj.parent:
				list.append({'id': obj.id, 'name': obj.name, 'level': 1, 'parent': obj.parent, 'checked': False})
			else:
				list.append({'id': obj.id, 'name': obj.name, 'level': 0, 'parent': obj.parent, 'checked': False})
		
		return web.json_response({'objects': json.dumps(list)})
		
	return web.json_response({'data': ''})
	
	
async def addCategories(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	data		= await request.post()
	
	name 		= data.get('name', False)
	svg 		= data.get('svg', False)
	content 	= data.get('content', False)
	slug 		= data.get('slug', False)
	seo_title 	= data.get('seo_title', False)
	seo_desc 	= data.get('seo_desc', False)
	stocksID 	= data.get('stocksID', False)
	parent		= data.get('parent', False)
	order		= data.get('order', False)
	
	if slug and len(slug):
		slug = ya_translate(slug)
	else:
		slug = ya_translate(name)
	
	async with request.app['db'].acquire() as conn:
		try:
			await conn.execute(categories.insert().values(
				name		= name,
				svg			= svg,
				content		= content,
				slug		= slug,
				seo_title	= seo_title,
				seo_desc	= seo_desc,
				stocks_id	= stocksID,
				parent		= parent,
				order		= order,
			))
			
			return web.json_response({'response': True})
			
		except psycopg2.IntegrityError:
			return web.json_response({'response': False, "err": "Такое значение уже существует, Короткий адресс!"})

	return web.json_response({'response': False, "err": ""})

async def getCategory(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	id = request.match_info['id']
	async with request.app['db'].acquire() as conn:
		object = await conn.execute(categories.select().where(categories.c.id == id))
		object = await object.fetchone()
		
		return web.json_response({
			'id': 			object.id,
			'name': 		object.name,
			'svg':			object.svg,
			'content': 		object.content,
			'slug': 		object.slug,
			'seo_title': 	object.seo_title,
			'seo_desc': 	object.seo_desc,
			'stocksID': 	object.stocks_id,
			'parent':		object.parent,
			'order':		object.order,
		})

	return web.json_response({'': ''})
	
async def updateCategories(request):

	if not request.app['debug']:
	
		session = await get_session(request)
		auth = session.get('auth', False)
		if not auth:
			return web.json_response({'': ''})
		
	id 	= request.match_info['id']
	data 		= await request.post()
	
	name 		= data.get('name', False)
	svg 		= data.get('svg', False)
	content 	= data.get('content', False)
	slug 		= data.get('slug', False)
	seo_title 	= data.get('seo_title', False)
	seo_desc 	= data.get('seo_desc', False)
	parent 		= data.get('parent', False)
	order		= data.get('order', False)
	
	if slug and len(slug):
		slug = ya_translate(slug)
	else:
		slug = ya_translate(name)
	
	async with request.app['db'].acquire() as conn:
		try:
		
			await conn.execute(categories.update().values(
				name		= name,
				svg			= svg,
				content		= content,
				slug		= slug,
				seo_title	= seo_title,
				seo_desc	= seo_desc,
				parent		= parent,
				order		= order,
			).where(categories.c.id == id))
			
			return web.json_response({'response': True})
		except psycopg2.IntegrityError:
			return web.json_response({'response': False, "err": "Такое значение уже существует, Короткий адресс!"})
			
	return web.json_response({'response': False, "err": "Такое значение уже существует, Короткий адресс!"})
