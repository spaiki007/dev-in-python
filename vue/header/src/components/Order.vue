<template>
	<div class="page-order">

			<h1 class="order-name">Оформление заказа</h1>

			<div class="wrap-wrap-order-form-block">

				<div class="wrap-order-form-block">
					<div class="order-form-block">

						<div class="wrap-order-form-head">
							<div class="order-form-name">Персональные данные</div>
							<div class="icon-border"></div>
							<div class="order-form-warning">* поля, обязательные для заполнения</div>
						</div>

						<div class="icon-border x1200"></div>

						<div class="wrap-order-form-input-block">
							<div class="order-form-input-block">
								<div class="order-form-input-head">
									<div class="order-form-input-name">Имя *</div>
									<div :class="['input-chek', {active: checkForms.firtName}]"></div>
								</div>
								<div class="wrap-order-form-input">
									<input v-model="firtName" class="order-form-input" placeholder="Степан">
								</div>
							</div>

							<div class="order-form-input-block">
								<div class="order-form-input-head">
									<div class="order-form-input-name">Фамилия *</div>
									<div :class="['input-chek', {active: checkForms.lastName}]"></div>
								</div>
								<div class="wrap-order-form-input">
									<input v-model="lastName" class="order-form-input" placeholder="Иванов">
								</div>
							</div>
							<div class="order-form-input-block">
								<div class="order-form-input-head">
									<div class="order-form-input-name">Телефон*</div>
									<div :class="['input-chek', {active: checkForms.phone}]"></div>
								</div>
								<div class="wrap-order-form-input">
									<input v-model="phone" class="order-form-input" placeholder="+7 (999) 999 99 99">
								</div>
							</div>

							<div class="order-form-input-block">
								<div class="order-form-input-head">
									<div class="order-form-input-name">E-mail *</div>
									<div :class="['input-chek', {active: checkForms.email}]"></div>
								</div>
								<div class="wrap-order-form-input">
									<input v-model="email" class="order-form-input" placeholder="stepan@ivanov.ru">
								</div>
							</div>
						</div>
					</div>

					<div class="order-form-block">

						<div class="wrap-order-form-head">
							<div class="order-form-name">Адрес доставки</div>
							<div class="icon-border"></div>
							<div class="order-form-warning">* поля, обязательные для заполнения</div>
						</div>
						<div class="icon-border x1200"></div>
						<div class="order-form-input-block">
							<div class="order-form-input-head">
								<div class="order-form-input-name">Адрес *</div>
								<div :class="['input-chek', {active: checkForms.adress}]"></div>
							</div>
							<div class="wrap-order-form-input">
								<input v-model="adress" class="order-form-input" placeholder="ул. Вторая Советская, д. 95, кв. 757">
							</div>
						</div>

					</div>

					<div class="order-form-block">
						<div class="order-form-name x768">Способ оплаты</div>
						<div class="icon-border"></div>
						<div class="wrap-order-form-radio-block">
							<div v-for="method in paymentMethod" :key="method.id" class="order-form-radio-block" @click="changePayment(method.id)">
								<div class="order-form-radio-icon">
									<div :class="['order-form-radio-icon-inset', {check: method.active}]"></div>
								</div>
								<div class="order-form-radio-name">{{ method.name }}</div>
							</div>
						</div>

					</div>

					<div class="order-form-block">
						<div class="order-form-name x768">Способ доставки</div>
						<div class="icon-border"></div>
						<div class="wrap-order-form-radio-block">
							<div v-for="method in deliveryMethod" :key="method.id" class="order-form-radio-block" @click="changeDelivery(method.id)">
								<div class="order-form-radio-icon">
									<div :class="['order-form-radio-icon-inset', {check: method.active}]"></div>
								</div>
								<div class="order-form-radio-name">{{ method.name }}</div>
							</div>
						</div>
					</div>
					<div class="order-form-block">
						<div class="order-form-name x768">
							Комментарий к заказу
						</div>
						<div class="icon-border"></div>
						<div class="order-form-textarea-block">
							<div class="wrap-order-form-textarea">
								<textarea v-model="comment" class="order-form-textarea" placeholder="Просьба курьеру позвонить перед доставкой."></textarea>
							</div>
						</div>
					</div>

					<div class="place-order-block">

						<div class="wrap-callback return-pre-order" @click="$parent.componentsViews(1)">
							<div class="callback-background">
								<div class="wrap-callback-background"></div>
							</div>
							<div class="callback">
								<div class="callback-name">Вернуться в корзину</div>
							</div>
						</div>

						<div class="wrap-callback" @click="orderRegistration" v-if="checkForms.firtName && checkForms.lastName && checkForms.adress && checkForms.email && checkForms.phone">
							<div class="callback-background">
								<div class="wrap-callback-background"></div>
							</div>
							<div class="callback">
								<div class="callback-name">Оформить заказ</div>
							</div>
						</div>
						<div class="wrap-callback"v-else>
							Заполните все поля помеченные звездочкой.
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

			firtName: 	'',
			lastName: 	'',
			phone:		'',
			email:		'',
			adress:		'',
			comment:	'',

			checkForms: {
				firtName: false,
				lastName: false,
				phone: false,
				email: false,
				adress: false,
			},

			paymentMethod: [
				{id: 1, name: 'Наличные курьеру', active: true},
				{id: 2, name: 'Картой на сайте', active: false},
				{id: 3, name: 'Картой курьеру', active: false},
				{id: 4, name: 'Яндекс.Деньги/Visa/Mastercard', active: false},
			],

			deliveryMethod: [
				{id: 1, name: 'Самовывоз', active: true},
				{id: 2, name: 'Курьер', active: false},
				{id: 3, name: 'Транспортная компания', active: false},
				{id: 4, name: 'Почта России', active: false},
			],

		}
	},

	watch: {

		firtName: function (val) {
			this.checkForms.firtName = val.length ? true : false;
		},

		lastName: function (val) {
			this.checkForms.lastName = val.length ? true : false;
		},

		adress: function (val) {
			this.checkForms.adress = val.length ? true : false;
		},

		email: function (val) {
			this.checkForms.email = val.length ? true : false;
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

		changePayment(id){
			for(let i=0; i<this.paymentMethod.length; i++){
				if(this.paymentMethod[i].id == id){
					this.paymentMethod[i].active = true;
				}else{
					this.paymentMethod[i].active = false;
				}
			}
		},

		changeDelivery(id){
			for(let i=0; i<this.deliveryMethod.length; i++){
				if(this.deliveryMethod[i].id == id){
					this.deliveryMethod[i].active = true;
				}else{
					this.deliveryMethod[i].active = false;
				}
			}
		},

		orderRegistration(){
			let o = this;

			o.$parent.componentsViews(3);

			if(!(o.checkForms.firtName && o.checkForms.lastName && o.checkForms.adress && o.checkForms.email && o.checkForms.phone)){
				return false;
			}

			let data = new FormData();

			data.append("firtName", o.firtName);
			data.append("lastName", o.lastName);
			data.append("phone", o.phone);
			data.append("email", o.email);
			data.append("adress", o.adress);
			data.append("comment", o.comment);

			for(let i=0; i<o.paymentMethod.length; i++){
				if(o.paymentMethod[i].active){
					data.append("payment", o.paymentMethod[i].name);
					break;
				}
			}

			for(let i=0; i<o.deliveryMethod.length; i++){
				if(o.deliveryMethod[i].active){
					data.append("delivery", o.deliveryMethod[i].name);
					break;
				}
			}

			let articles = [];
			for(let i=0; i<o.$store.state.data.length; i++){
				articles.push({
					id: o.$store.state.data[i].articleID,
					count: o.$store.state.data[i].product.count,
				});
			}
			data.append("products", JSON.stringify(articles));

			axios.post(o.$store.state.domain + '/shop/products/order', data).then(function(response){
				console.log(response.data);
				o.$store.commit('updateData', []);
			}).catch(function (error){
				console.log(error);
			});

		},


	}

}
</script>
