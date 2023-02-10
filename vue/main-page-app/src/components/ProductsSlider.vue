<template>

	<div class="main-category-products-action-block">

		<callback v-if="quickOrderOpen" :close="close" :product="activeProduct"></callback>
		<addbasket v-if="color.active" @close-color="closeColor" :product="color.product"></addbasket>

		<div class="wrap-main-category-products">
			<div class="wrap-wrap-wrap-main-category-products">
				<div class="wrap-wrap-main-category-products">
					<div class="main-category-arrow-left click-arrow-left">
						<img :src="domain + '/static/img/arrow-left.png'">
					</div>
					<div class="main-category-products-top">
						<div class="main-category-products-top-name">{{ componentName }}</div>
					</div>
					<div class="main-category-arrow-right click-arrow-right">
						<img :src="domain + '/static/img/slider-arrow-right.png'">
					</div>
				</div>
				<div class="all-categories-count green">{{ objects.length }}</div>
			</div>
			<div class="wrap-wrap-arrow-desc">
				<img class="arrow-desc arrow-left-desctop click-arrow-left" :src="domain + '/static/img/arrow-left-desctop.png'">
				<img class="arrow-desc arrow-right-desctop click-arrow-right" :src="domain + '/static/img/arrow-right-desctop.png'">
			</div>
		</div>

		<div class="main-action-category-products">

	      <!-- swiper -->
		  <swiper :options="swiperOption" class="products">
			  <swiper-slide v-for="object in objects" :key="object.id">
				  <div class="product">
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


							<div class="product-block-3" v-if="char">

								<div v-for="(characteristic, item) in object.characteristics" :key="characteristic.id" v-if="item < 3" class="characteristic">
									<div class="product-parameter-name">{{ characteristic.key }}</div>
									<div class="product-parameter-key">{{ characteristic.value }}</div>
								</div>

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
				</swiper-slide>
			</swiper>

		</div>
	</div>

</template>

<script>

import axios from 'axios';
import Callback from './Callback.vue'
import AddBasket from './AddBasket.vue'

export default {

	props: ['domain', 'component-name', 'char', 'objects'],
	components: {
		'callback': Callback,
		'addbasket': AddBasket,
	},
	data(){
		return {
			color: {
				active: false,
				product: false,
			},

			activeProduct: false,
			quickOrderOpen: false,

			swiperOption: {
				slidesPerView: 4,
				spaceBetween: 40,
		        loop: true,
		        loopFillGroupWithBlank: true,

				navigation: {
					nextEl: '.click-arrow-right',
					prevEl: '.click-arrow-left',
				},

				breakpoints: {
					1200: {slidesPerView: 4, spaceBetween: 20},
		            1110: {slidesPerView: 3, spaceBetween: 20},
		            850: {slidesPerView: 2, spaceBetween: 20},
					575: {slidesPerView: 1, spaceBetween: 20},

		       	}

			},
		}
	},

	methods: {

		openColor(object){

			let o = this;

			if(object.colors.length > 1){
				o.color.active = true;
				o.color.product = object;
			}else{
				let data = new FormData();
				data.append("order", JSON.stringify({id: object.colors[0].id, giftID: '', optionIDS: []}));
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

		getBack(object) {
			if(object.img == ""){
				return {'background': object.code};
			}
			return {'background-image': "url('" + object.img + "')"};
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


	},
}
</script>
