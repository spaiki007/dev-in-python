<template>
    <div>

		<div class="gifts">
			<div v-for="obj in pickings" :key="obj.id" :class="[obj.active ? 'gift-active' : 'gift']" @click="editPickings(obj)">{{ obj.name }}</div>
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

				pickings:	[],
				paps:		[],

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
					for(let k=0; k<o.paps.length; k++){
						if(object.id == o.paps[k].pic_id){
							id = o.paps[k].id
						}
					}

					axios.post(o.$store.state.domain + "/paps/" + id + "/delete").then(function(response){
						o.init();
					}).catch(function (error){
						console.log(error);
					});

				}else{

					let data = new FormData();

					data.append("pid", o.$route.params.id);
					data.append("pic_id", object.id);

					axios.post(o.$store.state.domain + "/paps/add", data).then(function(response){
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

				//загружаем комлектации
				axios.get(o.$store.state.domain + '/pickings/get').then(function(response){
					o.pickings = JSON.parse(response.data.objects);

					//загружаем ассоциации с комлектациями
					axios.get(o.$store.state.domain + '/paps/' + o.$route.params.id).then(function(response){
						o.paps = JSON.parse(response.data.objects);

						//инициализируем комлектации
						for(let i=0; i<o.pickings.length; i++){
							for(let k=0; k<o.paps.length; k++){
								if(o.pickings[i].id == o.paps[k].pic_id){
									o.pickings[i].active = true;
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
