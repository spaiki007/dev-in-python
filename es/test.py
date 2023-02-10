#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from es.settings import settings

from es.db import menus, pages


DSN = "postgresql://{user}:{password}@{host}:{port}/{database}".format(
	host 		= settings['db_host'],
	port 		= settings['db_port'],
	database 	= settings['db'],
	user 		= settings['db_user'],
	password 	= settings['db_pass']
)

conn = create_engine(DSN)


# def sortMenu(parent, temp, objects):
	# for object in objects:
		# if object.parent == parent:
			# temp.append(object)
			# sortMenu(object.id, temp, objects)
			

page_objects = conn.execute(pages.select())
page_objects = page_objects.fetchall()

objects = conn.execute(menus.select().order_by(menus.c.order))
objects = objects.fetchall()

temp = []
for object in objects:
	if object.parent == 0:
	
		temp.append({
			'id': object.id,
			'name': object.name,
			'data': [{'id': o.id, 'name': o.name, 'link': '/pages/' + page.slug} for o in objects if o.parent == object.id for page in page_objects if o.pid == page.id],
			'active': False,
		})
		
		#sortMenu(object.id, temp, objects)
		
print(temp)