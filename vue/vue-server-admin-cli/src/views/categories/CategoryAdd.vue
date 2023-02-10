<template>
    <div>
        <h2>Добавление категории</h2>

        <form class="form" action="." method="post" accept-charset="utf-8">
            <div id="tab" class="demo">

				<div class="name">{{ parent.name }}</div>
				<div class="wrap_select_block">
					<div class="select_block">
						<div class="active_select form-control">{{ parent.text }}</div>
						<div class="change" @click="parent.active = parent.active ? false : true"><i class="fas fa-sort-down"></i></div>
					</div>
					<div v-if="parent.active" class="select_elements">
						<div :key="0" @click="changeParent(0, 'Родитель')" class="select_element">Родитель</div>
						<div v-for="obj in parent.objects" :key="obj.id" @click="changeParent(obj.id, obj.name)" class="select_element">{{ "—" . repeat(obj.level) + " " + obj.name }}</div>
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

				<label for='svg'>svg - иконка</label>
                <textarea v-model="svg" class="form-control"></textarea>

    			<div class="user-content">
    				<label for='content'>Контент</label>
                    <editor v-model="content" api-key='90qosixkylz14n41uwhlz2127dcmqb0xt9cvxx0wt2kfinzz' :init="this.$store.state.setting_editor"></editor>
    			</div>

    			<label for='slug'>Адрес страницы</label>
    			<input v-model="slug" id='slug' class="form-control" name='slug' type='text'/>

    			<label for='seo_title'>Seo Title</label>
    			<input v-model="seo_title" id='seo_title' class="form-control" name='seo_title' type='text'/>

    			<label for='seo_desc'>Seo Desc</label>
    			<textarea v-model="seo_desc" id='seo_desc' class="form-control" name='seo_desc'></textarea>

				<label for='order'>Сортировка</label>
				<input v-model="order" id='order' class="form-control" name='order' type='text'/>

                <div v-if="statusm == 0" class="message">{{ message }}</div>
                <div v-else-if="statusm == -1" class="message alert-danger">{{ message }}</div>
                <div v-else="statusm == 1" class="message alert-success">{{ message }}</div>

                <button type="submit" class="btn btn-primary sub" v-on:click.prevent="addObject">Добавить</button>
            </div>
        </form>
    </div>
</template>


<script>
    import Editor from '@tinymce/tinymce-vue';

    export default {
        data: function(){
    		return {

				parent: {
					name:		"Выберите родителя",
					active: 	false,
					text: 		"Родитель",
					object:		0,
					objects:	[],
				},

				stock: {
					name:		"Выберите акцию",
					active: 	false,
					text: 		"Выберите акцию",
					object:		0,
					objects:	[],
				},

        		name: 				"",
				svg:				"",
        		content:			"",
        		slug:				"",
        		seo_title:			"",
        		seo_desc:			"",
				order:				0,

        		statusm: 			0,
        		message:			"",
        		activeSelect: 		false,
        		activeSelectText: 	"Выберите меню",
    		}
    	},

        components: {
            'editor': Editor,
        },

		mounted: function (){
			this.$nextTick(function(){

				let o = this;

				axios.get(o.$store.state.domain + '/stocks/get').then(function(response){
					o.stock.objects = JSON.parse(response.data.objects);

					axios.get(o.$store.state.domain + '/categories/get').then(function(response){
	    				o.parent.objects = JSON.parse(response.data.objects);
	    			}).catch(function(error){
	    				console.log(error);
	    			});


				}).catch(function(error){
					console.log(error);
				});

			})
		},

        methods: {

			changeParent: function(id, name){
				this.parent.object = id;
				this.parent.active = false;
				this.parent.text = name;
			},

			changeStock: function(id, name){
				this.stock.object = id;
				this.stock.active = false;
				this.stock.text = name;
			},

    		addObject: function(){

    			let o = this;
    			let data = new FormData();

    			data.append("name", o.name);
				data.append("svg", o.svg);
    			data.append("content", o.content);
    			data.append("slug", o.slug);
    			data.append("seo_title", o.seo_title);
    			data.append("seo_desc", o.seo_desc);
				data.append("stocksID", o.stock.object);
				data.append("parent", o.parent.object);
				data.append("order", o.order);

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
