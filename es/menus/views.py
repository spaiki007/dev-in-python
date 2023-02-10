#!/usr/bin/env python
# -*- coding: utf-8 -*-

from aiohttp import web

from es.db import menus, pages, categories


def sortMenu(parent, temp, objects):
	for object in objects:
		if object.parent == parent:
			temp.append(object)
			sortMenu(object.id, temp, objects)


async def getMenus(request):

	async with request.app['db'].acquire() as conn:
	
		menu = []

		#выбираем категории
		objects = await conn.execute(categories.select().where(categories.c.parent == 0))
		objects = await objects.fetchall()
		menu.append({
			'id': 999999,
			'name': 'каталог',
			'data': [{'id': o.id, 'name': o.name, 'link': '/shop/categories/' + o.slug, 'svg': o.svg} for o in objects],
			'active': False,
		})
		
		
		#собираем статичное меню
		page_objects = await conn.execute(pages.select())
		page_objects = await page_objects.fetchall()

		objects = await conn.execute(menus.select().order_by(menus.c.order))
		objects = await objects.fetchall()

		for object in objects:
			if object.parent == 0:
			
				menu.append({
					'id': object.id,
					'name': object.name,
					'data': [{'id': o.id, 'name': o.name, 'link': '/pages/' + page.slug} for o in objects if o.parent == object.id for page in page_objects if o.pid == page.id],
					'active': False,
				})

		
		return web.json_response(menu)
		
	return web.json_response({'data': ''})
