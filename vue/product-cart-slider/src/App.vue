<template>
  <div id="slider-app">
	  <slider-components v-if="acessories.length" :domain="domain" component-name="Аксессуары" :char="false" :objects="acessories"></slider-components>
	  <slider-components v-if="similarProducts.length" :domain="domain" component-name="Похожие товары" :char="true" :objects="similarProducts"></slider-components>
  </div>
</template>

<script>

import axios from 'axios';
import Slider from './components/Slider.vue'

export default {
	name: 'slider-app',

	components: {
		'slider-components': Slider,
	},

	data (){
		return {
			//domain: 			'http://localhost',
			domain: 			'',
			acessories: 		[],
			similarProducts: 	[],
			productSlug: 		'',
		}
	},

	mounted (){
		this.$nextTick(function(){

			let o = this;

			let path = window.location.pathname.split('/');
			o.productSlug = path[path.length-1];

			axios.get(o.domain + '/shop/product-slider-get?slug=' + o.productSlug).then(function(response){
				o.acessories = JSON.parse(response.data.objects);

				axios.get(o.domain + '/shop/similar-products?slug=' + o.productSlug).then(function(response){
					o.similarProducts = JSON.parse(response.data.objects);
				}).catch(function (error){
					console.log(error);
				});

			}).catch(function (error){
				console.log(error);
			});


		})
	},

	methods: {

	}

}
</script>
