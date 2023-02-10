#!/usr/bin/env python
# -*- coding: utf-8 -*-

from aiohttp import web
import aiohttp_jinja2

@aiohttp_jinja2.template('pages.html')
async def pagesViews(request):
	context = {}
	return context

	