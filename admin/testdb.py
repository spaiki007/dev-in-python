#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime, random, re, time
from sqlalchemy import create_engine
import sqlalchemy as sa

from sqlalchemy import update

from sqlalchemy.sql import and_
from sqlalchemy.sql import func, select, join


class Connection:

	def __init__(self, host, port, database, user, password):
		self.host 		= host
		self.port		= port
		self.database	= database
		self.user		= user
		self.password	= password
	
	def create_conn(self):
		conn = "postgresql://{user}:{password}@{host}:{port}/{database}".format(
			host 		= self.host,
			port 		= self.port,
			database 	= self.database,
			user 		= self.user,
			password 	= self.password,
		)
		return conn
		

# local_conn = Connection('localhost', '5432', 'shopconsoles', 'postgres', 'burda4488@')
# local_conn = create_engine(local_conn.create_conn())
# meta_local = sa.MetaData()

# local_products = sa.Table(
	# 'products', meta_local,
	# sa.Column('id', sa.Integer, nullable=False, primary_key=True),
	# sa.Column('name', sa.String(255), nullable=True),
	# sa.Column('content', sa.Text, nullable=True),
	# sa.Column('price', sa.Integer, nullable=True),
	
	# sa.Column('slug', sa.String(255), unique=True),
	# sa.Column('seo_title', sa.String(255), nullable=True),
	# sa.Column('seo_desc', sa.String(255), nullable=True),
	
	# #постер
	# sa.Column('poster', sa.String(255), default="/static/img/no image avalible.jpg"),
	
	# sa.Column('market', sa.Boolean, default=False),
	# sa.Column('avalible', sa.Boolean, default=True),
	
	# #ссылка на категорию
	# sa.Column('parent', sa.Integer, nullable=True),
# )

# #фотки продукта
# local_product_images = sa.Table(
	# 'product_images', meta_local,
	# sa.Column('id', sa.Integer, nullable=False, primary_key=True),
	# sa.Column('path', sa.String(255), nullable=True),
	# sa.Column('alt', sa.String(255), nullable=True),
	
	# #ссылка на продукт
	# sa.Column('parent', sa.Integer, nullable=True),
	# sa.Column('product_id', sa.Integer, sa.ForeignKey("products.id")),
# )

# #свойства продукта
# local_product_features = sa.Table(
	# 'product_features', meta_local,
	# sa.Column('id', sa.Integer, nullable=False, primary_key=True),
	# sa.Column('features', sa.String(255), nullable=True),
	# sa.Column('value', sa.String(255), nullable=True),
	# #ссылка на продукт
	# sa.Column('parent', sa.Integer, nullable=True),
# )
# meta_local.create_all(local_conn)		


conn = Connection('81.177.6.145', '5432', 'shopconsoles_v2', 'postgres', 'burda4488@')
conn = create_engine(conn.create_conn())
meta = sa.MetaData()


#фотки продукта
product_images = sa.Table(
	'product_images', meta,
	sa.Column('id', sa.Integer, nullable=False, primary_key=True),
	sa.Column('path', sa.String(255), nullable=True),
	sa.Column('alt', sa.String(255), nullable=True),
	
	#ссылка на продукт
	sa.Column('parent', sa.Integer, nullable=True),
	sa.Column('product_id', sa.Integer, sa.ForeignKey("products.id")),
	
	#формат изображения
	sa.Column('img_format', sa.String(5), default="jpg"),

)

meta.create_all(conn)



sql_expression = """ SELECT id, path FROM product_images """

all_products_obj= conn.execute(sql_expression)

if all_products_obj is not None:
	for obj in all_products_obj:
	
		sql_expression 	= """UPDATE product_images SET path=(%s) WHERE id=(%s) """
		conn.execute(sql_expression, (obj.path.split('.')[0], obj.id,))
	
	#product_images.update().where(product_images.c.id==obj.id).values(path=obj.path.split('.')[0])
		
		
		


# for sub_menu in conn.execute(menus.select().where(menus.c.parent != None)):
	# print('--', sub_menu.id, sub_menu.name)
	# for cat in conn.execute(category.select()):
		# if sub_menu.id == cat.parent:
			# print("-----", cat.id, cat.name, cat.parent)

# for count, product in enumerate(local_conn.execute(local_products.select())):
	# local_conn.execute(local_product_images.delete().where(local_product_images.c.path == product.poster))



# #добавляем продукт
# def add_product(id, name, content, price, slug, poster, parent):
	# local_conn.execute(local_products.insert().values(
			# id		= id,
			# name 	= name,
			# content	= content,
			# price	= price,
			# slug	= slug,
			# poster	= poster,
			# parent	= parent,
		# )
	# )
	
# def add_image(path, alt, parent, product_id):
	# local_conn.execute(local_product_images.insert().values(
			# path 		= path,
			# alt			= alt,
			# parent		= parent,
			# product_id	= product_id,
		# )
	# )
	
# for count, product in enumerate(conn.execute(products.select())):
	
	# first_img = conn.execute(product_images.select().where(product_images.c.parent==product.id))
	# first_img = first_img.fetchone()
	# add_product(product.id, product.name, product.content, product.price, product.slug, first_img.path, product.parent)
	
	# for img in conn.execute(product_images.select().where(product_images.c.parent==product.id)):
		# add_image(img.path, img.alt, img.parent, img.product_id)

	
# start 	= time.time()
# result 	= conn.execute(products.select())
# result 	= result.fetchall()
# end 	= time.time()
# print(end - start, len(result))


# start 	= time.time()
# sql_expression = """
	# SELECT 
		# products.id,
		# products.name,
		# products.price,
		# products.slug,
		# products.parent,
		# (SELECT path FROM product_images WHERE products.id = product_images.product_id LIMIT 1),
		# (SELECT alt FROM product_images WHERE products.id = product_images.product_id LIMIT 1)
	# FROM products"""
# result 	= conn.execute(sql_expression)
# result 	= result.fetchall()
# end 	= time.time()
# print(end - start, len(result))






# for product in result:
	# for i in range(0, 5):
		# add_image('/static/img/no image avalible.jpg', "What is Lorem Ipsum?", product.id)


# for _ in range(0, 10000):

	# name			= ''.join([random.choice('qwertyuiopasdfghjklzxcvbnm1234567890 -{}<>()/?!') for i in range(0, 255)])
	# content			= ''.join([random.choice('qwertyuiopasdfghjklzxcvbnm1234567890 -{}()/?!') for i in range(0, 5000)])
	# price			= random.randint(100, 100000)
	# slug 			= ''.join([random.choice('qwertyuiopasdfghjklzxcvbnm1234567890') for i in range(0, 10)])
	# seo_title		= "What is Lorem Ipsum?"
	# seo_desc		= "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s..."
	# avalible		= True
	# production_date	= "25.10.1987"
	# parent			= 1

	# add_product(name, content, price, slug, seo_title, seo_desc, avalible, parent)	





#conn.execute(product_images.delete().where(product_images.c.id == 8013))



# sql_expression = """
	# SELECT 
		# products.id,
		# products.name,
		# products.price,
		# products.slug,
		# products.parent,
		# (SELECT path FROM product_images WHERE products.id = product_images.product_id LIMIT 1),
		# (SELECT alt FROM product_images WHERE products.id = product_images.product_id LIMIT 1),
		# (SELECT product_id FROM product_images WHERE products.id = product_images.product_id LIMIT 1)
	# FROM products
	# WHERE parent=(%s) AND name ILIKE (%s)
# """

# # j = join(products, product_images, products.c.id == product_images.c.product_id)
# # sql_expression = select([products, product_images], products.c.parent == 2).select_from(j)
# # print(sql_expression)


# response = conn.execute(sql_expression, (2, '%1TB%',))
# for resp in response.fetchall():
	# print(resp.product_id, resp.name)


# for images in conn.execute(product_images.select()):
	# conn.execute(product_images.update().values(product_id=images.parent).where(product_images.c.id == images.id))

# conn.execute("ALTER TABLE product_images DROP COLUMN product_id")


# conn.execute("ALTER TABLE product_images ADD product_id integer REFERENCES products(id)")

# j = join(products, test_images, products.c.id == test_images.c.product_id)
# response = conn.execute(select([products, test_images]).limit(1).select_from(j))
# response = response.fetchall()
# print(response)

# result = conn.execute(select([func.count()], products.c.parent == 2).select_from(products))
# print(result)



# for resp in response:
	# print(resp.name, resp.product_id)

#conn.execute(test_images.insert().values(product_id = 506))



#conn.execute(products.update().values(market=False).where(products.c.id == 506))
	
# for product in conn.execute(products.select()):
	# print(product.market)



#conn.execute("ALTER TABLE products ADD COLUMN market BOOLEAN NOT NULL DEFAULT FALSE")

#conn.execute("ALTER TABLE products DROP COLUMN video")

	
#replace = re.compile(r"Пункты самовывоза находятся по адресам:", re.I)
	
# for count, product in enumerate(conn.execute(products.select())):
	# #conn.execute(products.update().values(content=product.content.strip()).where(products.c.id == product.id))
	
	# if replace.search(product.content):
		# print(product.content)
		#conn.execute(products.update().values(content=replace.sub('', product.content)).where(products.c.id == product.id))
	#print(replace.sub('', product.content))
	#print(count)

	
#data = datetime.datetime.now()
#print(data.strftime('%d/%m/%Y'), data.strftime('%H:%M:%S'))

# conn.execute(products.delete())
# conn.execute(product_images.delete())
# conn.execute(product_features.delete())

#stmp = products.update().values(name='asdasdasdasd', slug='asd').where(products.c.id == 1)
#conn.execute(products.update().values(name='a1', slug='1').where(products.c.id == 1))




# def save(name='', parent=None, level=0):
	# response = conn.execute(menus.insert().values(
			# name 	= name,
			# parent	= parent,
			# level 	= level,
		# ).returning(menus.c.id, menus.c.parent)
	# )
	
	# last_entry 	= [(resp.id, resp.parent,) for resp in response]
	# last_entry 	= last_entry[0]
	# id, parent_id = last_entry
		
		# result = conn.execute(menus.select().where(menus.c.id == parent_id)).fetchone()
		# print(result)
		
#save(name='Xbox')
#save(name='Аксессуары', parent=2, level=1)

# def tree():
	# for menu in conn.execute(menus.select().where(menus.c.parent == None)).fetchall():
		# sub_menu = conn.execute(menus.select().where(menus.c.parent == menu.id)).fetchall()
		# print(sub_menu)
	# print("-" * response.level, response.name)
	# if response.child:
		# tree(response.child)
		
#tree()
		
# def delete():
	# #удаление первого поля
	# conn.execute(menus.delete().where(menus.c.id > 3))
# #delete()


# #вставка данных в бд
# def all():
	# return conn.execute(menus.select()).fetchall()	
#print(all())

# result = conn.execute(users.select())
# print(result.fetchone())

# content = conn.execute(contents.select())
# result2 = content.fetchall()

# var = conn.execute(send_contents.select())
# var1 = var.fetchall()

# for cont in result2:

	# result = conn.execute(send_contents.select().where(and_(
																# send_contents.c.id_cli == 1,
																# send_contents.c.id_cont == cont.id
															# )
														# )
													# )
						
	# if result.fetchone() is None:
		# print('Добавляю')
		# #conn.execute(send_contents.insert().values(id_cli=1, id_cont=cont.id))
	# else:
		# print('Уже добавленно!')
	


# result = conn.execute(users.select().where(users.c.id == 1))
# id_cli = result.fetchone()

# result = conn.execute(contents.select().where(contents.c.id == 1))
# id_cont = result.fetchone()

#conn.execute(send_contents.insert().values(id_cli=1, id_cont=1))

# conn.execute(send_contents.delete())
# conn.execute(contents.delete())
# conn.execute(users.delete())

# result = conn.execute(contents.select().with_only_columns([contents.c.id]))

# conn.execute(users.update().where(users.c.vk_id == 12345).values(online=False))
# conn.execute(users.update().where(users.c.vk_id == 123456).values(online=False))



#result = conn.execute(contents.select().where(contents.c.job.like("%лендинг%")))

# result = conn.execute(users.select())
# res = result.fetchall()
# print(res)


# if res is not None:
	# id, id_cli, id_cont = res
	# print(id, id_cli, id_cont)


#conn.execute(send_contents.insert().values(id_cli=1, id_cont=1))


# txt="""
	# <h2 class="job_name">Изи 5</h2>
	# <div class="job_desc">Ищу специалиста по рекламе на Авито. Наличие положительного опыта обязательно.</div>
	# <div class="contacts">
		# <div>Город: Москва</div>
		# <div>Телефон: +79851623717</div>
		# <div>skype: prokurorus1973</div>
		# <div>email: prokurorus@mail.ru</div>
	# </div>
	# <a href='https://freelance.ru/projects/reklama-na-avito-950019.html' class='job_link' target="_blank">Ссылка на задание...</a>
	# <a href='https://freelance.ru/prokurorus' class='job_user_link' target="_blank">Cсылка на страницу заказчика...</a>
# """
# conn.execute(contents.insert().values(job=txt))

# result = conn.execute(contents.select())
# print(result.fetchall())

#user_datetime = datetime.datetime.today()+datetime.timedelta(days=360)
# for i in range(1, 10):
	# conn.execute(users.insert().values(vk_id=i, pwd='bS2Ca#$cv(', exp_date=user_datetime))
	
#conn.execute(users.insert().values(vk_id=123456, pwd='admin', online=False, exp_date=user_datetime))

# result = conn.execute(users.select())
# print(result.fetchall())




