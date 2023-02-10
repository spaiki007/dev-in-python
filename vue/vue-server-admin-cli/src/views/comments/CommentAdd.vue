<template>
    <div>
        <h2>Добавление комментария</h2>

		<div class="wrap_select_block">
			<div class="select_block">
				<div class="active_select form-control">{{ user.text }}</div>
				<div class="change" @click="user.active = user.active ? false : true"><i class="fas fa-sort-down"></i></div>
			</div>
			<div v-if="user.active" class="select_elements">
				<div v-for="obj in user.objects" :key="obj.id" @click="changeUser(obj.id, obj.name)" class="select_element">{{ obj.name }}</div>
			</div>
		</div>

		<div class="wrap_select_block">
			<div class="select_block">
				<div class="active_select form-control">{{ comment.text }}</div>
				<div class="change" @click="comment.active = comment.active ? false : true"><i class="fas fa-sort-down"></i></div>
			</div>
			<div v-if="comment.active" class="select_elements">
				<div v-for="obj in comment.objects" :key="obj.id" @click="changeСomment(obj.id, obj.name)" class="select_element">{{ obj.name }}</div>
			</div>
		</div>

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

        <div v-if="statusm == 0" class="message">{{ message }}</div>
        <div v-else-if="statusm == -1" class="message alert-danger">{{ message }}</div>
        <div v-else="statusm == 1" class="message alert-success">{{ message }}</div>

        <button type="submit" class="btn btn-primary sub" v-on:click.prevent="addObject">Добавить</button>

    </div>
</template>


<script>

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

        		statusm: 		0,
        		message:		"",
    		}
    	},

		mounted: function(){
			this.$nextTick(function(){

				let o = this;

				//загружаем пользователей
				axios.get(o.$store.state.domain + '/users/get').then(function(response){
					o.user.objects = JSON.parse(response.data.objects);

					//загружаем комменты
					axios.get(o.$store.state.domain + '/comments/get').then(function(response){
						o.comment.objects = JSON.parse(response.data.objects);

						//загружаем продукты
						axios.get(o.$store.state.domain + '/products/get').then(function(response){
							o.product.objects = JSON.parse(response.data.objects);
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

    		addObject: function(){

    			let o = this;
    			let data = new FormData();

    			data.append("name", o.name);
    			data.append("positive", o.positive);
    			data.append("negative", o.negative);
    			data.append("rating", o.rating);
    			data.append("uid", o.user.object);
				data.append("cid", o.comment.object);
				data.append("pid", o.product.object);

    			axios.post(o.$store.state.domain + window.location.pathname, data).then(function(response){
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

    		}

    	}

    }
</script>
