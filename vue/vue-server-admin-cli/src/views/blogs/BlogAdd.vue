<template>
    <div>
        <h2>Добавление блога</h2>

        <form class="form" action="." method="post" accept-charset="utf-8">

			<label for='name'>Наименование</label>
			<input v-model="name" id='name' class="form-control" name='name' type='text'/>

            <label for='slug'>Url - адресс</label>
            <input v-model="slug" id='slug' class="form-control" name='slug' type='text'/>

			<label for='pre_content'>Пре контент (макс. 500 символов - {{ pre_content.length }})</label>
			<textarea v-model="pre_content" class="form-control"></textarea>

            <div class="user-content">
                <label for='content'>Контент</label>
                <editor v-model="content" api-key='90qosixkylz14n41uwhlz2127dcmqb0xt9cvxx0wt2kfinzz' :init="this.$store.state.setting_editor"></editor>
            </div>

			<label for='poster'>Постер</label>
	        <div class="wrap-poster">
	            <a :href="poster" target="_blank">
	                <img :src="poster" class="activePoster">
	            </a>
				<div class="inputPoster">
					<input v-model="poster" class="form-control" type='text'/>
				</div>
	        </div>

			<label for='seo_title'>Seo Title</label>
			<input v-model="seo_title" id='seo_title' class="form-control" name='seo_title' type='text'/>

			<label for='seo_desc'>Seo Desc</label>
			<input v-model="seo_desc" id='seo_desc' class="form-control" name='seo_desc' type='text'/>

			<div v-if="statusm == 0" class="message">{{ message }}</div>
			<div v-else-if="statusm == -1" class="message alert-danger">{{ message }}</div>
			<div v-else="statusm == 1" class="message alert-success">{{ message }}</div>

			<button type="submit" class="btn btn-primary sub" v-on:click.prevent="addObject">Добавить</button>

        </form>
    </div>
</template>


<script>

    import Editor from '@tinymce/tinymce-vue';

    export default {

        data: function(){
    		return {

                name: 			"",
				pre_content: 	"",
                content: 		"",
                slug: 			"",
 				poster:			"",
                seo_title: 		"",
                seo_desc: 		"",

                statusm: 0,
                message: "",

    		}
    	},

        components: {
            'editor': Editor,
        },

    	methods: {

    		addObject: function(){

    			let o    = this;
    			let data = new FormData();

                data.append("name", o.name);
				data.append("pre_content", o.pre_content);
    			data.append("content", o.content);
    			data.append("slug", o.slug);
    			data.append("poster", o.poster);
    			data.append("seo_title", o.seo_title);
    			data.append("seo_desc", o.seo_desc);

    			axios.post(o.$store.state.domain + window.location.pathname, data).then(function(response){
    				if(response.data.response){
						o.statusm = 1;
    					o.message = "Основная информация добавлена...";
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
