<template>
  <div class="callback-block">
	  <div class="callback-back"></div>
	  <div class="callback-form-block">

		  	<div class="callback-form">

				<div class="callback-messge" v-if="message">Заявка оформлена, ожидайте звонка оператора.</div>

				<div class="callback-form-head" @click="$parent.close()">
					<div class="name">Быстрый заказ товара</div>
					<img :src="domain + '/static/img/close.png'">
				</div>

				<div class="icon-border"></div>

				<div class="order-form-input-block">
					<div class="order-form-input-head">
						<div class="order-form-input-name">Доступные цвета для товара</div>
					</div>
					<div class="wrap_select_block">
						<div class="select_block" @click="color.active = true">
							<div class="select-block-wrap-name">
								<div class="active_select form-control active" :style="color.img"></div>
								<div class="active_select form-control">{{ color.text }}</div>
							</div>
							<div class="change"><img :src="domain + '/static/img/arrow-top-bottom.png'"></div>
						</div>
						<div v-if="color.active" class="select_elements">
							<div v-for="obj in color.objects" :key="obj.id" @click="changeColor(obj)" class="select_element">
								<div class="active_select form-control active" :style="getBack(obj)"></div>
								{{ obj.name }}
							</div>
						</div>
					</div>
				</div>

				<div class="order-form-input-block">
					<div class="order-form-input-head">
						<div class="order-form-input-name">
							Имя *
						</div>
						<div class="order-form-input-check">
							<img v-if="checkForms.name" class="social" :src="domain + '/static/img/order-check.png'">
							<img v-else class="social" :src="domain + '/static/img/order-uncheck.png'">
						</div>
					</div>
					<div class="wrap-order-form-input">
						<input v-model="name" class="order-form-input" placeholder="Степан">
					</div>
				</div>

				<div class="order-form-input-block">
					<div class="order-form-input-head">
						<div class="order-form-input-name">
							Телефон *
						</div>
						<div class="order-form-input-check">
							<img v-if="checkForms.phone" class="social" :src="domain + '/static/img/order-check.png'">
							<img v-else class="social" :src="domain + '/static/img/order-uncheck.png'">
						</div>
					</div>
					<div class="wrap-order-form-input">
						<input v-model="phone" class="order-form-input" placeholder="например +7(999)-999-99-99">
					</div>
				</div>

				<div class="order-form-input-block">
					<div class="order-form-input-name">Комментарий</div>
					<div class="order-form-textarea-block"><div class="wrap-order-form-textarea"><textarea placeholder="Просьба курьеру позвонить перед доставкой." class="order-form-textarea"></textarea></div></div>
				</div>

				<div :class="['send-request', {active: checkForms.name && checkForms.phone}]" @click="createCallbaks">
					<div class="wrap-callback">
						<div class="callback-background">
							<div class="wrap-callback-background"></div>
						</div>
						<div class="callback">
							<div class="callback-name">Заказать</div>
						</div>
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

			color: {
				img:			this.getBack(this.product.colors[0]),
				active: 		false,
				text: 			this.product.colors[0].name,
				object:			this.product.colors[0].id,
				objects:		this.product.colors,
			},

			domain:		'http://localhost',
			//domain: "",

			name: 		'',
			phone: 		'',
			comments:	'',

			checkForms: {
				name: false,
				phone: false,
			},

			message: false,

		}
	},

	watch: {

		name: function (val) {
			if(val.length){
				this.checkForms.name = true;
			}else{
				this.checkForms.name = false;
			}
		},

		phone: function (val) {
			if (val.replace(/\D+/ig, '').length == 11){
				this.checkForms.phone = true;
			}else{
				this.checkForms.phone = false;
			}
		},

	},

	methods: {

		getBack(object){

			if(object.poster == ""){
				return {'background': object.code};
			}
			return {'background-image': "url('" + object.poster + "')"};

		},

		//меняем цвет
        changeColor: function(obj){
			this.color.img 		= this.getBack(obj);
			this.color.object 	= obj.id;
			this.color.active 	= false;
			this.color.text 	= obj.name;
		},

		close (){
			this.$parent.close();
			o.message = false;
		},

		createCallbaks(){
			let o = this;

			if(!(o.checkForms.name && o.checkForms.phone)){
				return false;
			}

			o.message = true;

			let data = new FormData();

			data.append("pid", o.product.id);
			data.append("cid", o.color.object);
			data.append("name", o.name);
			data.append("phone", o.phone);
			data.append("comments", o.comments);

			axios.post(o.domain + '/shop/quick-order', data).then(function(response){
				console.log(response.data);
			}).catch(function (error){
				console.log(error);
			});

		},

	}



}
</script>
