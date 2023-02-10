<template>
	<div class="main">
		<div class="header">
			<router-link :to="{name: 'home'}">ES-ADMIN v.1</router-link>
		</div>

		<div class="wrap_content">
			<div class="leftBar">

				<router-link :to="{name: 'sliders'}">Слайдер</router-link>

				<div class="menu-block">
					<router-link :to="{name: 'orders'}">Заказы</router-link>
					<div class="child">
						<router-link :to="{name: 'quickOrders'}">- Быстрые заказы</router-link>
						<router-link :to="{name: 'callbacks'}">- Обратные звонки</router-link>
					</div>
				</div>

				<router-link :to="{name: 'roles'}">Роли</router-link>
				<router-link :to="{name: 'users'}">Пользователи</router-link>
				<router-link :to="{name: 'comments'}">Комментарии</router-link>
				<router-link :to="{name: 'blogs'}">Блог</router-link>
				<router-link :to="{name: 'pages'}">Страницы</router-link>
				<router-link :to="{name: 'menus'}">Меню</router-link>

				<router-link :to="{name: 'categories'}">Категории</router-link>
				<router-link :to="{name: 'manufacturers'}">Производители</router-link>

				<div class="menu-block">
					<router-link :to="{name: 'stocks'}">Акции</router-link>
					<div class="child">
						<router-link :to="{name: 'gifts'}">- Подарки</router-link>
					</div>
				</div>

				<div class="menu-block">
					<router-link :to="{name: 'products'}">Продукты</router-link>
					<div class="child">
						<router-link :to="{name: 'characteristics'}">- Характеристики</router-link>
						<router-link :to="{name: 'cvalues'}">- Значения xарактеристик</router-link>
						<router-link :to="{name: 'pickings'}">- Комплектации</router-link>
						<router-link :to="{name: 'options'}">- Опции</router-link>
					</div>
				</div>

	        </div>

			<div class="content"><div class="block"><router-view/></div></div>

		</div>
	</div>
</template>
