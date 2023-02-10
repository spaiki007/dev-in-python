import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
	state: {
	  domain: "",
	  data: {},
	},
	mutations: {
		updateData(state, data){
			state.data = data;
		},
	},
	actions: {
		loadData({state, commit}){
			axios.get(state.domain + '/shop/products/get-basket').then((response) => {
				let data = JSON.parse(response.data.response);
				commit('updateData', data);
			});
		}
	}
})
