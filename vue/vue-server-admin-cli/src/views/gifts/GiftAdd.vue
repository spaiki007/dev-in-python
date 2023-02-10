<template>
    <div>
        <h2>Добавление подарка</h2>

        <form class="form" action="." method="post" accept-charset="utf-8">

			<div class="name">{{ stock.name }}</div>
			<div class="wrap_select_block">
				<div class="select_block">
					<div class="active_select form-control">{{ stock.text }}</div>
					<div class="change" @click="stock.active = stock.active ? false : true"><i class="fas fa-sort-down"></i></div>
				</div>
				<div v-if="stock.active" class="select_elements">
					<div v-for="obj in stock.objects" :key="obj.id" @click="changeStock(obj.id, obj.name)" class="select_element">{{ obj.name }}</div>
				</div>
			</div>

			<label for='name'>Наименование</label>
			<input v-model="name" id='name' class="form-control" name='name' type='text'/>

			<label for='poster'>Постер</label>
	        <div class="wrap-poster">
	            <a :href="poster" target="_blank">
	                <img :src="poster" class="activePoster">
	            </a>
				<div class="inputPoster">
					<input v-model="poster" class="form-control" type='text'/>
				</div>
	        </div>

            <div v-if="statusm == 0" class="message">{{ message }}</div>
            <div v-else-if="statusm == -1" class="message alert-danger">{{ message }}</div>
            <div v-else="statusm == 1" class="message alert-success">{{ message }}</div>

            <button type="submit" class="btn btn-primary sub" v-on:click.prevent="addObject">Добавить</button>

        </form>
    </div>
</template>


<script>


    export default {

        data: function(){
    		return {

				stock: {
					name:		"Выберите акцию",
                    active: 	false,
                    text: 		"Выберите акцию",
                    object:		0,
                    objects:	[],
                },

                name: 		"",
                poster:		"",

                statusm: 0,
                message: "",
    		}
    	},

		mounted: function (){
			this.$nextTick(function(){

				let o = this;

				axios.get(o.$store.state.domain + '/stocks/get').then(function(response){
					o.stock.objects = JSON.parse(response.data.objects);
				}).catch(function(error){
					console.log(error);
				});

			})
		},

    	methods: {

			changeStock: function(id, name){
				this.stock.object = id;
				this.stock.active = false;
				this.stock.text = name;
			},

    		addObject: function(){

    			let o    = this;
    			let data = new FormData();

                data.append("name", o.name);
    			data.append("poster", o.poster);
				data.append("parent", o.stock.object);

    			axios.post(o.$store.state.domain + window.location.pathname, data).then(function(response){

    				if(response.data.response){
						o.statusm = 1;
    					o.message = "Основная информация добавлена...";
    				}else{
    					o.statusm = -1;
    					o.message = response.data.err;
    				}

    			}).catch(function (error){
    				o.statusm = -1;
    				o.message = "Неизвестная ошибка!";
    			})

    		},

    	}

    }
</script>
