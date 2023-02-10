<template>
	<div id="catalog-app" class="categories-app">
		<div class="catalog-products">
			<div class="filters">
				<div class="filters-name-block">
					<img :src="domain + '/static/img/filter-name-icon.png'" class="filters-name-icon">
					<div class="filters-name">фильтры</div>
				</div>

				<!--
				<div class="filter">
					<div class="filter-name">Артикул</div>
					<div class="icon-border"></div>
					<div class="filters-article">
						<div class="filter-article">
							<input v-model="search" class="filter-article-input">
							<img class="filter-article-icon" :src="domain + '/static/img/filter-close-icon.png'">
						</div>
					</div>
				</div>
				-->

				<div class="filter">
					<div class="filter-name">Цена (рубли)</div>
					<div class="icon-border"></div>

					<div class="user-slider">
						<range-slider class="slider" :min="staticMin" :max="staticMax" step="100" v-model="valMin"></range-slider>
						<range-slider class="slider" :min="staticMin" :max="staticMax" step="100" v-model="valMax"></range-slider>
				  	</div>

					<div class="filter-range">
						<div class="filter-start">{{ valMin }}</div>
						<div class="filter-end">{{ valMax }}</div>
					</div>
				</div>

				<div class="filter">
					<div class="filter-name">Наличие</div>
					<div class="icon-border"></div>
					<div class="filters-radio-button">

						<div class="filter-radio-button-block" @click="avalible = false">
							<div class="filter-radio-button-wrap">
								<div :class="['filter-radio-button', {'radio-active': !avalible}]"></div>
							</div>
							<div class="filter-checkbox-name">Все товары</div>
						</div>

						<div class="filter-radio-button-block" @click="avalible = true">
							<div class="filter-radio-button-wrap">
								<div :class="['filter-radio-button', {'radio-active': avalible}]"></div>
							</div>
							<div class="filter-checkbox-name">Товары в наличии</div>
						</div>

					</div>
				</div>

				<div class="filter">
					<div class="filter-name">Производитель</div>
					<div class="icon-border"></div>
					<div class="filters-select">
						<div class="main-category-select" @click="manufacturer.active = !manufacturer.active">
							<div class="main-category-products-bottom-name">{{ manufacturer.name }}</div>
							<img class="main-arrow-top-bottom" :src="domain + '/static/img/arrow-top-bottom.png'">
						</div>
						<div class="sort-by-list" v-if="manufacturer.active">
							<div class="sort-by" @click="changeManufacturers(false, 'Выберите бренд')">Выберите бренд</div>
							<div v-for="obj in manufacturer.objects" :key="obj.id" class="sort-by" @click="changeManufacturers(obj.id, obj.name)">{{ obj.name }}</div>
						</div>
					</div>

				</div>

				<!--
				<div class="filter">
					<div class="filter-name">Диаметр колес (дюймы)</div>
					<div class="icon-border"></div>
					<div class="filters-checkbox">
						<div class="filter-checkbox-block">
							<div class="filter-checkbox">
								<img :src="domain + '/static/img/checkboxcheck.png'" class="filter-checkbox-check check-active">
							</div>
							<div class="filter-checkbox-name">8</div>
						</div>

						<div class="filter-checkbox-block">
							<div class="filter-checkbox">
								<img :src="domain + '/static/img/checkboxcheck.png'" class="filter-checkbox-check">
							</div>
							<div class="filter-checkbox-name">6</div>
						</div>
					</div>
				</div>

				<div class="filter-search">

					<div class="wrap-callback find-produts">
						<div class="callback-background">
							<div class="wrap-callback-background"></div>
						</div>
						<div class="callback">
							<div class="callback-name">найти</div>
						</div>
					</div>

				</div>
				-->

				<div class="filter">
					<div class="filter-name">Категории</div>
					<div class="icon-border"></div>
					<div class="filter-categories">
						<div class="filter-category" v-for="key, val in categories" :key="val">
							<a class="name" :href="'/shop/categories/' + key.category.slug">{{ key.category.name }}</a>
							<a class="sub-name" v-for="(key2, item) in key.subCat" :key="key2.id" :href="'/shop/categories/' + key2.slug" v-if="item < 3">{{ key2.name }}</a>
							<a class="sub-name" v-for="(key2, item) in key.subCat" :key="key2.id" :href="'/shop/categories/' + key2.slug" v-if="item > 3 && key.active">{{ key2.name }}</a>
							<div class="sub-cat-open" v-if="key.subCat.length > 3" @click="key.active = !key.active">
								раскрыть <svg aria-hidden="true" focusable="false" data-prefix="fas" data-icon="chevron-down" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" class="svg-inline--fa fa-chevron-down fa-w-14 fa-2x"><path fill="currentColor" d="M207.029 381.476L12.686 187.132c-9.373-9.373-9.373-24.569 0-33.941l22.667-22.667c9.357-9.357 24.522-9.375 33.901-.04L224 284.505l154.745-154.021c9.379-9.335 24.544-9.317 33.901.04l22.667 22.667c9.373 9.373 9.373 24.569 0 33.941L240.971 381.476c-9.373 9.372-24.569 9.372-33.942 0z" class=""></path></svg>
							</div>
						</div>
					</div>
				</div>

				<div class="filter-search">
					<div class="wrap-callback" @mouseover="buttonIsActive = true" @mouseout="buttonIsActive = false" @click="getProducts">
						<div :class="['callback-background', {active: buttonIsActive}]">
							<div class="wrap-callback-background"></div>
						</div>
						<div class="callback">
							<div class="callback-name">Найти</div>
						</div>
					</div>
					<div class="wrap-callback" @mouseover="buttonIsActive2 = true" @mouseout="buttonIsActive2 = false" @click="location.reload()">
						<div :class="['callback-background', {active: buttonIsActive2}]">
							<div class="wrap-callback-background"></div>
						</div>
						<div class="callback">
							<div class="callback-name">Сбросить фильтры</div>
						</div>
					</div>
				</div>

			</div>

			<div class="sort-and-category-products">

				<div class="sort-block">

					<div class="filter-sort" @click="sort.active = !sort.active">
						<div class="name">Сортировка по {{ sort.activeName }}</div>
						<img class="icon" :src="domain + '/static/img/arrow-top-bottom.png'">
					</div>
					<div class="sort-by-list" :style="{ display: sort.active ? 'block' : 'none' }">
						<div v-for="obj in sort.variant" :key="obj.id" class="sort-by" @click="selectSort(obj.id, obj.name)">{{ obj.name }}</div>
					</div>

				</div>

				<div class="main-action-category-products catalog">

					<callback v-if="quickOrderOpen" :close="close" :product="activeProduct"></callback>
					<addbasket v-if="color.active" @close-color="closeColor" :product="color.product"></addbasket>

					<div class="products">
						<div v-for="(object, index) in objects.slice(pagination.active * pagination.max)" v-show="index < pagination.max" :key="object.id" class="product">
							<div class="wrap-product">
							  <div class="product-block-1">
								  <div class="product-image-block" :style="[{backgroundImage: 'url(' + object.poster + ')'}]"></div>
								  <a :href="domain + '/shop/products/' + object.slug" class="product-name">{{ object.name }}</a>
								  <div class="product-rating">
									  <img class="star" :src="domain + '/static/img/raiting-fill.png'">
									  <img class="star" :src="domain + '/static/img/raiting-fill.png'">
									  <img class="star" :src="domain + '/static/img/raiting-fill.png'">
									  <img class="star" :src="domain + '/static/img/raiting-fill.png'">
									  <img class="star" :src="domain + '/static/img/raiting.png'">
								  </div>
							  </div>
							  <div class="product-block-2">
								  <div class="product-price">{{ object.price }} руб.</div>
								  <div class="product-action-block" v-if="object.old_price != 0">
									  <div class="old-price">{{ object.old_price }} руб.</div>
									  <div class="all-categories-count">-{{ procent(object) }}%</div>
								  </div>
							  </div>

								<div class="product-block-3">

									<!--
									<div v-for="(characteristic, item) in object.characteristics" :key="characteristic.id" v-if="item < 3" class="characteristic">
										<div class="product-parameter-name">{{ characteristic.key }}</div>
										<div class="product-parameter-key">{{ characteristic.value }}</div>
									</div>
									-->

									<div  class="characteristic">
										<div class="product-parameter-name">Цвета</div>
										<div class="product-parameter-key colors">
											<div v-for="(color, item) in object.colors" :key="color.id" v-if="item < 4" class="product-colors" :style="getBack(color)"></div>
										</div>
									</div>
								</div>

								<div class="product-block-4">

									<div class="product-basket" @click="openColor(object)">
										<img :src="domain + '/static/img/slider-icon-2.png'">
										<div class="product-basket-name">В корзину</div>
									</div>

									<div class="quick-order" @click="quickOrder(object)">
										<img :src="domain + '/static/img/slider-icon-1.png'">
										<div class="product-basket-name">Быстрый заказ</div>
									</div>

								</div>

							</div>
						</div>

					</div>
				</div>
				<!-- end products -->

				<div class="pagination-block" v-if="objects.length > pagination.max">
					<div class="pagination-name">Страницы:</div>
					<div v-for="(count, index) in pagination.countPages" :class="['pagination-link', {'pagination-active-link': index == pagination.active}]" @click="pagination.active = index">{{ count }}</div>
				</div>
			</div>

		</div>

	</div>
</template>

<script>

import axios from 'axios';
import Callback from './components/Callback.vue'
import AddBasket from './components/AddBasket.vue'

import RangeSlider from 'vue-range-slider'
import 'vue-range-slider/dist/vue-range-slider.css'

export default {

	name: 'catalog-app',

	components: {
		'callback': Callback,
		'addbasket': AddBasket,
		RangeSlider,
	},

	data: function(){
		return {

			valMin: 	0,
			valMax: 	0,

			staticMin: 	0,
			staticMax: 	0,

			avalible: false,

			color: {
				active: false,
				product: false,
			},

			activeProduct: false,
			quickOrderOpen: false,

			buttonIsActive: false,
			buttonIsActive2: false,

			domain:		'http://localhost',
			//domain: "",

			sort: {
				activeName: "наименованию, a-z",
				active: false,
				variant: [
					{id: 1, name: 'наименованию, a-z'},
					{id: 2, name: 'наименованию, z-a'},
					{id: 3, name: 'цене, от низкой к высокой'},
					{id: 4, name: 'цене, от высокой к низкой'},
				],

			},

			pagination: {
				max: 		11,
				countPages: 0,
				active:		0,
			},

			category:		false,
			objects: 		[],
			manufacturer:	{
				id: false,
				name: "Выберите бренд",
				active: false,
				objects: [],
			},
			categories: {},
			//assoc: 				[],
			//characteristics: 	[],
		}
	},

	mounted: function (){
		this.$nextTick(function(){

			let o = this;

			let path 	= document.location.pathname.split('/');
			o.category 	= path[path.length-1];

			let params = {
				slug: 		o.category,
				min: 		0,
				max: 		0,
				avalible: 	false,
				manufacturer: o.manufacturer.id,
		    }

			axios.get(o.domain + '/shop/categories/get-products', {params: params}).then(function(response){

				let r = JSON.parse(response.data);

				o.objects = r.products;
				o.manufacturer.objects = r.manufacturers;
				o.categories = r.categories;

				if(o.objects.length > o.pagination.max){
					o.pagination.countPages = Math.ceil(o.objects.length / o.pagination.max);
				}

				o.staticMin = r.constMin;
				o.valMin	= r.constMin;

				o.staticMax = r.constMax;
				o.valMax 	= r.constMax;

			}).catch(function (error){
				console.log(error);
			});


		});
	},

	methods: {

		changeManufacturers(id, name){
			this.manufacturer.id = id;
			this.manufacturer.name = name;
			this.manufacturer.active = false;
		},

		getProducts(){
			let o = this;

			let params = {
				slug: 			this.category,
				min: 			this.valMin,
				max: 			this.valMax,
				avalible: 		this.avalible,
				manufacturer: 	this.manufacturer.id,
		    }

			axios.get(o.domain + '/shop/categories/get-products', {params: params}).then(function(response){

				let r = JSON.parse(response.data);
				o.objects = r.products;

				if(o.objects.length > o.pagination.max){
					o.pagination.countPages = Math.ceil(o.objects.length / o.pagination.max);
				}

			}).catch(function (error){
				console.log(error);
			});
		},

		openColor(object){

			let o = this;

			if(object.colors.length > 1){
				o.color.active = true;
				o.color.product = object;
			}else{
				let data = new FormData();
				data.append("order", JSON.stringify({id: object.colors[0].article, giftID: '', optionIDS: []}));
				axios.post(o.domain + '/shop/products/add-basket', data).then(function(response){
					location.reload();
				}).catch(function (error){
					console.log(error);
				});
			}

		},

		closeColor(){
			this.color.active = false;
			this.color.product = false;
		},

		getBack(object){

			if(object.poster == ""){
				return {'background': object.code};
			}
			return {'background-image': "url('" + object.poster + "')"};

		},

		quickOrder(object){
			this.quickOrderOpen = true;
			this.activeProduct = object;
		},

		close (){
			this.quickOrderOpen = false;
			this.activeProduct = false;
		},

		procent: function (object){
			return Math.ceil(((object.old_price - object.price) * 100) / object.old_price);
		},

		getPaginations(){
			if(this.objects.length > this.pagination.max){
				this.pagination.countPages = Math.ceil(this.objects.length / this.pagination.max);
			}
		},

		getObjectID(object){
			for(let i=0; i<object.colors.length; i++){
				if(object.colors[i].default){
					return object.colors[i].id;
				}
			}
		},

		getPrice(object){
			for(let i=0; i<object.length; i++){
				if(object[i].default){
					return this.formatPrice(object[i].price);
				}
			}
		},

		selectSort(id, name){

			this.sort.activeName = name;
			this.sort.active = this.sort.active ? false : true;

			switch(id){

				case 1:
					this.objects.sort(function(a, b){

						if(a.name < b.name){
							return -1;
						}
						if(a.name > b.name){
							return 1;
						}

					})
					break;

				case 2:
					this.objects.sort(function(a, b){

						if(a.name < b.name){
							return -1;
						}
						if(a.name > b.name){
							return 1;
						}

					}).reverse()
					break;

				case 3:
					this.objects.sort(function(a, b){
						return a.price - b.price;
					})
					break;
				case 4:
					this.objects.sort(function(a, b){
						return b.price - a.price;
					})
					break;
			}



		},

	    formatPrice(value) {
	        let val = (value/1);
	        return val.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".")
	    }

	}

}

</script>
