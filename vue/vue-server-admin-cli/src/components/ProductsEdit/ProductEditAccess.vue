<template>
    <div>

		<div class="add-acces">

			<div class="wrap_select_block">
				<div class="select_block">
					<div class="active_select form-control">{{ accessorie.text }}</div>
					<div class="change" @click="accessorie.active = !accessorie.active"><i class="fas fa-sort-down"></i></div>
				</div>
				<div v-if="accessorie.active" class="select_elements">
					<div v-for="obj in products" :key="obj.id" @click="addAcces(obj)" class="select_element">{{ obj.name }}</div>
				</div>
			</div>

		</div>

		<div class="accessories">
			<div v-for="obj in activeProducts" :key="obj.id" class="accessorie">
				<div class='name'>{{ obj.name }}</div>
				<div class='delete-acces' @click="delAcces(obj)">отвязать</div>
			</div>
		</div>

        <div v-if="statusm == 0" class="message">{{ message }}</div>
        <div v-else-if="statusm == -1" class="message alert-danger">{{ message }}</div>
        <div v-else="statusm == 1" class="message alert-success">{{ message }}</div>

    </div>
</template>


<script>

    export default {

        data(){
    		return {

				activeProducts: [],
				products: 		[],
				assoc: 			[],

				accessorie: {
					name: "Акссесуары",
					text: "Выберите акссесуар...",
					active: false,
				},

                statusm: 0,
                message: "",
    		}
    	},

        mounted: function (){
            this.$nextTick(function(){
				this.init();
            });
        },

        methods: {

			addAcces: function(object){

				let o = this;
				let data = new FormData();

				data.append("parent", o.$route.params.id);
				data.append("pid", object.id);

				axios.post(o.$store.state.domain + "/accessories/add", data).then(function(response){
					o.statusm = 1;
					o.message = "Добавил...";
					o.init();

				}).catch(function (error){
					o.statusm = -1;
					o.message = "Неизвестная ошибка!";
				});

			},

			delAcces: function(object){

				let o = this;

				let id = 0;
				for(let k=0; k<o.assoc.length; k++){
					if(object.id == o.assoc[k].pid){
						id = o.assoc[k].id
					}
				}

				axios.post(o.$store.state.domain + "/accessories/" + id + "/delete").then(function(response){
					o.init();
				}).catch(function (error){
					console.log(error);
				});

			},

			init(){
				let o = this;

				//загружаем продукты
				axios.get(o.$store.state.domain + '/products/get').then(function(response){
					o.products = JSON.parse(response.data.objects);

					//загружаем ассоциации
					axios.get(o.$store.state.domain + '/accessories/' + o.$route.params.id).then(function(response){
						o.assoc = JSON.parse(response.data.objects);

						//удаляем редактируемый товар из списка
						for(let i=0; i<o.products.length; i++){
							if(o.products[i].id == o.$route.params.id){
								o.products.splice(i, 1);
							}
						}

						let temp = [];

						//добавляем товары в активный список, удаляем товары из общего списка
						for(let k=0; k<o.assoc.length; k++){
							for(let i=0; i<o.products.length; i++){
								if(o.products[i].id == o.assoc[k].pid){
									temp.push(o.products[i]);
									o.products.splice(i, 1);
								}
							}
						}

						o.activeProducts = temp;

					}).catch(function (error){
						console.log(error);
					});

				}).catch(function (error){
					console.log(error);
				});

			},


        }

    }
</script>
