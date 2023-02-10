import Vue from 'vue'
import App from './App.vue'
import store from './store'

Vue.config.productionTip = false

//require("@/assets/header.css");

new Vue({
	store,
	created() {
    	store.dispatch('loadData')
	},
	render: h => h(App)
}).$mount('#header-app')
