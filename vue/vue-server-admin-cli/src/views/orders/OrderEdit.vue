<template>
    <div>
        <h2>Изменение заказа</h2>
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


				<label for='firtName'>Имя</label>
				<input v-model="firtName" class="form-control" type='text'/>

				<label for='lastName'>Фамилия</label>
				<input v-model="lastName" class="form-control" type='text'/>

				<label for='phone'>Телефон</label>
				<input v-model="phone" class="form-control" type='text'/>

				<label for='email'>Email</label>
				<input v-model="email" class="form-control" type='text'/>

				<label for='comment'>Коментарий</label>
                <textarea v-model="comment" class="form-control"></textarea>

				<label for='adress'>Адрес</label>
				<input v-model="adress" class="form-control" type='text'/>

				<label for='info'>Информация о заказе</label>
                <textarea v-model="info" class="form-control"></textarea>

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


        		firtName: 	"",
        		lastName:	"",
        		phone:		"",
        		email:		"",
				adress:		"",
				comment:	"",
				info:		"",
				created:	"",

        		statusm: 	0,
        		message:	"",

    		}
    	},

        mounted: function (){
            this.$nextTick(function(){

                let o = this;
    			axios.get(o.$store.state.domain + '/orders/' + o.$route.params.id).then(function(response){

					for(let i=0; i<o.order.objects.length; i++){
						if(o.order.objects[i].id == response.data.status){
							o.order.object 	= o.order.objects[i].id;
							o.order.text	= o.order.objects[i].name;
						}
					}

    				o.firtName 		= response.data.firtName;
    				o.lastName 		= response.data.lastName;
    				o.phone 		= response.data.phone;
    				o.email 		= response.data.email;
					o.comment 		= response.data.comment;
					o.adress 		= response.data.adress;
					o.info 			= response.data.info;
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

                axios.post(o.$store.state.domain + '/orders/' + o.$route.params.id + '/update', data).then(function(response){
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
