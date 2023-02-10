#!/usr/bin/env python
# -*- coding: utf-8 -*-


from aiohttp import web
from es.views import index, getMainJson

from menus.views import getMenus
from categories.views import categoriesViews, getProducts
from product.views import productViews, productSliderGet, similarProducts, addBasket, getBasket, delBasket, addProductsComments

from callbacks.views import createdCallback
from orders.views import order, quickOrder
from comments.views import commentsViews, addMainComments
from blogs.views import blogsViews, detailBlogViews
from pages.views import pagesViews

from images.views import getImages

def setup_routes(app):
	app.add_routes([
		web.get('/', index),
		web.get('/get-main-json', getMainJson),
		
		web.post('/shop/callback', createdCallback),

		web.post('/shop/quick-order', quickOrder),
		
		web.post('/shop/products/order', order),
		web.get('/shop/products/del-basket-products', delBasket),
		web.get('/shop/products/get-basket', getBasket),
		web.post('/shop/products/add-basket', addBasket),
		web.post('/shop/products/add-products-comments', addProductsComments),
		
		web.get('/shop/similar-products', similarProducts),
		web.get('/shop/product-slider-get', productSliderGet),
		web.get('/shop/get-menus', getMenus),
		web.get('/shop/comments/{page:[0-9]+}', commentsViews),
		web.post('/shop/add-main-comments', addMainComments),
		
		web.get('/shop/categories/get-products', getProducts),
		web.get('/shop/categories/{slug:[a-z0-9\-]+}', categoriesViews),
		
		web.get('/shop/products/{slug:[a-z0-9\-]+}', productViews),
		web.get('/shop/images/get', getImages),
		
		web.get('/pages/{slug:[a-z0-9\-]+}', pagesViews),
		web.get('/blog/page/{page:[0-9]+}', blogsViews),
		web.get('/blog/{slug:[a-z0-9\-]+}', detailBlogViews),
		
	])