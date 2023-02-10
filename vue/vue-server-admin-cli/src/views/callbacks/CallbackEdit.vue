<template>
    <div>
        <h2>Изменение обратного звонка</h2>
        <form class="form" action="." method="post" accept-charset="utf-8">

            <div id="tab" class="demo">

				<div class="name">Статус</div>
				<div class="wrap_select_block">
					<div class="select_block">
						<div class="active_select form-control">{{ order.text }}</div>
						<div class="change" @click="order.active = order.active ? false : true"><i class="fas fa-sort-down"></i></div>
					</div>
					<div v-if="order.active" class="select_elements">
						<div v-for="obj in order.objects" :key="obj.id" @click="changeOrder(obj.id, obj.name)" class="select_element">{{ obj.name }}</div>
					</div>
				</div>


				<label for='name'>Имя</label>
				<input v-model="name" class="form-control" type='text'/>

				<label for='phone'>Телефон</label>
				<input v-model="phone" class="form-control" type='text'/>

				<label for='adress'>Время звонка</label>
				<input v-model="call_time" class="form-control" type='text'/>

				<label for='created'>Дата заказа</label>
				<input v-model="created" class="form-control" type='text'/>

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

				order: {
					active: 		false,
					text: 			"Выберите статус",
					object:			1,
					objects:		[
						{id: 1, name: 'новый'},
						{id: 2, name: 'обработан'},
						{id: 3, name: 'отменен'}
					],
				},


        		name: 		"",
        		phone:		"",
				call_time:	"",
				created:	"",

        		statusm: 	0,
        		message:	"",

    		}
    	},

        mounted: function (){
            this.$nextTick(function(){

                let o = this;
    			axios.get(o.$store.state.domain + '/callbacks/' + o.$route.params.id).then(function(response){

					for(let i=0; i<o.order.objects.length; i++){
						if(o.order.objects[i].id == response.data.status){
							o.order.object 	= o.order.objects[i].id;
							o.order.text	= o.order.objects[i].name;
						}
					}

    				o.name 			= response.data.name;
    				o.phone 		= response.data.phone;
    				o.call_time 	= response.data.call_time;
					o.created 		= response.data.created;

    			}).catch(function (error){
    				console.log(error);
    			});

            })
        },

        methods: {

			changeOrder: function(id, name){
				this.order.object 	= id;
				this.order.active 	= false;
				this.order.text		= name;
			},

            editObject: function(){

                let o = this;
                let data = new FormData();

				data.append("status", o.order.object);

                axios.post(o.$store.state.domain + '/callbacks/' + o.$route.params.id + '/update', data).then(function(response){
                    if(response.data.response){
                        o.statusm 	= 1;
                        o.message	= "Изменен!";
                    }else{
                        o.statusm 	= -1;
                        o.message	= response.data.err;
                    }
                }).catch(function (error){
                    o.statusm 	= -1;
                    o.message	= "Неизвестная ошибка!";
                })

            }

        }

    }
</script>
