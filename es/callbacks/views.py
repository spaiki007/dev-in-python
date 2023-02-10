#!/usr/bin/env python
# -*- coding: utf-8 -*-

from aiohttp import web
import aiohttp_jinja2, json

from es.db import callbacks


async def createdCallback(request):
	
	data 		= await request.post()
	
	name 		= data.get('name', False)
	phone 		= data.get('phone', False)
	call_time 	= data.get('call_time', False)
	
	if name and phone:
		if len(name) > 0 and len(phone) > 0:
			
			async with request.app['db'].acquire() as conn:
				await conn.execute(callbacks.insert().values(
					name		= name,
					phone		= phone,
					call_time	= call_time,
				))
				
				return web.json_response({'response': json.dumps(True)})
		
	return web.json_response({'response': json.dumps(False)})
	