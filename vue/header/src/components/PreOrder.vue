<template>
	<div class="basket-block">
		<h1 class="order-name order-name-basket">Корзина</h1>

		<div class="basket">

			<div v-for="object in $store.state.data" :key="object.cid" class="basket-wrap-product-order">
				<div class="product-order">
					<div class="wrap-order-block-3">
						<div class="product-order-img-block">
							<div class="del-products-bascket x320" @click="deleteProducts(object.cid)">
								<img :src="$store.state.domain + '/static/img/del-basket-product.png'">
							</div>
							<img class="product-order-img" :src="object.product.image">
						</div>

						<div class="wrap-order-block-1">
							<a :href="$store.state.domain + '/shop/products/' + object.product.slug" class="product-order-name">{{ object.product.name }}</a>
							<div class="product-order-rating">
								<div class="product-rating">
									<img class="star" :src="$store.state.domain + '/static/img/raiting-fill.png'">
									<img class="star" :src="$store.state.domain + '/static/img/raiting-fill.png'">
									<img class="star" :src="$store.state.domain + '/static/img/raiting-fill.png'">
									<img class="star" :src="$store.state.domain + '/static/img/raiting-fill.png'">
									<img class="star" :src="$store.state.domain + '/static/img/raiting.png'">
								</div>
							</div>
							<div class="product-order-price">
								<div class="product-price">{{ formatPrice(object.product.price) }} руб.</div>
							</div>
						</div>
					</div>


					<div class="wrap-order-block-2">
						<div class="product-order-count-block">
							<div class="product-order-count-name">
								количество
							</div>
							<div class="product-order-count">
								<div class="product-order-count-sub" @click="object.product.count = object.product.count > 1 ? object.product.count - 1 : 1">
									<img :src="$store.state.domain + '/static/img/order-product-sub.png'">
								</div>
								<div class="product-order-count-count">
									<input v-model="object.product.count" class="product-order-count-input">
								</div>
								<div class="product-order-count-add" @click="object.product.count += 1">
									<img :src="$store.state.domain + '/static/img/order-product-basket-add.png'">
								</div>
							</div>
						</div>

						<div class="product-order-price-all-block">
							<div class="product-price-all-name">Стоимость</div>
							<div class="product-price-all">{{ productGetAllPrice(object) }} руб.</div>
						</div>
					</div>

					<div class="del-products-bascket x1200" @click="deleteProducts(object.cid)">
						<img :src="$store.state.domain + '/static/img/del-basket-product.png'">
					</div>

				</div>
			</div>

		</div>

		<div class="result-order-block">
			<div class="result-order-name">
				Итого: {{ resultPrice() }} руб.
			</div>

			<div class="result-order-button" @click="$parent.componentsViews(2)">
				<div class="wrap-callback" @mouseover="buttonIsActive = true" @mouseout="buttonIsActive = false">
					<div :class="['callback-background', {active: buttonIsActive}]">
						<div class="wrap-callback-background"></div>
					</div>
					<div class="callback">
						<div class="callback-name">Оформить заказ</div>
					</div>
				</div>
			</div>

		</div>
	</div>
</template>

<script>

import axios from 'axios';

export default {

	data: function(){
		return {
			buttonIsActive: false,
		}
	},


	methods: {

		deleteProducts(id){
			let o = this;
			axios.get(o.$store.state.domain + '/shop/products/del-basket-products?id=' + id).then(function(response){
				axios.get(o.$store.state.domain + '/shop/products/get-basket').then(function(response){
					o.$store.commit('updateData', JSON.parse(response.data.response));
				}).catch(function (error){
					console.log(error);
				});

			}).catch(function (error){
				console.log(error);
			});
		},

		resultPrice(){
			let temp = 0
			for(let i=0; i<this.$store.state.data.length; i++){
				temp += this.$store.state.data[i].product.count * this.$store.state.data[i].product.price;
			}
			return this.formatPrice(temp)
		},

		productGetAllPrice(o){
			return this.formatPrice(o.product.price * o.product.count);
		},

		formatPrice(value) {
	        let val = (value/1);
	        return val.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".");
	    }

	}

}
</script>
