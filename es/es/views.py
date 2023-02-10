#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json, psycopg2, aiohttp_jinja2
from aiohttp import web

from es.db import main_slider
from es.db import categories

async def getMainJson(request):

	context = {}
	
	async with request.app['db'].acquire() as conn:
	
		category = await conn.execute(categories.select().where(categories.c.parent == 0).order_by(categories.c.order))
		category = await category.fetchall()
		context['categories'] = [(dict(row.items())) for row in category]
		
		main_sliders = await conn.execute(main_slider.select())
		main_sliders = await main_sliders.fetchall()
		context['sliders'] = [(dict(row.items())) for row in main_sliders]
	
		

	return web.json_response(context)



@aiohttp_jinja2.template('index.html')
async def index(request):
	context = {}
	return context