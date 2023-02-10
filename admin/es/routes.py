#!/usr/bin/env python
# -*- coding: utf-8 -*-

from aiohttp import web

from admin.views import admin, Auth
from api.api import auth_jwt, tinymce_upload


from mainSlider.views import getMainSliders, addMainSlider, getMainSlider, updateMainSlider, deleteMainSlider

from quickOrders.views import getQuickOrders, getQuickOrder, updateQuickOrders, deleteQuickOrders
from callbacks.views import getCallbacks, getCallback, updateCallbacks, deleteCallbacks
from orders.views import getOrders, getOrder, updateOrders, deleteOrders

from roles.views import getRoles, addRoles, getRole, updateRoles, deleteRoles
from users.views import getUsers, addUsers, getUser, updateUsers, deleteUsers
from comments.views import getComments, addComments, addCommentsAdmin, getComment, updateComments, deleteComments

from blogs.views import getBlogs, addBlogs, getBlog, updateBlogs, deleteBlogs
from pages.views import getPages, addPages, getPage, updatePages, deletePages

from menus.views import getMenus, addMenus, getMenu, updateMenus, deleteMenus
from categories.views import getCategories, addCategories, getCategory, updateCategories, deleteCategories

from manufacturers.views import getManufacturers, addManufacturers, getManufacturer, updateManufacturers, deleteManufacturers
from products.views import getProducts, addProducts, getProduct, updateProducts, deleteProducts
from colors.views import getColors, addColors, getColor, updateColors, deleteColors
from images.views import getImages, addImages, deleteImage

from accessories.views import getAccessories, addAccessories, deleteAccessories

from stocks.views import getStocks, addStocks, getStock, updateStocks, deleteStocks
from gifts.views import getGifts, addGifts, getGift, updateGifts, deleteGifts

from pickings.views import getPickings, addPickings, getPicking, updatePickings, deletePickings
from pickings_assoc_products.views import getPaps, addPaps, deletePaps

from options.views import getOptions, addOptions, getOption, updateOptions, deleteOptions
from options_assoc_products.views import getOaps, addOaps, deleteOaps

from characteristics.views import getCharacteristics, addCharacteristics, getCharacteristic, updateCharacteristics, deleteCharacteristics
from cvalue.views import getCvalues, addCvalues, getCvalue, updateCvalues, deleteCvalues
from cvalues_assoc_products.views import getCaps, addCaps, deleteCaps


def setup_routes(app):

	app.add_routes([
		
		web.view('/auth', Auth),
		web.get('/', admin),
		
		web.post('/jwt', auth_jwt),
		web.post('/tinymce/upload', tinymce_upload),

		#mainSlider
		web.get('/main-sliders/get', getMainSliders),
		web.get('/main-sliders/{id:[0-9]+}', getMainSlider),
		web.post('/main-sliders/add', addMainSlider),
		web.post('/main-sliders/{id:[0-9]+}/update',  updateMainSlider),
		web.post('/main-sliders/delete', deleteMainSlider),


		#quickOrders
		web.get('/quick-orders/get', getQuickOrders),
		web.get('/quick-orders/{id:[0-9]+}', getQuickOrder),
		web.post('/quick-orders/{id:[0-9]+}/update', updateQuickOrders),
		web.post('/quick-orders/delete', deleteQuickOrders),
		
		#callbacks
		web.get('/callbacks/get', getCallbacks),
		web.get('/callbacks/{id:[0-9]+}', getCallback),
		web.post('/callbacks/{id:[0-9]+}/update', updateCallbacks),
		web.post('/callbacks/delete', deleteCallbacks),
		
		#orders
		web.get('/orders/get', getOrders),
		web.get('/orders/{id:[0-9]+}', getOrder),
		web.post('/orders/{id:[0-9]+}/update', updateOrders),
		web.post('/orders/delete', deleteOrders),
		
		#roles
		web.get('/roles/get', getRoles),
		web.get('/roles/{id:[0-9]+}', getRole),
		web.post('/roles/add', addRoles),
		web.post('/roles/{id:[0-9]+}/update', updateRoles),
		web.post('/roles/delete', deleteRoles),
		
		#users
		web.get('/users/get', getUsers),
		web.get('/users/{id:[0-9]+}', getUser),
		web.post('/users/add', addUsers),
		web.post('/users/{id:[0-9]+}/update', updateUsers),
		web.post('/users/delete', deleteUsers),
		
		#comments
		web.get('/comments/get', getComments),
		web.get('/comments/{id:[0-9]+}', getComment),
		web.post('/comments/add', addComments),
		web.post('/comments/custom/add', addCommentsAdmin),
		
		web.post('/comments/{id:[0-9]+}/update', updateComments),
		web.post('/comments/delete', deleteComments),

		#blogs
		web.get('/blogs/get', getBlogs),
		web.get('/blogs/{id:[0-9]+}', getBlog),
		web.post('/blogs/add', addBlogs),
		web.post('/blogs/{id:[0-9]+}/update',  updateBlogs),
		web.post('/blogs/delete', deleteBlogs),
	
		#pages
		web.get('/pages/get', getPages),
		web.get('/pages/{id:[0-9]+}', getPage),
		web.post('/pages/add', addPages),
		web.post('/pages/{id:[0-9]+}/update',  updatePages),
		web.post('/pages/delete', deletePages),

		#menus
		web.get('/menus/get', getMenus),
		web.get('/menus/{id:[0-9]+}', getMenu),
		web.post('/menus/add', addMenus),
		web.post('/menus/{id:[0-9]+}/update',  updateMenus),
		web.post('/menus/delete', deleteMenus),

		#сategories
		web.get('/categories/get', getCategories),
		web.get('/category/{id:[0-9]+}', getCategory),
		web.post('/categories/add', addCategories),
		web.post('/categories/{id:[0-9]+}/update',  updateCategories),
		web.post('/categories/delete', deleteCategories),
		
		#manufacturers
		web.get('/manufacturers/get', getManufacturers),
		web.get('/manufacturers/{id:[0-9]+}', getManufacturer),
		web.post('/manufacturers/add', addManufacturers),
		web.post('/manufacturers/{id:[0-9]+}/update', updateManufacturers),
		web.post('/manufacturers/delete', deleteManufacturers),
		
		#products
		web.get('/products/get', getProducts),
		web.get('/products/{id:[0-9]+}', getProduct),
		web.post('/products/add', addProducts),
		web.post('/products/{id:[0-9]+}/update',  updateProducts),
		web.post('/products/delete', deleteProducts),
		
		#colors
		web.get('/colors/get/{id:[0-9]+}', getColors),
		web.get('/colors/{id:[0-9]+}', getColor),
		web.post('/colors/add', addColors),
		web.post('/colors/{id:[0-9]+}/update',  updateColors),
		web.post('/colors/delete/{id:[0-9]+}', deleteColors),
		
		#images
		web.get('/images/{id:[0-9]+}', getImages),
		web.post('/images/add', addImages),
		web.post('/images/delete/{id:[0-9]+}', deleteImage),
		
		#Accessories
		web.get('/accessories/{id:[0-9]+}', getAccessories),
		web.post('/accessories/add', addAccessories),
		web.post('/accessories/{id:[0-9]+}/delete', deleteAccessories),

		#stocks
		web.get('/stocks/get', getStocks),
		web.get('/stocks/{id:[0-9]+}', getStock),
		web.post('/stocks/add', addStocks),
		web.post('/stocks/{id:[0-9]+}/update',  updateStocks),
		web.post('/stocks/delete', deleteStocks),
		
		#gifts
		web.get('/gifts/get', getGifts),
		web.get('/gifts/{id:[0-9]+}', getGift),
		web.post('/gifts/add', addGifts),
		web.post('/gifts/{id:[0-9]+}/update',  updateGifts),
		web.post('/gifts/delete', deleteGifts),
		
		#pickings
		web.get('/pickings/get', getPickings),
		web.get('/pickings/{id:[0-9]+}', getPicking),
		web.post('/pickings/add', addPickings),
		web.post('/pickings/{id:[0-9]+}/update',  updatePickings),
		web.post('/pickings/delete', deletePickings),
		
		#pickings assoc products
		web.get('/paps/{id:[0-9]+}', getPaps),
		web.post('/paps/add', addPaps),
		web.post('/paps/{id:[0-9]+}/delete', deletePaps),
		
		#options
		web.get('/options/get', getOptions),
		web.get('/options/{id:[0-9]+}', getOption),
		web.post('/options/add', addOptions),
		web.post('/options/{id:[0-9]+}/update',  updateOptions),
		web.post('/options/delete', deleteOptions),
		
		#options assoc products
		web.get('/oaps/{id:[0-9]+}', getOaps),
		web.post('/oaps/add', addOaps),
		web.post('/oaps/{id:[0-9]+}/delete', deleteOaps),
		
		#сharacteristics
		web.get('/characteristics/get', getCharacteristics),
		web.get('/characteristics/{id:[0-9]+}', getCharacteristic),
		web.post('/characteristics/add', addCharacteristics),
		web.post('/characteristics/{id:[0-9]+}/update',  updateCharacteristics),
		web.post('/characteristics/delete', deleteCharacteristics),
		
		#cvalues
		web.get('/cvalues/get', getCvalues),
		web.get('/cvalues/{id:[0-9]+}', getCvalue),
		web.post('/cvalues/add', addCvalues),
		web.post('/cvalues/{id:[0-9]+}/update',  updateCvalues),
		web.post('/cvalues/delete', deleteCvalues),
		
		#cvalues assoc products
		web.get('/caps/{id:[0-9]+}', getCaps),
		web.post('/caps/add', addCaps),
		web.post('/caps/{id:[0-9]+}/delete', deleteCaps),

		
	])