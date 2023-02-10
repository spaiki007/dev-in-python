<template>
    <div>

		<div class="add-colors">
			<input v-model="color.code" class="form-control" type='text' placeholder="Код цвета"/>
			<input v-model="color.img" class="form-control" type='text' placeholder="Изображение цвета"/>
			<input v-model="color.article" class="form-control" type='text' placeholder="Артикуль"/>
			<input v-model="color.name" class="form-control" type='text' placeholder="Имя цвета"/>
			<input v-model="color.default" class="form-control" type='checkbox' />
			<button type="submit" @click.prevent="addColor()" class="btn btn-success">Добавить</button>
		</div>

		<div class="wrap-colors">

			<div class="colors" v-for="object in colors" :key="object.id">

				<div class="product-color-block">
					<div class="color" :style="{ background: object.code }"></div>
					<input v-model="object.code" class="form-control" type='text' placeholder="Код цвета"/>
				</div>

				<div class="product-color-block">
					<a :href="object.img" class="color-img" :style="{ 'background-image': 'url(' + object.img + ')'}"></a>
					<input v-model="object.img" class="form-control" type='text' placeholder="Изображение цвета"/>
				</div>

				<input v-model="object.article" class="form-control" type='text' placeholder="Артикуль"/>
				<input v-model="object.name" class="form-control" type='text' placeholder="Имя цвета"/>
				<input v-model="object.default" class="form-control" type='checkbox' />

				<button type="submit" @click.prevent="editColor(object)" class="btn btn-success">Изменить</button>
				<button type="submit" @click.prevent="delColor(object.id)" class="btn btn-success">Удалить</button>
			</div>

		</div>

        <div v-if="statusm == 0" class="message">{{ message }}</div>
        <div v-else-if="statusm == -1" class="message alert-danger">{{ message }}</div>
        <div v-else="statusm == 1" class="message alert-success">{{ message }}</div>

    </div>
</template>


<script>

    export default {
        data: function(){
    		return {

				colors: 		[],

				color: {
					article: 	"",
					name: 		"",
					code: 		"",
					img: 		"",
					default: 	false,
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

			init(){
				let o = this;
				axios.get(o.$store.state.domain + '/colors/get/'+ o.$route.params.id).then(function(response){

					let temp = JSON.parse(response.data.objects);
					for(let i=0; i<temp.length; i++){
						temp[i]['active'] = false;
						temp[i]['images'] = [];
					}
					o.colors = temp;
				});
			},

			addColor(){

				let o 		= this;
				let data 	= new FormData();

				data.append("pid", o.$route.params.id);
				data.append("article", o.color.article);
				data.append("name", o.color.name);
				data.append("code", o.color.code);
				data.append("img", o.color.img);
				data.append("default", o.color.default);

				axios.post(o.$store.state.domain + '/colors/add', data).then(function(response){

					if(response.data.response){
						o.init();
						o.color.article = "";
						o.color.name = "";
						o.color.code = "";
						o.color.img = "";
						o.color.default = false;

					}else{
						o.statusm 	= -1;
						o.message	= response.data.err;
					}

				}).catch(function (error){
					o.statusm 	= -1;
					o.message	= "Неизвестная ошибка!";
				});

			},

			delColor(id){
				let o = this;

				axios.post(o.$store.state.domain + '/colors/delete/' + id).then(function(response){
					o.init();
				}).catch(function (error) {
					console.log(error);
				});

			},

            editColor(object){

                let o = this;
                let data = new FormData();

				data.append("article", object.article);
				data.append("name", object.name);
				data.append("code", object.code);
				data.append("img", object.img);
				data.append("default", object.default);

				axios.post(o.$store.state.domain + "/colors/"+ object.id +"/update", data).then(function(response){
					if(response.data.response){
						o.message = "Изменен";
						o.statusm = 1;
					}else{
						o.statusm 	= -1;
						o.message	= response.data.err;
					}

				}).catch(function (error){
					o.statusm 	= -1;
					o.message	= "Неизвестная ошибка!";
				});

            },

        }

    }
</script>
