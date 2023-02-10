<template>
  <div class="callback-block">
	  <div class="callback-back"></div>
	  <div class="callback-form-block">

		  	<div class="callback-form">

				<div class="callback-messge" v-if="message">Заявка оформлена, ожидайте звонка оператора.</div>

				<div class="callback-form-head" @click="$parent.close()">
					<div class="name">Обратный звонок</div>
					<img :src="$store.state.domain + '/static/img/close.png'">
				</div>

				<div class="icon-border"></div>

				<div class="order-form-input-block">
					<div class="order-form-input-head">
						<div class="order-form-input-name">
							Имя *
						</div>
						<div class="order-form-input-check">
							<img v-if="checkForms.name" class="social" :src="$store.state.domain + '/static/img/order-check.png'">
							<img v-else class="social" :src="$store.state.domain + '/static/img/order-uncheck.png'">
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
							<img v-if="checkForms.phone" class="social" :src="$store.state.domain + '/static/img/order-check.png'">
							<img v-else class="social" :src="$store.state.domain + '/static/img/order-uncheck.png'">
						</div>
					</div>
					<div class="wrap-order-form-input">
						<input v-model="phone" class="order-form-input" placeholder="например +7(999)-999-99-99">
					</div>
				</div>

				<div class="order-form-input-block">
					<div class="order-form-input-name">Время звонка</div>
					<div class="wrap-order-form-input">
						<input v-model="call_time" class="order-form-input" placeholder="например 10:00">
					</div>
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
	data: function(){
		return {
			name: 	'',
			phone: 	'',
			call_time:	'',

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

			data.append("name", o.name);
			data.append("phone", o.phone);
			data.append("call_time", o.call_time);

			axios.post(o.$store.state.domain + '/shop/callback', data).then(function(response){
				console.log(response.data);
			}).catch(function (error){
				console.log(error);
			});

		},

	}



}
</script>
