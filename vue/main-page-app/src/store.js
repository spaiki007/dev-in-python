import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({

	state: {
		domain: "http://localhost",

		categories: [],
		sliders: 	[],

		status:		false,

	},

	mutations: {
		updateData(state, data){
			state.categories = data.categories;
			state.sliders = data.sliders;
		},
	},

	actions: {
		loadData({state, commit}){
			axios.get(state.domain + '/get-main-json').then((response) => {
				commit('updateData', response.data);
			});
		}
	}

})
