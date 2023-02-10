<template>
    <div class="form">

		<div class="name">Категория</div>
		<div class="wrap_select_block">
			<div class="select_block">
				<div class="active_select form-control">{{ category.text }}</div>
				<div class="change" @click="category.active = category.active ? false : true"><i class="fas fa-sort-down"></i></div>
			</div>
			<div v-if="category.active" class="select_elements">
				<div v-for="obj in category.objects" :key="obj.id" @click="changeCategory(obj.id, obj.name)" class="select_element">{{ "—" . repeat(obj.level) + " " + obj.name }}</div>
			</div>
		</div>

		<div class="name">Производитель</div>
		<div class="wrap_select_block">
			<div class="select_block">
				<div class="active_select form-control">{{ manufacturer.text }}</div>
				<div class="change" @click="manufacturer.active = manufacturer.active ? false : true"><i class="fas fa-sort-down"></i></div>
			</div>
			<div v-if="manufacturer.active" class="select_elements">
				<div v-for="obj in manufacturer.objects" :key="obj.id" @click="changeManufacturer(obj.id, obj.name)" class="select_element">{{ obj.name }}</div>
			</div>
		</div>

		<div class="name">{{ stock.name }}</div>
		<div class="wrap_select_block">
			<div class="select_block">
				<div class="active_select form-control">{{ stock.text }}</div>
				<div class="change" @click="stock.active = stock.active ? false : true"><i class="fas fa-sort-down"></i></div>
			</div>
			<div v-if="stock.active" class="select_elements">
				<div :key="0" @click="changeStock(0, 'Без акции...')" class="select_element">Без акции...</div>
				<div v-for="obj in stock.objects" :key="obj.id" @click="changeStock(obj.id, obj.name)" class="select_element">{{ obj.name }}</div>
			</div>
		</div>

		<label for='name'>Наименование</label>
		<input v-model="name" id='name' class="form-control" name='name' type='text'/>

        <label for='slug'>Url - адресс</label>
        <input v-model="slug" id='slug' class="form-control" name='slug' type='text'/>

        <div class="user-content">
            <label for='content'>Контент</label>
            <editor v-model="content" api-key='90qosixkylz14n41uwhlz2127dcmqb0xt9cvxx0wt2kfinzz' :init="this.$store.state.setting_editor"></editor>
        </div>

		<label for='price'>Цена</label>
		<input v-model="price" class="form-control" type='text' placeholder="Цена"/>

		<label for='old_price'>Старая цена</label>
		<input v-model="old_price" class="form-control" type='text' placeholder="Старая цена"/>

		<label for='poster'>Постер</label>
        <div class="wrap-poster">
            <a :href="poster" target="_blank">
                <img :src="poster" class="activePoster">
            </a>
			<div class="inputPoster">
				<input v-model="poster" class="form-control" type='text'/>
			</div>
        </div>

		<label for='poster'>Thumbnail - Постер</label>
		<div class="wrap-poster">
			<a :href="thumbnail" target="_blank">
				<img :src="thumbnail" class="activePoster">
			</a>
			<div class="inputPoster">
				<input v-model="thumbnail" class="form-control" type='text'/>
			</div>
		</div>

		<label for='seo_title'>Seo Title</label>
		<input v-model="seo_title" id='seo_title' class="form-control" name='seo_title' type='text'/>

		<label for='seo_desc'>Seo Desc</label>
		<input v-model="seo_desc" id='seo_desc' class="form-control" name='seo_desc' type='text'/>
		<div class="checkbox">
			<input v-model="market" id='market' name='market' type='checkbox'/>
			<label for='market'>Маркет</label>
		</div>
		<div class="checkbox">
			<input v-model="avalible" id='avalible' name='avalible' type='checkbox' />
			<label for='avalible'>Доступность</label>
		</div>

        <div v-if="statusm == 0" class="message">{{ message }}</div>
        <div v-else-if="statusm == -1" class="message alert-danger">{{ message }}</div>
        <div v-else="statusm == 1" class="message alert-success">{{ message }}</div>

		<button type="submit" class="btn btn-primary sub" v-on:click.prevent="editObject">Изменить</button>

    </div>
</template>


<script>

	import Editor from '@tinymce/tinymce-vue';

    export default {

		components: {
            'editor': Editor,
        },

        data: function(){
    		return {

				category: {
					active: 	false,
					text: 		"Выберите меню",
					id:			"",
					objects:	[],
				},

				manufacturer: {
					active: 	false,
					text: 		"Выберите производителя",
					id:			"",
					objects:	[],
				},

				stock: {
					name:		"Выберите акцию",
					active: 	false,
					text: 		"Выберите акцию",
					id:			0,
					objects:	[],
				},


                name: 		"",
                content: 	"",
                slug: 		"",
				price:		0,
				old_price:	0,
				poster:		"",
				thumbnail:	"",
                seo_title: 	"",
                seo_desc: 	"",
                market: 	false,
                avalible: 	true,

                statusm: 0,
                message: "",
    		}
    	},

        mounted: function (){
            this.$nextTick(function(){

				let o = this;

				axios.get(o.$store.state.domain + '/products/' + o.$route.params.id).then(function(response){

					let cid = response.data.cid;
					let mid = response.data.mid;
					let sid = response.data.sid;

					o.name      = response.data.name;
					o.content   = response.data.content;
					o.slug      = response.data.slug;

					o.price		= response.data.price;
					o.old_price = response.data.old_price;

					o.seo_title = response.data.seo_title;
					o.seo_desc  = response.data.seo_desc;
					o.market    = response.data.market;
					o.avalible  = response.data.avalible;
					o.poster	= response.data.poster;
					o.thumbnail	= response.data.thumbnail;

					axios.get(o.$store.state.domain + '/categories/get').then(function(response){
						o.category.objects = JSON.parse(response.data.objects);

						for(let i=0; i<o.category.objects.length; i++){
							if(o.category.objects[i].id == cid){
								o.category.id = o.category.objects[i].id;
								o.category.text = o.category.objects[i].name;
								break;
							}
						}

						axios.get(o.$store.state.domain + '/manufacturers/get').then(function(response){
							o.manufacturer.objects = JSON.parse(response.data.objects);

							for(let i=0; i<o.manufacturer.objects.length; i++){
								if(o.manufacturer.objects[i].id == mid){
									o.manufacturer.id = o.manufacturer.objects[i].id;
									o.manufacturer.text = o.manufacturer.objects[i].name;
									break;
								}
							}

							axios.get(o.$store.state.domain + '/stocks/get').then(function(response){
								o.stock.objects = JSON.parse(response.data.objects);

								for(let i=0; i<o.stock.objects.length; i++){
									if(o.stock.objects[i].id == sid){
										o.stock.id = o.stock.objects[i].id;
										o.stock.text = o.stock.objects[i].name;
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

            });
        },

        methods: {

			changeStock: function(id, name){
				this.stock.id = id;
				this.stock.active = false;
				this.stock.text = name;
			},

			changeCategory: function(id, name){
				this.category.id 		= id;
				this.category.active 	= false;
				this.category.text 		= name;
			},

			changeManufacturer: function(id, name){
				this.manufacturer.id 		= id;
				this.manufacturer.active 	= false;
				this.manufacturer.text 		= name;
			},

            editObject: function(){

                let o		= this;
                let data	= new FormData();

				data.append("cid", o.category.id);
                data.append("mid", o.manufacturer.id);
				data.append("sid", o.stock.id);
                data.append("name", o.name);
    			data.append("content", o.content);
    			data.append("slug", o.slug);
				data.append("price", o.price);
    			data.append("old_price", o.old_price);
				data.append("poster", o.poster);
				data.append("thumbnail", o.thumbnail);
    			data.append("seo_title", o.seo_title);
    			data.append("seo_desc", o.seo_desc);
    			data.append("market", o.market);
    			data.append("avalible", o.avalible);

                axios.post(o.$store.state.domain + '/products/' + o.$route.params.id + '/update', data).then(function(response){
                    if(response.data.response){
                        o.statusm = 1;
                        o.message = "Изменен!";
                    }else{
                        o.statusm = -1;
                        o.message = response.data.err;
                    }

                }).catch(function (error){
                    console.log(error);
                    o.statusm = -1;
                    o.message = "Неизвестная ошибка!";
                });

            },

        }

    }
</script>
