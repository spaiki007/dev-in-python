#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math, json, aiohttp_jinja2, random
from aiohttp_session import get_session
from aiohttp import web

from es.db import roles
from es.db import users
from es.db import comments


async def addMainComments(request):
	
	data 			= await request.post()

	user_name 		= data.get('user_name', False)
	user_city 		= data.get('user_city', False)
	rating 			= data.get('rating', False)
	user_positive 	= data.get('user_positive', False)
	user_negative 	= data.get('user_negative', False)
	user_comment 	= data.get('user_comment', False)

	if not(user_name and user_city and rating and user_comment):
		return web.json_response(json.dumps({'response': False, 'err': 'Заполните все поля помеченные *.'}))
	
	if len(user_name) < 0 or len(user_name) > 255:
		return web.json_response(json.dumps({'response': False, 'err': 'Поле имя не может быть менее 0 и не должно превышать 255 символов.'}))
	
	if len(user_city) < 0 or len(user_city) > 255:
		return web.json_response(json.dumps({'response': False, 'err': 'Поле город не может быть менее 0 и не должно превышать 255 символов.'}))
		
	if int(rating) < 0 or int(rating) > 5:
		return web.json_response(json.dumps({'response': False, 'err': 'Рейтинг не может быть менее 0 и более 5.'}))
		
	if len(user_positive) < 0 or len(user_positive) > 250:
		return web.json_response(json.dumps({'response': False, 'err': 'Поле плюсы не должно превышать 250 символов.'}))
		
	if len(user_negative) < 0 or len(user_negative) > 250:
		return web.json_response(json.dumps({'response': False, 'err': 'Поле минусы не должно превышать 250 символов.'}))
	
	if len(user_comment) < 0 or len(user_comment) > 1000:
		return web.json_response(json.dumps({'response': False, 'err': 'Поле комментарий не может быть менее 0 и не должно превышать 1000 символов.'}))
		

	async with request.app['db'].acquire() as conn:
	
		sum = "qwertyuiopasdfghjklzxcvbnm"
		
		#генерируем логин юзера
		user_login = ''.join([random.choice(sum) for _ in range(10)])
		
		#генерируем пароль юзера
		user_pass = ''.join([random.choice(sum) for _ in range(10)])
		
		role = await conn.execute(roles.select().where(roles.c.name == "user"))
		role = await role.fetchone()
		
		userID = await conn.execute(
			users.insert().values(
				role  		= role.id,
				login 		= user_login,
				user_name 	= user_name,
				passw 		= user_pass,
				city 		= user_city,
			).returning(users.c.id)
		)
		userID = await userID.fetchone()
		userID = userID[0]
	
		await conn.execute(comments.insert().values(
			name		= user_comment,
			positive	= user_positive,
			negative	= user_negative,
			rating		= rating,
			uid			= userID,
		))

	return web.json_response(json.dumps({'response': True}))


@aiohttp_jinja2.template('comments.html')
async def commentsViews(request):

	page = request.match_info.get('page', False)
	if not page:
		raise web.HTTPNotFound()
	page = int(page)
	
	async with request.app['db'].acquire() as conn:
	
		context = {}

		order = " ORDER BY created DESC"
		sort = request.query.get('sort', False)
		if sort:
			if sort == "0":
				order = " ORDER BY rating ASC"
			else:
				order = " ORDER BY rating DESC"
			
		context['sort'] = sort
		
		objects = await conn.execute("""
			SELECT r.name AS role_name, u.user_name, u.city, c.* 
			FROM roles r, users u, comments c 
			WHERE c.pid=0 AND u.id=c.uid AND status=true AND u.role=r.id""" + order)
		objects = await objects.fetchall()
		
		countCommnets = len(objects)
		
		context['countCommnets'] = countCommnets

		allPages = math.ceil(countCommnets / 12)
		
		if page < 1 or page > allPages:
			raise web.HTTPNotFound()
			
		context['paginations'] = {'allPages': allPages, 'active': page}
		
		rating = {
			"negative": {"count": 0, "procent": 0},
			"positive": {"count": 0, "procent": 0},
			1: {"count": 0, "procent": 0},
			2: {"count": 0, "procent": 0},
			3: {"count": 0, "procent": 0},
			4: {"count": 0, "procent": 0},
			5: {"count": 0, "procent": 0},
		}

		for object in objects:
			
			if object.role_name == "admin":
				continue
			
			if not object.negative == "":
				rating["negative"]["count"] += 1
				
			if not object.positive == "":
				rating["positive"]["count"] += 1
			
			if object.rating == 1:
				rating[1]["count"] += 1
				
			if object.rating == 2:
				rating[2]["count"] += 1
				
			if object.rating == 3:
				rating[3]["count"] += 1
				
			if object.rating == 4:
				rating[4]["count"] += 1
			
			if object.rating == 5:
				rating[5]["count"] += 1

		if rating["negative"]["count"]:
			rating["negative"]["procent"] = int(100 / (countCommnets / rating["negative"]["count"]))
			
		if rating["positive"]["count"]:
			rating["positive"]["procent"] = int(100 / (countCommnets / rating["positive"]["count"]))
		
		if rating[1]["count"]:
			rating[1]["procent"] = int(100 / (countCommnets / rating[1]["count"]))
			
		if rating[2]["count"]:
			rating[2]["procent"] = int(100 / (countCommnets / rating[2]["count"]))
			
		if rating[3]["count"]:
			rating[3]["procent"] = int(100 / (countCommnets / rating[3]["count"]))
			
		if rating[4]["count"]:
			rating[4]["procent"] = int(100 / (countCommnets / rating[4]["count"]))
			
		if rating[5]["count"]:
			rating[5]["procent"] = int(100 / (countCommnets / rating[5]["count"]))
	
		context['rating'] = rating
		
		context['comments'] = objects[((page * 12) - 12):(((page * 12) - 12)+12)]
	
	return context

	