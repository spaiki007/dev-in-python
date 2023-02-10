<template>
    <div>
        <h2>Добавление опции</h2>

        <form class="form" action="." method="post" accept-charset="utf-8">

			<label for='name'>Наименование</label>
			<input v-model="name" id='name' class="form-control" name='name' type='text'/>

			<label for='price'>Цена</label>
			<input v-model="price" id='price' class="form-control" name='name' type='text'/>

            <div v-if="statusm == 0" class="message">{{ message }}</div>
            <div v-else-if="statusm == -1" class="message alert-danger">{{ message }}</div>
            <div v-else="statusm == 1" class="message alert-success">{{ message }}</div>

            <button type="submit" class="btn btn-primary sub" v-on:click.prevent="addObject">Добавить</button>

        </form>
    </div>
</template>


<script>


    export default {

        data: function(){
    		return {
	            name:	"",
                price:	"",

                statusm: 0,
                message: "",
    		}
    	},

    	methods: {

    		addObject: function(){

    			let o    = this;
    			let data = new FormData();

                data.append("name", o.name);
    			data.append("price", o.price);

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
