#!/usr/bin/env python
# -*- coding: utf-8 -*-

from aiohttp import web
import aiohttp_jinja2, math

from es.db import blogs


@aiohttp_jinja2.template('detail-blog.html')
async def detailBlogViews(request):

	slug = request.match_info.get('slug', False)
	if not slug:
		raise web.HTTPNotFound()
	
	async with request.app['db'].acquire() as conn:
		context = {}
		
		object = await conn.execute(blogs.select().where(blogs.c.slug == slug))
		object = await object.fetchone()
		
		if object is None:
			raise web.HTTPNotFound()
			
		context['object'] = object

	return context


@aiohttp_jinja2.template('blogs.html')
async def blogsViews(request):

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
		
		objects = await conn.execute("""SELECT * FROM blogs""" + order)
		objects = await objects.fetchall()
		
		count = len(objects)

		allPages = math.ceil(count / 12)
		
		if page < 1 or page > allPages:
			raise web.HTTPNotFound()
			
		context['paginations'] = {'allPages': allPages, 'active': page}
		
		context['blogs'] = objects[((page * 12) - 12):(((page * 12) - 12)+12)]
		
	return context

	