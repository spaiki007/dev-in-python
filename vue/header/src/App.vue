<template>
	<div id="header-app">


		<header class="header">

			<div :class="['wrap-top-menu', {active: positionAbsolute}]">
				<div class="top-menu">
					<nav class="menu">
						<div id="header-top" class="svg-menu-icon">

							<a href="#header-top" class="mobile-menu-block" v-if="!menuOpen" @click="openMenu">
								<img class="mobile-menu-icon" :src="$store.state.domain +  '/static/img/mobile-menu.png'">
							</a>

							<div :class="['mobile-menu-block', {active: menuOpen}]" v-else @click="openMenu">
								<img :src="$store.state.domain +  '/static/img/top-menu-icon-mobile.png'">
							</div>

							<div class="hidden-mobile-menu" v-show="menuOpen">

								<div v-for="menu in menus" :key="menu.id" v-if="menu.data.length && menu.id == 999999 && !mainPage" class="top-menu-name" >

									<a class="category-block" v-for="(object, index) in menu.data" :key="object.id" v-if="index < visibleCount" :href="$store.state.domain + object.link" >
										<div class="icon" v-if="object.svg != null" v-html="object.svg"></div>
										<div class="wrap-icon">
											<div class="category-name">{{ object.name }}</div>
											<div class="icon-border"></div>
										</div>
									</a>

									<a href="#" class="category-block" v-if="!mainPage">
										<div class="icon">
											<img :src="$store.state.domain +  '/static/img/manufacturers-header-icon.png'">
										</div>

										<div class="wrap-icon">
											<div class="category-name">
												Производители
											</div>
											<div class="icon-border"></div>
										</div>
									</a>
								</div>

								<div class="wrap-icon open-all" @click="openCatalog">
									<div class="category-name">{{ catalogName }}</div>
									<div class="icon-border"></div>
								</div>

								<div v-for="menu in menus" :key="menu.id" v-if="menu.data.length && menu.id != 999999" class="top-menu-name" >
									<div class="wrap-top-menu-name" >
										<div class="name">{{ menu.name }}</div>
									</div>

									<div class="wrap-hidden-menu">
										<div class="hidden-menu">
											<a v-for="object in menu.data" :key="object.id" :href="$store.state.domain + object.link">{{ object.name }}</a>
										</div>
									</div>
								</div>

								<div class="top-menu-name" >
									<div class="wrap-top-menu-name">
										<div class="name">Блог</div>
									</div>
								</div>

								<div class="top-menu-name" >
									<div class="wrap-top-menu-name">
										<div class="name">Отзывы</div>
									</div>
								</div>

								<div class="mobile-menu-contacts-block">
									<div class="wrap-top-phone">
										<div class="top-phone">
											<div class="phone phone-1">
												+7 (495) 481-40-37
											</div>
											<div class="top-phone-name">
												Заказы принимаются круглосуточно
											</div>
										</div>
										<div class="top-phone top-phone-2">
											<div class="phone  phone-2">
												+7 (495) 481-40-39
											</div>
											<div class="messenger-block">
												<div class="messenger-icon">
													<img :src="$store.state.domain +  '/static/img/viber-icon.png'">
													<div class="messenger-icon-name">Viber</div>
												</div>
												<div class="messenger-icon messenger-icon-center">
													<img :src="$store.state.domain +  '/static/img/watsapp-icon.png'">
													<div class="messenger-icon-name">Whatsapp</div>
												</div>
												<div class="messenger-icon">
													<img :src="$store.state.domain +  '/static/img/telegram-icon.png'">
													<div class="messenger-icon-name">Telegram</div>
												</div>
											</div>
										</div>
									</div>

									<div class="adress-info">
										<div class="top-adress">г. Москва, пр. Волгоградский, д. 32, к. 8</div>
										<div class="top-operating-mode">9:00 — 18:00 (Пн — Пт)</div>
									</div>

								</div>

							</div>
						</div>

						<div v-for="menu in menus" :key="menu.id" v-if="menu.data.length && menu.id == 999999 && !mainPage" class="top-menu-name">

							<div :class="['wrap-top-menu-name', {active: menu.active}]" @click="changeMenus(menu.id)">
								<div class="name">{{ menu.name }}</div>
								<img v-if="!menu.active" :src="$store.state.domain + '/static/img/top-menu-arrow.png'">
								<img v-else :src="$store.state.domain + '/static/img/top-menu-arrow-hover.png'">
							</div>

							<div :class="['wrap-hidden-menu', {active: menu.active}]">
								<div class="hidden-menu-icon">
									<img :src="$store.state.domain + '/static/img/top-hidden-menu-arrow.png'">
								</div>
								<div class="hidden-menu">
									<a v-for="object in menu.data" :key="object.id" :href="$store.state.domain + object.link">{{ object.name }}</a>
								</div>
							</div>
						</div>

						<div class="top-menu-name" v-if="!mainPage">
							<div class="wrap-top-menu-name">
								<a href="/shop/manufacturers">Производители</a>
							</div>
						</div>

						<div v-for="menu in menus" :key="menu.id" v-if="menu.data.length && menu.id != 999999" class="top-menu-name">

							<div :class="['wrap-top-menu-name', {active: menu.active}]" @click="changeMenus(menu.id)">
								<div class="name">{{ menu.name }}</div>
								<img v-if="!menu.active" :src="$store.state.domain + '/static/img/top-menu-arrow.png'">
								<img v-else :src="$store.state.domain + '/static/img/top-menu-arrow-hover.png'">
							</div>

							<div :class="['wrap-hidden-menu', {active: menu.active}]">
								<div class="hidden-menu-icon">
									<img :src="$store.state.domain + '/static/img/top-hidden-menu-arrow.png'">
								</div>
								<div class="hidden-menu">
									<a v-for="object in menu.data" :key="object.id" :href="$store.state.domain + object.link">{{ object.name }}</a>
								</div>
							</div>
						</div>

						<div class="top-menu-name">
							<div class="wrap-top-menu-name">
								<a href="/blogs">Блог</a>
							</div>
						</div>

						<div class="top-menu-name">
							<div class="wrap-top-menu-name">
								<a href="/shop/comments">Отзывы</a>
							</div>
						</div>

					</nav>

					<div class="search">
						<div class="search-input"></div>
						<div class="icon">
							<img :src="$store.state.domain + '/static/img/search-header-icon.png'">
						</div>
					</div>

					<div :class="['wrap-basket', {active: basket.active}]" @click="componentsViews(1)" @mouseover="basket.active = true" @mouseout="basket.active = false">
						<div class="bascket">
							<div class="count-products">{{ $store.state.data.length }}</div>
							<img :src="$store.state.domain + '/static/img/bascket-header-icon.png'">
						</div>
						<div class="bascket-name">корзина</div>
					</div>

				</div>

				<div class="panel" v-show="currentComponent">
					<component :is="currentComponent" />
				</div>

			</div>

			<div class="head-info-block">

				<div class="logo-block">
					<a href="/"><img class="logo" :src="$store.state.domain + '/static/img/logo.png'"></a>
					<div class="logo-name">персональный электротранспорт</div>

					<div class="wrap-callback" @mouseover="buttonIsActive = true" @mouseout="buttonIsActive = false" @click="callbackForm = true">
						<div :class="['callback-background', {active: buttonIsActive}]">
							<div class="wrap-callback-background"></div>
						</div>
						<div class="callback">
							<img :src="$store.state.domain + '/static/img/icon-phone.png'">
							<div class="callback-name">Обратный звонок</div>
						</div>
					</div>
					<callback v-if="callbackForm" :close="close"></callback>
				</div>

				<div class="top-contact-info">
					<div class="search">
						<input class="search-field" type="text" placeholder="Например, электросамокаты MaxSpeed">

						<div class="top-icon-search">
							<img :src="$store.state.domain + '/static/img/search-header-icon.png'">
						</div>
					</div>

					<div class="wrap-contact-info">
						<div class="contact-info">
							<div class="phone-icon">
								<img :src="$store.state.domain + '/static/img/header-contacts-icon.png'">
							</div>

							<div class="wrap-top-phone">

								<div class="top-phone">
									<div class="phone phone-1">+7 (495) 481-40-37</div>
									<div class="top-phone-name">Заказы принимаются круглосуточно</div>
								</div>

								<div class="top-phone top-phone-2">
									<div class="phone  phone-2">+7 (495) 481-40-39</div>
									<div class="messenger-block">

										<div class="messenger-icon">
											<img :src="$store.state.domain + '/static/img/viber-icon.png'">
											<div class="messenger-icon-name">Viber</div>
										</div>

										<div class="messenger-icon messenger-icon-center">
											<img :src="$store.state.domain + '/static/img/watsapp-icon.png'">
											<div class="messenger-icon-name">Whatsapp</div>
										</div>

										<div class="messenger-icon">
											<img :src="$store.state.domain + '/static/img/telegram-icon.png'">
											<div class="messenger-icon-name">Telegram</div>
										</div>

									</div>
								</div>
							</div>
						</div>

						<div class="contact-adress level-3">

							<div class="adress-icon">
								<img :src="$store.state.domain + '/static/img/header-map-icon.png'">
							</div>
							<div class="adress-info">
								<div class="top-adress">г. Москва, пр. Волгоградский, д. 32, к. 8</div>
								<div class="top-operating-mode">9:00 — 18:00 (Пн — Пт)</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</header>
	</div>
</template>

<script>

import axios from 'axios';
import Callback from './components/Callback.vue';
import PreOrder from './components/PreOrder.vue';
import Order from './components/Order.vue';
import TrueOrder from './components/TrueOrder.vue';

export default {
	name: 'header-app',
	data: function(){
		return {

			currentComponent: false,

			tabs: [
				{'id': 1, 'active': false, 'component': PreOrder},
				{'id': 2, 'active': false, 'component': Order},
				{'id': 3, 'active': false, 'component': TrueOrder},
			],

			positionAbsolute: false,

			menuOpen: false,
			menus: [],
			basket: {
				active: false,
			},

			visibleCount: 3,
			catalogName: "Посмотреть все",

			mainPage: false,
			buttonIsActive: false,

			callbackForm: false,

		}
	},

	components: {Callback, PreOrder, Order},

	mounted: function (){
		this.$nextTick(function(){

			let o = this;

			if(window.location.pathname == '/'){
				o.mainPage = true;
			}

			axios.get(o.$store.state.domain + '/shop/get-menus').then(function(response){
				o.menus = response.data;
			}).catch(function (error){
				console.log(error);
			});

		})
	},

	methods: {

		openMenu(){
			this.menuOpen = !this.menuOpen;
			this.positionAbsolute = !this.positionAbsolute;
		},

		componentsViews: function(id){

			window.scrollTo(0,0);

			this.positionAbsolute 	= true;

			for(let i = 0; i<this.tabs.length; i++){

				if(this.tabs[i].id == id){
					if(this.tabs[i].active){
						this.currentComponent 	= false;
						this.tabs[i].active		= false;
						this.positionAbsolute 	= false;
					}else{
						this.currentComponent 	= this.tabs[i].component;
						this.tabs[i].active		= true;
					}
				}else{
					this.tabs[i].active 	= false;
				}

			}

		},

		close (){
			this.callbackForm = false;
		},

		openCatalog (){
			if(this.visibleCount == 3){

				for(let i=0; i<this.menus.length; i++){
					if(this.menus[i].id == 999999){
						this.visibleCount = this.menus[i].data.length;
					}
				}

				this.catalogName = "Скрыть";
			}else{
				this.visibleCount = 3;
				this.catalogName = "Посмотреть все";
			}

		},

		changeMenus (id){

			let o = this;
			for(let i = 0; i<o.menus.length; i++){
				if(o.menus[i].id == id){
					if(o.menus[i].active){
						o.menus[i].active = false;
					}else{
						o.menus[i].active = true;
					}
				}else{
					o.menus[i].active = false;
				}
			}

		},

	},


}
</script>
