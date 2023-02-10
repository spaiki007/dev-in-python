<template>
    <div>

		<div class="block-colors">
			<div class="wrap-color" v-for="color in colors">
				<div class="color-count">{{ color.images.length }}</div>
				<div :class="['color', {'color-active': color.active}]"
					:style="{ background:  getBack(color), 'background-size': 'cover' }"
					:title="color.name"
					@click="colorActivate(color.name)"
				></div>
			</div>

		</div>

		<div class="add-images">

			<div class="add-image-block">
				<input v-model="image" class="form-control" type='text' />
				<button type="submit" @click.prevent="addImage" class="btn btn-success">Добавить</button>
			</div>

			<div class="imagesBlock" v-for="object in colors" v-if="object.active">
				<div v-for="e in object.images" :key="e.id" :style="{backgroundImage: 'url(' + e.name + ')' }" class="viewImages" @click="deleteImages(e.id)"></div>
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

				image: '',
				colors: [],

                statusm: 0,
                message: "",
    		}
    	},

        mounted: function (){
            this.$nextTick(function(){

				let o = this;
				axios.get(o.$store.state.domain + '/colors/get/'+ o.$route.params.id).then(function(response){

					let temp = JSON.parse(response.data.objects);
					for(let i=0; i<temp.length; i++){
						temp[i]['active'] = false;

						axios.get(o.$store.state.domain + '/images/'+ temp[i].id).then(function(response){
							temp[i]['images'] = JSON.parse(response.data.objects);
						}).catch(function (error){
							console.log(error);
						});

					}
					o.colors = temp;

				}).catch(function (error){
					console.log(error);
				});



            });
        },

        methods: {

			getBack(object){

				if(object.img != ""){
					return "url(" + object.img + ") center center no-repeat"
				}

				if(object.code != ""){
					return object.code
				}

			},

			addImage(object){

				let o = this;

				for(let i = 0; i<o.colors.length; i++){
					if(o.colors[i].active){

						let data = new FormData();

						data.append("cid", o.colors[i].id);
						data.append("name", o.image);

						axios.post(o.$store.state.domain + "/images/add", data).then(function(response){

							axios.get(o.$store.state.domain + '/images/' + o.colors[i].id).then(function(response){
								o.colors[i].images = JSON.parse(response.data.objects);
								o.image = '';
								return;
							}).catch(function (error){
								o.statusm = -1;
								o.message = error;
							});
						}).catch(function(error){
							o.statusm = -1;
							o.message = error;
						});

					}
				}

			},

			deleteImages(id){
				let o = this;
				for(let i = 0; i<o.colors.length; i++){
					if(o.colors[i].active){

						axios.post(o.$store.state.domain + '/images/delete/' + id).then(function(response){
							axios.get(o.$store.state.domain + '/images/' + o.colors[i].id).then(function(response){
								o.colors[i].images = JSON.parse(response.data.objects);
								return;
							}).catch(function (error){
								o.statusm = -1;
								o.message = error;
							});
						}).catch(function (error) {
							o.statusm = -1;
							o.message = error;
						});

					}
				}

    		},

			//выбираем цвета
			colorActivate: function(name){
				let o = this;
				for(let i = 0; i<o.colors.length; i++){
					o.colors[i].active = o.colors[i].name == name ? true : false;
				}
			},

        }

    }
</script>
