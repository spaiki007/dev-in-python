<template>
  <div class="callback-block">
	  <div class="callback-back"></div>
	  <div class="callback-form-block color-window">
		  	<div class="callback-form">
				<div class="callback-form-head" @click="$emit('close-color')">
					<div class="name">Выберите цвет</div>
					<img :src="domain + '/static/img/close.png'">
				</div>

				<div class="icon-border"></div>

				<div class="order-form-input-block">
					<div v-for="obj in product.colors" :key="obj.id" class="select_element" @click="addBasket(obj.id)">
						<div class="active_select form-control active" :style="getBack(obj)"></div>
						{{ obj.name }}
					</div>
				</div>

			</div>

	  </div>
  </div>
</template>

<script>

import axios from 'axios';

export default {
	props: ['product'],

	data (){
		return {
			domain:		'http://localhost',
			//domain: "",
		}
	},

	methods: {

		getBack(object){

			if(object.poster == ""){
				return {'background': object.code};
			}
			return {'background-image': "url('" + object.poster + "')"};

		},

		addBasket(id){
			let o = this;

			let data = new FormData();
			data.append("order", JSON.stringify({id: id, giftID: '', optionIDS: []}));
			axios.post(o.domain + '/shop/products/add-basket', data).then(function(response){
				location.reload();
			}).catch(function (error){
				console.log(error);
			});
			this.$emit('close-color');

		},

	}



}
</script>
