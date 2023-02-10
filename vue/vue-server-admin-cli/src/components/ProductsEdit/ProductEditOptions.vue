<template>
    <div>

		<div class="gifts">
			<div v-for="obj in options" :key="obj.id" :class="[obj.active ? 'gift-active' : 'gift']" @click="editPickings(obj)">{{ obj.name }}</div>
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

				options:	[],
				oaps:		[],

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

			editPickings(object){

				let o = this;

				if(object.active){

					let id = 0;
					for(let k=0; k<o.oaps.length; k++){
						if(object.id == o.oaps[k].oid){
							id = o.oaps[k].id
						}
					}

					axios.post(o.$store.state.domain + "/oaps/" + id + "/delete").then(function(response){
						o.init();
					}).catch(function (error){
						console.log(error);
					});

				}else{

					let data = new FormData();

					data.append("pid", o.$route.params.id);
					data.append("oid", object.id);

					axios.post(o.$store.state.domain + "/oaps/add", data).then(function(response){
						o.statusm = 1;
						o.message = "Добавил...";
						o.init();

					}).catch(function (error){
						o.statusm = -1;
						o.message = "Неизвестная ошибка!";
					});
				}

			},

			init(){
				let o = this;

				//загружаем опции
				axios.get(o.$store.state.domain + '/options/get').then(function(response){
					o.options = JSON.parse(response.data.objects);

					//загружаем ассоциации с опции
					axios.get(o.$store.state.domain + '/oaps/' + o.$route.params.id).then(function(response){
						o.oaps = JSON.parse(response.data.objects);

						//инициализируем комлектации
						for(let i=0; i<o.options.length; i++){
							for(let k=0; k<o.oaps.length; k++){
								if(o.options[i].id == o.oaps[k].oid){
									o.options[i].active = true;
								}
							}
						}

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
