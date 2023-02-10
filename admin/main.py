#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, ssl, base64, aiohttp_jinja2, jinja2, aiohttp_session, pysftp, aiohttp_cors

from cryptography import fernet
from aiohttp import web
from aiohttp_session.cookie_storage import EncryptedCookieStorage
from aiopg.sa import create_engine

from es.settings import settings
from es.routes import setup_routes
	
async def init_sftp(app):
	pass
	# cnopts = pysftp.CnOpts()
	# cnopts.hostkeys = None
	# sftp = pysftp.Connection('81.177.6.145', username='root', password='JeP{Bq]wmVw5', cnopts=cnopts)
	# app['sftp'] = sftp
	
async def close_sftp(app):
    #app['sftp'].close()
	pass
	
async def init_pg(app):
	settings = app['settings']
	engine = await create_engine(
		database= settings['db'],
		user	= settings['db_user'],
		password= settings['db_pass'],
		host	= settings['db_host'],
		port	= settings['db_port'],
		minsize	= settings['db_minsize'],
		maxsize	= settings['db_maxsize'],
	)
	app['db'] = engine

async def close_pg(app):
    app['db'].close()
    await app['db'].wait_closed()

	
if os.name == 'nt':

	if __name__ == '__main__':

		app = web.Application()

		app['debug'] = True

		fernet_key = fernet.Fernet.generate_key()
		secret_key = base64.urlsafe_b64decode(fernet_key)
		
		aiohttp_session.setup(app, EncryptedCookieStorage(secret_key, cookie_name="session"))

		app['settings'] = settings
		aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('templates'))

		setup_routes(app)
		
		cors = aiohttp_cors.setup(app, defaults={
		"*": aiohttp_cors.ResourceOptions(
				allow_credentials=True,
				expose_headers="*",
				allow_headers="*",
			)
		})
		
		for route in list(app.router.routes()):
		
			try:
				cors.add(route)
			except ValueError:
				pass
				
		app.on_startup.append(init_pg)
		app.on_cleanup.append(close_pg)
		
		app.on_startup.append(init_sftp)
		app.on_cleanup.append(close_sftp)

		app.router.add_static('/static/', path='static', name='static')
		
		web.run_app(app, host=app['settings']['s_name'], port=app['settings']['s_port'])
else:

	async def start():
	
		app = web.Application()
		
		app['debug'] = False
		
		fernet_key = fernet.Fernet.generate_key()
		secret_key = base64.urlsafe_b64decode(fernet_key)
		
		aiohttp_session.setup(app, EncryptedCookieStorage(secret_key, cookie_name="session"))

		app['settings'] = settings
		aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('templates'))

		setup_routes(app)
		
		app.on_startup.append(init_pg)
		app.on_cleanup.append(close_pg)
		
		app.on_startup.append(init_sftp)
		app.on_cleanup.append(close_sftp)

		app.router.add_static('/static/', path='static', name='static')

		return app
		