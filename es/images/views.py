#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random, json, os
from aiohttp import web
from sqlalchemy.sql import and_

from es.db import product_images


async def getImages(request):

	cid = request.query.get('cid', False)
	if cid:
		async with request.app['db'].acquire() as conn:
			objects = await conn.execute(product_images.select().where(product_images.c.cid == cid))
			objects = await objects.fetchall()
			
			return web.json_response({'objects': json.dumps([{'id': obj.id, 'path': obj.name} for obj in objects])})
		
	return web.json_response({'data': ''})



	