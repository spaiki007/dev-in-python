#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
from sqlalchemy import create_engine
import sqlalchemy as sa

from es.settings import settings


DSN = "postgresql://{user}:{password}@{host}:{port}/{database}".format(
	host 		= settings['db_host'],
	port 		= settings['db_port'],
	database 	= settings['db'],
	user 		= settings['db_user'],
	password 	= settings['db_pass']
)

conn = create_engine(DSN)
meta = sa.MetaData()

#слайдер на главной
main_slider = sa.Table(
	'main_slider', meta,
	
	sa.Column('id', sa.Integer, nullable=False, primary_key=True),

	sa.Column('name', sa.String(255), nullable=False),
	sa.Column('desc', sa.Text, default=""),

	sa.Column('link', sa.String(255)),
	sa.Column('price', sa.Integer, default=0),

	#постер
	sa.Column('poster', sa.String(1000)),
)

#быстрый заказы
quickOrders = sa.Table(
	'quick_orders', meta,
	
	sa.Column('id', sa.Integer, nullable=False, primary_key=True),
	
	sa.Column('name', sa.String(255)),
	sa.Column('phone', sa.String(255)),
	sa.Column('comment', sa.String(1000), nullable=True),
	sa.Column('info', sa.Text),
	
	sa.Column('status', sa.Integer, default=1),
	sa.Column('created', sa.DateTime, default=datetime.datetime.utcnow),
)

#обратные звоноки
callbacks = sa.Table(
	'callbacks', meta,
	
	sa.Column('id', sa.Integer, nullable=False, primary_key=True),
	
	sa.Column('name', sa.String(255)),
	sa.Column('phone', sa.String(255)),
	sa.Column('call_time', sa.String(255)),
	
	sa.Column('status', sa.Integer, default=1),
	sa.Column('created', sa.DateTime, default=datetime.datetime.utcnow),
)

#заказы
orders = sa.Table(
	'orders', meta,
	
	sa.Column('id', sa.Integer, nullable=False, primary_key=True),
	sa.Column('firtName', sa.String(255)),
	sa.Column('lastName', sa.String(255)),
	sa.Column('phone', sa.String(255)),
	sa.Column('email', sa.String(255)),
	sa.Column('adress', sa.String(255)),
	sa.Column('comment', sa.String(1000), nullable=True),
	sa.Column('info', sa.Text),
	sa.Column('status', sa.Integer, default=1),
	sa.Column('created', sa.DateTime, default=datetime.datetime.utcnow),
)

roles = sa.Table(
	'roles', meta,
	
	sa.Column('id', sa.Integer, nullable=False, primary_key=True),
	sa.Column('name', sa.String(255), unique=True),
)

users = sa.Table(
	'users', meta,
	
	sa.Column('id', sa.Integer, nullable=False, primary_key=True),
	sa.Column('role', sa.Integer),
	sa.Column('login', sa.String(255), unique=True),
	sa.Column('user_name', sa.String(255)),
	sa.Column('passw', sa.String(255), nullable=False),
	sa.Column('city', sa.String(255), nullable=False),
)

#комментарии
comments = sa.Table(
	'comments', meta,
	
	sa.Column('id', sa.Integer, nullable=False, primary_key=True),
	sa.Column('name', sa.String(1000)),
	sa.Column('positive', sa.String(250), nullable=True),
	sa.Column('negative', sa.String(250), nullable=True),
	sa.Column('rating', sa.Integer, default=1),
	sa.Column('created', sa.DateTime, default=datetime.datetime.utcnow),
	sa.Column('status', sa.Boolean, default=False),
	
	#ссылка на самого себя
	sa.Column('cid', sa.Integer, nullable=True),
	
	#ссылка на юзера
	sa.Column('uid', sa.Integer),
	
	#ссылка на продукт, 0 означает что коммент оставлен на магазин а не на кокретный товар
	sa.Column('pid', sa.Integer, default=0),
	
)

blogs = sa.Table(
	'blogs', meta,
	
	sa.Column('id', sa.Integer, nullable=False, primary_key=True),
	sa.Column('name', sa.String(255), nullable=True),
	sa.Column('content', sa.Text, nullable=True),
	sa.Column('pre_content', sa.String(500), nullable=True),
	sa.Column('poster', sa.String(1000), default=""),
	sa.Column('slug', sa.String(255), unique=True),
	sa.Column('seo_title', sa.String(255), nullable=True),
	sa.Column('seo_desc', sa.String(255), nullable=True),
	sa.Column('created', sa.DateTime, default=datetime.datetime.utcnow),
	
)

pages = sa.Table(
	'pages', meta,
	
	sa.Column('id', sa.Integer, nullable=False, primary_key=True),
	sa.Column('name', sa.String(255), nullable=True),
	sa.Column('content', sa.Text, nullable=True),
	sa.Column('slug', sa.String(255), unique=True),
	sa.Column('seo_title', sa.String(255), nullable=True),
	sa.Column('seo_desc', sa.String(255), nullable=True),
)

menus = sa.Table(
	'menus', meta,
	
	sa.Column('id', sa.Integer, nullable=False, primary_key=True),
	sa.Column('parent', sa.Integer, default=0),
	sa.Column('name', sa.String(255), nullable=False),
	sa.Column('icon', sa.Text, default=""),
	sa.Column('level', sa.Integer, default=0, nullable=False),
	sa.Column('order', sa.Integer, default=0, nullable=False),
	
	#pages id
	sa.Column('pid', sa.Integer, default=0, nullable=False),

)

categories = sa.Table(
	'categories', meta,
	
	sa.Column('id', sa.Integer, nullable=False, primary_key=True),
	sa.Column('name', sa.String(255), nullable=False),
	sa.Column('svg', sa.Text, nullable=True),
	sa.Column('content', sa.Text, default=""),
	sa.Column('slug', sa.String(255), unique=True, nullable=False),
	sa.Column('seo_title', sa.String(255), default=""),
	sa.Column('seo_desc', sa.String(255), default=""),
	
	#ссылка на акцию
	sa.Column('stocks_id', sa.Integer, default=0),
	
	#ссылка на себя
	sa.Column('parent', sa.Integer, default=0),
	
	sa.Column('order', sa.Integer, default=0, nullable=False),
	
	#будет ли включена категория в выборку, для слайдеров
	sa.Column('sliders_active', sa.Boolean, default=True),
)

manufacturers = sa.Table(
	'manufacturers', meta,
	
	sa.Column('id', sa.Integer, nullable=False, primary_key=True),
	sa.Column('name', sa.String(255), unique=True),
	sa.Column('content', sa.Text, default=""),
	sa.Column('slug', sa.String(255), unique=True, nullable=False),
	sa.Column('seo_title', sa.String(255), default=""),
	sa.Column('seo_desc', sa.String(255), default=""),
	
)

products = sa.Table(
	'products', meta,
	
	sa.Column('id', sa.Integer, nullable=False, primary_key=True),

	sa.Column('name', sa.String(255), nullable=False),
	sa.Column('content', sa.Text, default=""),

	sa.Column('slug', sa.String(255), unique=True),
	sa.Column('price', sa.Integer, default=0),
	sa.Column('old_price', sa.Integer, default=0),
	
	sa.Column('seo_title', sa.String(255), default=""),
	sa.Column('seo_desc', sa.String(255), default=""),
	
	#кол-во заказавших
	sa.Column('sold', sa.Integer, nullable=False, default=0),
	
	#постер
	sa.Column('poster', sa.String(1000)),
	
	#формат изображения
	sa.Column('thumbnail', sa.String(1000)),
	
	sa.Column('market', sa.Boolean, default=False),
	sa.Column('avalible', sa.Boolean, default=True),
	
	#ссылка на производителя
	sa.Column('manufacturer', sa.Integer, nullable=False),
	
	#ссылка на категорию
	sa.Column('parent', sa.Integer, nullable=False),
	
	#ссылка на акцию
	sa.Column('stocks_id', sa.Integer, nullable=False, default=0),
	
)

colors = sa.Table(
	'colors', meta,
	
	sa.Column('id', sa.Integer, nullable=False, primary_key=True),
	sa.Column('name', sa.String(255), nullable=False),
	sa.Column('article', sa.String(255), unique=True, nullable=False),
	sa.Column('img', sa.String(1000)),
	sa.Column('code', sa.String(255)),
	sa.Column('default', sa.Boolean, default=False),
	
	#ссылка на продукт
	sa.Column('pid', sa.Integer, nullable=True),
	
)

#фотки продукта
product_images = sa.Table(
	'product_images', meta,
	
	sa.Column('id', sa.Integer, nullable=False, primary_key=True),
	sa.Column('name', sa.String(1000), nullable=True),
	sa.Column('alt', sa.String(255), nullable=True),
	
	#ссылка на цвет
	sa.Column('cid', sa.Integer, nullable=True),
	
)

accessories = sa.Table(
	'accessories', meta,
	sa.Column('id', sa.Integer, nullable=False, primary_key=True),
	
	#ссылка на товар
	sa.Column('parent', sa.Integer, nullable=False, default=0),
	
	#ссылка на товар который ассоциируется с товаром
	sa.Column('pid', sa.Integer, nullable=False, default=0),
)

characteristics = sa.Table(
	'characteristics', meta,
	sa.Column('id', sa.Integer, nullable=False, primary_key=True),
	sa.Column('name', sa.String(255), nullable=False),
)

cvalues = sa.Table(
	'cvalues', meta,
	sa.Column('id', sa.Integer, nullable=False, primary_key=True),
	sa.Column('name', sa.String(255), nullable=False),
	
	#ссылка на характеристику
	sa.Column('parent', sa.Integer, nullable=False),
)

cvalues_assoc_products = sa.Table(
	'cvalues_assoc_products', meta,
	
	sa.Column('id', sa.Integer, nullable=False, primary_key=True),
	
	#ссылка на продукт
	sa.Column('product_id', sa.Integer, nullable=False),
	
	#ссылка на подарок
	sa.Column('cvalue_id', sa.Integer, nullable=False),
)

stocks = sa.Table(
	'stocks', meta,
	
	sa.Column('id', sa.Integer, nullable=False, primary_key=True),
	sa.Column('type', sa.String(255), nullable=False, default="gift with purchase"),
	sa.Column('name', sa.String(500), nullable=False),
	
	sa.Column('start', sa.DateTime, default=datetime.datetime.utcnow),
	sa.Column('end', sa.DateTime, nullable=False),
	
)

gifts = sa.Table(
	'gifts', meta,
	
	sa.Column('id', sa.Integer, nullable=False, primary_key=True),
	sa.Column('name', sa.String(255), nullable=False),
	
	#постер
	sa.Column('img', sa.String(1000), default=""),
	
	#ссылка на акцию
	sa.Column('parent', sa.Integer, nullable=False, default=0),
	
)

pickings = sa.Table(
	'pickings', meta,
	
	sa.Column('id', sa.Integer, nullable=False, primary_key=True),
	sa.Column('name', sa.String(255), nullable=False),
	
	#постер
	sa.Column('img', sa.String(1000), default=""),
	
)

pickings_assoc_products = sa.Table(
	'pickings_assoc_products', meta,
	
	sa.Column('id', sa.Integer, nullable=False, primary_key=True),
	
	#ссылка на продукт
	sa.Column('product_id', sa.Integer, nullable=False),
	
	#ссылка на подарок
	sa.Column('picking_id', sa.Integer, nullable=False),
)

options = sa.Table(
	'options', meta,
	
	sa.Column('id', sa.Integer, nullable=False, primary_key=True),
	sa.Column('name', sa.String(255), nullable=False),
	sa.Column('price', sa.Integer, default=0),
	
)

options_assoc_products = sa.Table(
	'options_assoc_products', meta,
	
	sa.Column('id', sa.Integer, nullable=False, primary_key=True),
	
	#ссылка на продукт
	sa.Column('product_id', sa.Integer, nullable=False),
	
	#ссылка на опцию
	sa.Column('option_id', sa.Integer, nullable=False),
)

# send_mail = sa.Table(
	# 'send_mail', meta,
	# sa.Column('id', sa.Integer, nullable=False, primary_key=True),
	# sa.Column('action', sa.String(255), nullable=False),
	# sa.Column('email', sa.String(255), nullable=False),
	# sa.Column('content', sa.Text),
# )

meta.create_all(conn)