<template>
    <div>
        <h2>Изменение страницы</h2>
        <form class="form" action="." method="post" accept-charset="utf-8">

			<label for='name'>Наименование</label>
			<input v-model="name" id='name' class="form-control" name='name' type='text'/>

			<label for='slug'>Url - адресс</label>
			<input v-model="slug" id='slug' class="form-control" name='slug' type='text'/>

			<div class="user-content">
				<label for='content'>Контент</label>
				<editor v-model="content" api-key='90qosixkylz14n41uwhlz2127dcmqb0xt9cvxx0wt2kfinzz' :init="this.$store.state.setting_editor"></editor>
			</div>

			<label for='seo_title'>Seo Title</label>
			<input v-model="seo_title" id='seo_title' class="form-control" name='seo_title' type='text'/>

			<label for='seo_desc'>Seo Desc</label>
			<input v-model="seo_desc" id='seo_desc' class="form-control" name='seo_desc' type='text'/>

			<div v-if="statusm == 0" class="message">{{ message }}</div>
			<div v-else-if="statusm == -1" class="message alert-danger">{{ message }}</div>
			<div v-else="statusm == 1" class="message alert-success">{{ message }}</div>

			<button type="submit" class="btn btn-primary sub" v-on:click.prevent="editObject">Изменить</button>

        </form>
    </div>
</template>


<script>

    import Editor from '@tinymce/tinymce-vue';

    export default {
        data: function(){
    		return {

                name: 		"",
                content: 	"",
                slug: 		"",
                seo_title: 	"",
                seo_desc: 	"",

                statusm: 0,
                message: "",
    		}
    	},

        components: {
            'editor': Editor,
        },

        mounted: function (){
            this.$nextTick(function(){

                let o = this;


				//загружаем информацию о продукте
				axios.get(o.$store.state.domain + '/pages/' + o.$route.params.id).then(function(response){

                    o.name      = response.data.name;
                    o.content   = response.data.content;
                    o.slug      = response.data.slug;
                    o.seo_title = response.data.seo_title;
                    o.seo_desc  = response.data.seo_desc;

                }).catch(function (error){
                    console.log(error);
                });

			})
        },

        methods: {

            editObject: function(){

                let o       = this;
                let data    = new FormData();

                data.append("name", o.name);
    			data.append("content", o.content);
    			data.append("slug", o.slug);
    			data.append("seo_title", o.seo_title);
    			data.append("seo_desc", o.seo_desc);

                axios.post(o.$store.state.domain + '/pages/' + o.$route.params.id + '/update', data).then(function(response){
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
                })
            },

        }

    }
</script>
