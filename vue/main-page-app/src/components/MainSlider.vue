<template>
	<div class="slider-block">

		<div class="slider-categories">

			<a v-for="(category, item) in $store.state.categories" :key="category.id" v-if="item < lastElements" :href="'/shop/categories/' + category.slug" class="category-block">
				<div class="wrap-icon">
					<div class="icon" v-html="category.svg"></div>
					<div class="category-name">{{ category.name }}</div>
				</div>
				<div class="icon-border" v-if="item < lastElements-1"></div>
				<img :src="$store.state.domain + '/static/img/slider-arrow-right.png'" class="category-block-arrow-right">
			</a>

			<div class="category-block all-categories" @click="setLastElements">
				<div class="all-categories-name">{{ getNameAllCatalog() }}</div>
			</div>

		</div>

		<div class="slider-content">
			<div class="slider-content-top">
				<div class="slider-content-top-left">
					<div class="slider-content-top-name">{{ slider.name }}</div>

					<div class="slider-content-top-border">
						<img :src="$store.state.domain + '/static/img/slider-bottom.png'">
					</div>
					<div class="slider-content-top-pre">{{ slider.desc }}</div>

					<div class="slider-content-top-nav">
						<div v-for="object in $store.state.sliders" :key="object.id" @click="setSlider(object.id)" class="wrap-slider-content-top-nav-icon">
							<div class="slider-content-top-nav-icon active">
								<div></div>
							</div>
						</div>

					</div>
				</div>
				<div class="slider-content-top-right">

					<div class="slider-content-top-right-image">
						<img :src="slider.poster">
					</div>

					<div class="slider-content-top-right-bottom">
						<div class="slider-content-top-right-price">
							{{ slider.price }} руб.
						</div>
						<div class="slider-content-top-right-detail">

							<a :href="slider.link" class="wrap-callback">
								<div class="callback-background">
									<div class="wrap-callback-background"></div>
								</div>
								<div class="callback">
									<div class="callback-name">Подробнее о товаре</div>
								</div>
							</a>

						</div>
					</div>

				</div>
			</div>

			<div class="main-mobile-slider-advantage">
				<hooper>
				    <slide v-for="advantage in advantageBlock" class="advantage-main-slider">
						<div class="slider-content-bot-advantage x320">
	  	  					<div class="advantage-img">
	  	  						<img :src="advantage.img">
	  	  					</div>
	  	  					<div class="advantage-name">{{ advantage.name }}</div>
	  	  					<div class="advantage-content">{{ advantage.desc }}</div>
	  	  				</div>
				    </slide>
					<hooper-navigation slot="hooper-addons"></hooper-navigation>
				</hooper>
			</div>


			<div class="slider-content-bot">

				<div v-for="advantage in advantageBlock" class="slider-content-bot-advantage x768">
					<div class="advantage-img">
						<img :src="advantage.img">
					</div>
					<div class="advantage-name">{{ advantage.name }}</div>
					<div class="advantage-content">{{ advantage.desc }}</div>
				</div>

			</div>
		</div>
	</div>
</template>

<script>

import {Hooper, Slide, Navigation as HooperNavigation} from 'hooper';
import 'hooper/dist/hooper.css';


export default {
	name: 'MainSlider',

	components: {Hooper, Slide, HooperNavigation},

	data () {
		return {
			lastElements: 	8,
			lastElment:		false,

			slider: {
				name: 	"",
				desc: 	"",
				link:	"",
				price: 	"",
				poster: "",
			},

			advantageBlock: [
				{
					img: 	this.$store.state.domain + "/static/img/advantage-1.png",
					name:	"Качественный товар",
					desc:	"Собственные поставки напрямую от производителя",
				},
				{
					img: 	this.$store.state.domain + "/static/img/advantage-2.png",
					name:	"Удобная доставка",
					desc:	"Сделали заказ до 20.00? Доставим завтра",
				},
				{
					img: 	this.$store.state.domain + "/static/img/advantage-3.png",
					name:	"Лучшая цена",
					desc:	"Мы гарантируем лучшее соотношение цена и качества",
				},
				{
					img: 	this.$store.state.domain + "/static/img/advantage-4.png",
					name:	"Гарантия на товары",
					desc:	"Обычная — 12 месяцев, расширенная — на 3 года",
				},
			],


		}
	},

	mounted (){
        this.$nextTick(function(){

        });
    },

	computed: {
		countSlider(){
			return this.$store.state.sliders.length;
		}
	},

	watch: {
		countSlider(){
			this.initSlider();
		}
	},

	methods: {

		setSlider(id){
			for(let i=0; i<this.$store.state.sliders.length; i++){
				if(this.$store.state.sliders[i].id == id){
					this.slider.name 	= this.$store.state.sliders[i].name;
					this.slider.desc 	= this.$store.state.sliders[i].desc;
					this.slider.link 	= this.$store.state.sliders[i].link;
					this.slider.price 	= this.$store.state.sliders[i].price;
					this.slider.poster 	= this.$store.state.sliders[i].poster;
				}
			}
		},

		initSlider(){
			let firstSlider = this.$store.state.sliders[0];

			this.slider.name = firstSlider.name;
			this.slider.desc = firstSlider.desc;
			this.slider.link = firstSlider.link;
			this.slider.price = firstSlider.price;
			this.slider.poster = firstSlider.poster;
		},

		setLastElements(){
			this.lastElment = !this.lastElment;
			this.lastElements = this.lastElment ? this.$store.state.categories.length : 8;
		},

		getNameAllCatalog(){
			return this.lastElment ? "Только популярные" : "Весь каталог";
		},

	},

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

@font-face {
	font-family: 'OpenSans';
	src: url('../static/fonts/open-sans/OpenSans.eot');
	src: url('../static/fonts/open-sans/OpenSans.eot?#iefix') format('embedded-opentype'),
	   url('../static/fonts/open-sans/OpenSans.svg#OpenSans') format('svg'),
	   url('../static/fonts/open-sans/OpenSans.ttf') format('truetype'),
	   url('../static/fonts/open-sans/OpenSans.woff') format('woff'),
	   url('../static/fonts/open-sans/OpenSans.woff2') format('woff2');
	font-weight: normal;
	font-style: normal;
}

@font-face {
	font-family: 'OpenSans-Light';
	src: url('../static/fonts/open-sans-light/OpenSans-Light.eot');
	src: url('../static/fonts/open-sans-light/OpenSans-Light.eot?#iefix') format('embedded-opentype'),
	   url('../static/fonts/open-sans-light/OpenSans-Light.svg#OpenSans-Light') format('svg'),
	   url('../static/fonts/open-sans-light/OpenSans-Light.ttf') format('truetype'),
	   url('../static/fonts/open-sans-light/OpenSans-Light.woff') format('woff'),
	   url('../static/fonts/open-sans-light/OpenSans-Light.woff2') format('woff2');
	font-weight: normal;
	font-style: normal;
}

@font-face {
	font-family: 'OpenSans-Semibold';
	src: url('../static/fonts/open-sans-semibold/OpenSans-Semibold.eot');
	src: url('../static/fonts/open-sans-semibold/OpenSans-Semibold.eot?#iefix') format('embedded-opentype'),
		url('../static/fonts/open-sans-semibold/OpenSans-Semibold.svg#OpenSans-Semibold') format('svg'),
		url('../static/fonts/open-sans-semibold/OpenSans-Semibold.ttf') format('truetype'),
		url('../static/fonts/open-sans-semibold/OpenSans-Semibold.woff') format('woff'),
		url('../static/fonts/open-sans-semibold/OpenSans-Semibold.woff2') format('woff2');
	font-weight: normal;
	font-style: normal;
}

@font-face {
	font-family: 'OpenSans-Bold';
	src: url('../static/fonts/open-sans-bold/OpenSans-Bold.eot');
	src: url('../static/fonts/open-sans-bold/OpenSans-Bold.eot?#iefix') format('embedded-opentype'),
	   url('../static/fonts/open-sans-bold/OpenSans-Bold.svg#OpenSans-Bold') format('svg'),
	   url('../static/fonts/open-sans-bold/OpenSans-Bold.ttf') format('truetype'),
	   url('../static/fonts/open-sans-bold/OpenSans-Bold.woff') format('woff'),
	   url('../static/fonts/open-sans-bold/OpenSans-Bold.woff2') format('woff2');
	font-weight: normal;
	font-style: normal;
}

@font-face {
	font-family: 'Geometria';
	src: url('../static/fonts/geometria/Geometria.eot');
	src: url('../static/fonts/geometria/Geometria.eot?#iefix') format('embedded-opentype'),
	   url('../static/fonts/geometria/Geometria.svg#Geometria') format('svg'),
	   url('../static/fonts/geometria/Geometria.ttf') format('truetype'),
	   url('../static/fonts/geometria/Geometria.woff') format('woff'),
	   url('../static/fonts/geometria/Geometria.woff2') format('woff2');
	font-weight: normal;
	font-style: normal;
}

@font-face {
	font-family: 'Geometria-Bold';
	src: url('../static/fonts/geometria-bold/Geometria-Bold.eot');
	src: url('../static/fonts/geometria-bold/Geometria-Bold.eot?#iefix') format('embedded-opentype'),
	   url('../static/fonts/geometria-bold/Geometria-Bold.svg#Geometria') format('svg'),
	   url('../static/fonts/geometria-bold/Geometria-Bold.ttf') format('truetype'),
	   url('../static/fonts/geometria-bold/Geometria-Bold.woff') format('woff'),
	   url('../static/fonts/geometria-bold/Geometria-Bold.woff2') format('woff2');
	font-weight: normal;
	font-style: normal;
}

:root {
	font-size: 0.75em;
	box-sizing: border-box;
}

*, ::before, ::after {
	box-sizing: inherit;
}

body {
	margin: 0;
	padding: 0;
	color: black;
	font-family: 'OpenSans', arial;
	overflow-x: hidden;
}

a {
	text-decoration: none;
}

</style>
