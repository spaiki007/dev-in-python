<template>
	<div class="form">
		<h2>Добавление слайдера</h2>

		<label for='name'>Наименование</label>
		<input v-model="name" class="form-control" type='text'/>

		<label for='link'>Url - адресс</label>
		<input v-model="link" class="form-control" type='text'/>

		<div class="user-content">
			<label for='desc'>Описание</label>
			<textarea v-model="desc" class="form-control"></textarea>
		</div>

		<label for='price'>Цена</label>
		<input v-model="price" class="form-control" type='text' placeholder="Цена"/>

		<label for='poster'>Постер</label>
		<div class="wrap-poster">
			<a :href="poster" target="_blank">
				<img :src="poster" class="activePoster">
			</a>
			<div class="inputPoster">
				<input v-model="poster" class="form-control" type='text'/>
			</div>
		</div>

        <div v-if="statusm == 0" class="message">{{ message }}</div>
        <div v-else-if="statusm == -1" class="message alert-danger">{{ message }}</div>
        <div v-else="statusm == 1" class="message alert-success">{{ message }}</div>

        <button type="submit" class="btn btn-primary sub" @click.prevent="addObject">Добавить продукт</button>

	</div>
</template>


<script>

    export default {

        data: function(){
    		return {

                name: 		"",
                desc: 		"",
                link: 		"",
				price:		0,
				poster:		"",

                statusm: 0,
                message: "",

    		}
    	},

    	methods: {

    		addObject: function(){

    			let o    = this;
    			let data = new FormData();

                data.append("name", o.name);
    			data.append("desc", o.desc);
    			data.append("link", o.link);
				data.append("price", o.price);
				data.append("poster", o.poster);

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
