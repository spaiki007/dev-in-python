#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

class Settings:

	def __init__(self, db_host=False, db_port=False, db=False, db_user=False, db_pass=False, s_name=False, s_port=False):
	
		#db settings
		self.db_host= db_host
		self.db_port= db_port
		self.db		= db
		self.db_user= db_user
		self.db_pass= db_pass
		
		#server settings
		self.s_name = s_name
		self.s_port	= s_port

	def settings_up(self):
		return {
			#db
			'db_host': self.db_host,
			'db_port': self.db_port,
			'db'	 : self.db,
			'db_user': self.db_user,
			'db_pass': self.db_pass,
			'db_minsize':  1,
			'db_maxsize':  50,
			
			#server
			's_name': self.s_name,
			's_port': self.s_port
		}
	
if os.name == 'nt':
	#локалка localhost
	#settings = Settings(db_host='81.177.6.145', db_port=5432, db='shopconsoles_v2', db_user='postgres', db_pass='burda4488@', s_name='localhost', s_port='80')
	
	#бд для разработки
	settings = Settings(db_host='localhost', db_port=5432, db='es', db_user='postgres', db_pass='123', s_name='0.0.0.0', s_port='80')
	
else:
	#сервер
	settings = Settings(db_host='localhost', db_port=5432, db='test', db_user='postgres', db_pass='123', s_name='0.0.0.0', s_port='80')
	
	
settings = settings.settings_up()







