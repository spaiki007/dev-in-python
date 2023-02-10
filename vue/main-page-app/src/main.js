import Vue from 'vue'
import App from './App.vue'
import store from './store'

import VueAwesomeSwiper from 'vue-awesome-swiper'
import 'swiper/dist/css/swiper.css'
Vue.use(VueAwesomeSwiper, /* { default global options } */)

Vue.config.productionTip = false

new Vue({
  	store,
  	created() {
    	store.dispatch('loadData')
	},
  	render: h => h(App)
}).$mount('#main-page-app')
