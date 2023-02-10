<template>
    <div>
        <h2>Изменение комментария</h2>
        <form class="form" action="." method="post" accept-charset="utf-8">

            <div id="tab" class="demo">

				<div class="name">Пользователь</div>
				<div class="wrap_select_block">
					<div class="select_block">
						<div class="active_select form-control">{{ user.text }}</div>
						<div class="change" @click="user.active = user.active ? false : true"><i class="fas fa-sort-down"></i></div>
					</div>
					<div v-if="user.active" class="select_elements">
						<div v-for="obj in user.objects" :key="obj.id" @click="changeUser(obj.id, obj.name)" class="select_element">{{ obj.name }}</div>
					</div>
				</div>

				<div class="name">Комментарии</div>
				<div class="wrap_select_block">
					<div class="select_block">
						<div class="active_select form-control">{{ comment.text }}</div>
						<div class="change" @click="comment.active = comment.active ? false : true"><i class="fas fa-sort-down"></i></div>
					</div>
					<div v-if="comment.active" class="select_elements">
						<div v-for="obj in comment.objects" :key="obj.id" @click="changeСomment(obj.id, obj.name)" class="select_element">{{ obj.name }}</div>
					</div>
				</div>

				<div class="name">Продукт</div>
				<div class="wrap_select_block">
					<div class="select_block">
						<div class="active_select form-control">{{ product.text }}</div>
						<div class="change" @click="product.active = product.active ? false : true"><i class="fas fa-sort-down"></i></div>
					</div>
					<div v-if="product.active" class="select_elements">
						<div @click="changeProduct(0, 'без продукта')" class="select_element">без продукта</div>
						<div v-for="obj in product.objects" :key="obj.id" @click="changeProduct(obj.id, obj.name)" class="select_element">{{ obj.name }}</div>
					</div>
				</div>

    			<label for='name'>Контент</label>
                <textarea v-model="name" class="form-control"></textarea>

    			<label for='positive'>positive</label>
    			<input v-model="positive" id='positive' class="form-control" name='positive' type='text'/>

    			<label for='negative'>negative</label>
    			<input v-model="negative" id='negative' class="form-control" name='negative' type='text'/>

    			<label for='rating'>rating</label>
    			<input v-model="rating" id='rating' class="form-control" name='rating' type='text'/>

				<div class="checkbox">
					<input v-model="status" type='checkbox' />
					<label for='status'>Статус</label>
				</div>


    			<div v-if="statusm == 0" class="message">{{ message }}</div>
    			<div v-else-if="statusm == -1" class="message alert-danger">{{ message }}</div>
    			<div v-else="statusm == 1" class="message alert-success">{{ message }}</div>

    			<button type="submit" class="btn btn-primary sub" @click.prevent="editObject">Изменить</button>

				<div class="custom-comments">
					<textarea v-model="customComments" class="form-control"></textarea>
					<button type="submit" class="btn btn-success sub" @click.prevent="addCustomObject">прокоментировать</button>
				</div>
            </div>
        </form>
    </div>
</template>


<script>
    import Editor from '@tinymce/tinymce-vue';

    export default {
        data: function(){
    		return {

				user: {
					active: 		false,
					text: 			"Выберите пользователя",
					object:			0,
					objects:		[],
				},

				comment: {
					active: 		false,
					text: 			"Выберите комментарий",
					object:			0,
					objects:		[],
				},

				product: {
					active: 		false,
					text: 			"Выберите продукт",
					object:			0,
					objects:		[],
				},

        		name: 			"",
        		positive:		"",
        		negative:		"",
        		rating:			1,
				status:			false,
				customComments: "",

        		statusm: 		0,
        		message:		"",

    		}
    	},

        mounted: function (){
            this.$nextTick(function(){

                let o = this;

    			axios.get(o.$store.state.domain + '/comments/' + o.$route.params.id).then(function(response){

					let uid = response.data.uid;
					let cid = response.data.cid;
					let pid = response.data.pid;

    				o.name 		= response.data.name;
    				o.positive 	= response.data.positive;
    				o.negative 	= response.data.negative;
    				o.rating 	= response.data.rating;
					o.status 	= response.data.status;

					//загружаем пользователей
					axios.get(o.$store.state.domain + '/users/get').then(function(response){
						o.user.objects = JSON.parse(response.data.objects);

						for(let i=0; i<o.user.objects.length; i++){
							if(o.user.objects[i].id == uid){
								o.user.object = o.user.objects[i].id;
								o.user.text = o.user.objects[i].name;
								break;
							}
						}

						//загружаем комменты
						axios.get(o.$store.state.domain + '/comments/get').then(function(response){
							o.comment.objects = JSON.parse(response.data.objects);

							for(let i=0; i<o.comment.objects.length; i++){
								if(o.comment.objects[i].id == cid){
									o.comment.object = o.comment.objects[i].id;
									o.comment.text = o.comment.objects[i].name;
									break;
								}
							}

							//загружаем продукты
							axios.get(o.$store.state.domain + '/products/get').then(function(response){
								o.product.objects = JSON.parse(response.data.objects);

								for(let i=0; i<o.product.objects.length; i++){
									if(o.product.objects[i].id == pid){
										o.product.object = o.product.objects[i].id;
										o.product.text = o.product.objects[i].name;
										break;
									}
								}

							}).catch(function (error){
								console.log(error);
							});

						}).catch(function (error){
							console.log(error);
						});

					}).catch(function (error){
						console.log(error);
					});

    			}).catch(function (error){
    				console.log(error);
    			});


            })
        },

        methods: {

			addCustomObject(){

    			let o = this;
    			let data = new FormData();

    			data.append("name", o.customComments);
				data.append("pid", o.product.object);
				data.append("cid", o.$route.params.id);

    			axios.post(o.$store.state.domain + '/comments/custom/add', data).then(function(response){
    				if(response.data.response){
    					o.statusm          = 1;
    					o.message          = "Добавлен!";
    				}else{
    					o.statusm 	= -1;
    					o.message	= response.data.err;
    				}
    			}).catch(function(error){
                    console.log(error);
    				o.statusm 	= -1;
    				o.message	= "Неизвестная ошибка!";
    			})

    		},

			changeUser: function(id, name){
				this.user.object 	= id;
				this.user.active 	= false;
				this.user.text		= name;
			},

			changeComment: function(id, name){
				this.comment.object = id;
				this.comment.active = false;
				this.comment.text 	= name;
			},

			changeProduct: function(id, name){
				this.product.object = id;
				this.product.active = false;
				this.product.text 	= name;
			},

            editObject: function(){

                let o = this;
                let data = new FormData();

				data.append("name", o.name);
				data.append("positive", o.positive);
				data.append("negative", o.negative);
				data.append("rating", o.rating);
				data.append("status", o.status);
				data.append("uid", o.user.object);
				data.append("cid", o.comment.object);
				data.append("pid", o.product.object);

                axios.post(o.$store.state.domain + '/comments/' + o.$route.params.id + '/update', data).then(function(response){
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
