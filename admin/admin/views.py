#!/usr/bin/env python
# -*- coding: utf-8 -*-

from aiohttp import web
import aiohttp_jinja2
from aiohttp_session import get_session

from sqlalchemy.sql import and_

from es.db import users


@aiohttp_jinja2.template('index.html')
async def admin(request):

	session = await get_session(request)
	auth = session.get('auth', False)
	
	if auth == True:
		return
	raise web.HTTPFound('/auth')


@aiohttp_jinja2.template('auth.html')
class Auth(web.View):
	
	#чекаем юзера
	async def check_auth(self, request, name, passw):
		async with request.app['db'].acquire() as conn:

			user = await conn.execute(
				users.select().where(
					and_(
						users.c.login == name,
						users.c.passw == passw,
					)
				)
			)
			user = await user.fetchone()
			if user is not None:
				return user
			else:
				return False

	async def get_resp(self, request):
		return {}
		
	async def post_resp(self, request):
		
		session = await get_session(request)
		data 	= await request.post()
		
		login 	= data['login']
		password= data['password']
		
		user = await self.check_auth(request, login, password)
		if user:
			session['auth'] = True
			raise web.HTTPFound('/')

		raise web.HTTPFound('/auth')
		
	async def get(self):
		return await self.get_resp(self.request)

	async def post(self):
		return await self.post_resp(self.request)