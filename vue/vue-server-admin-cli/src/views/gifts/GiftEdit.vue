<template>
    <div>
        <h2>Изменение подарка</h2>
        <form class="form" action="." method="post" accept-charset="utf-8">
            <div id="tab" class="demo">

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

                <button type="submit" class="btn btn-primary sub" v-on:click.prevent="editObject">Изменить</button>

            </div>
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
				parent:		"",
				poster:		"",

				statusm: 0,
				message: "",
    		}
    	},

        mounted: function (){
            this.$nextTick(function(){

                let o = this;

                axios.get(o.$store.state.domain + '/gifts/' + o.$route.params.id).then(function(response){

                    o.name      	= response.data.name;
                    o.poster   		= response.data.img;
					o.parent 		= response.data.parent;

					axios.get(o.$store.state.domain + '/stocks/get').then(function(response){
						o.stock.objects = JSON.parse(response.data.objects);
						for(let i=0; i<o.stock.objects.length; i++){
							if(o.stock.objects[i].id == o.parent){
								o.stock.object = o.stock.objects[i].id;
								o.stock.text = o.stock.objects[i].name;
							}
						}

					}).catch(function(error){
						console.log(error);
					});

                }).catch(function (error){
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

            editObject: function(){

                let o       = this;
                let data    = new FormData();

                data.append("name", o.name);
    			data.append("poster", o.poster);
				data.append("parent", o.stock.object);

                axios.post(o.$store.state.domain + '/gifts/' + o.$route.params.id + '/update', data).then(function(response){
                    if(response.data.response){
                        o.statusm = 1;
                        o.message = "Изменен!";
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
