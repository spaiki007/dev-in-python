<template>
    <div>
        <h2>Добавление продукта</h2>

        <div class="form" >

			<div class="name">Категория</div>
			<div class="wrap_select_block">
				<div class="select_block">
					<div class="active_select form-control">{{ parent.activeSelectText }}</div>
					<div class="change" @click="parent.activeSelect ? parent.activeSelect = false : parent.activeSelect = true"><i class="fas fa-sort-down"></i></div>
				</div>
				<div v-if="parent.activeSelect" class="select_elements">
					<div v-for="obj in parent.objects" :key="obj.id" @click="changeParent(obj.id, obj.name)" class="select_element">{{ "—" . repeat(obj.level) + " " + obj.name }}</div>
				</div>
			</div>

			<div class="name">Производитель</div>
			<div class="wrap_select_block">
				<div class="select_block">
					<div class="active_select form-control">{{ manufacturer.activeSelectText }}</div>
					<div class="change" @click="manufacturer.activeSelect ? manufacturer.activeSelect = false : manufacturer.activeSelect = true"><i class="fas fa-sort-down"></i></div>
				</div>
				<div v-if="manufacturer.activeSelect" class="select_elements">
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

	        <button type="submit" class="btn btn-primary sub" v-on:click.prevent="addObject">Добавить продукт</button>

        </div>
    </div>
</template>


<script>

    import Editor from '@tinymce/tinymce-vue';

    export default {

        data: function(){
    		return {

                parent: {
                    activeSelect: 		false,
                    activeSelectText: 	"Выберите категорию",
                    object:				"",
                    objects:			[],
                },

                manufacturer: {
                    activeSelect: 		false,
                    activeSelectText: 	"Выберите производителя",
                    object:				"",
                    objects:			[],
                },

				stock: {
					name:		"Выберите акцию",
                    active: 	false,
                    text: 		"Выберите акцию",
                    object:		0,
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

        components: {
            'editor': Editor,
        },

        mounted: function(){
    		this.$nextTick(function(){

    			let o = this;

				//загружаем категории
    			axios.get(o.$store.state.domain + '/categories/get').then(function(response){
    				o.parent.objects = JSON.parse(response.data.objects);

					//загружаем производителей
					axios.get(o.$store.state.domain + '/manufacturers/get').then(function(response){
	    				o.manufacturer.objects = JSON.parse(response.data.objects);

						//загружаем акции
						axios.get(o.$store.state.domain + '/stocks/get').then(function(response){
							o.stock.objects = JSON.parse(response.data.objects);
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
				this.stock.object = id;
				this.stock.active = false;
				this.stock.text = name;
			},

            //меняем категорию товара
            changeParent: function(id, name){
    			this.parent.object = id;
    			this.parent.activeSelect = false;
    			this.parent.activeSelectText = name;
    		},

            changeManufacturer: function(id, name){
    			this.manufacturer.object = id;
    			this.manufacturer.activeSelect = false;
    			this.manufacturer.activeSelectText = name;
    		},

    		addObject: function(){

    			let o    = this;
    			let data = new FormData();

                data.append("parent", o.parent.object);
                data.append("manufacturer", o.manufacturer.object);
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
				data.append("stocksID", o.stock.object);

    			axios.post(o.$store.state.domain + window.location.pathname, data).then(function(response){

    				if(response.data.response){
						o.statusm = 1;
    					o.message = "Основная информация добавлена...";
    				}else{
    					o.statusm = -1;
    					o.message = response.data.err;
    				}

    			}).catch(function (error){
    				o.statusm = -1;
    				o.message = "Неизвестная ошибка!";
    			})

    		},

    	}

    }
</script>
