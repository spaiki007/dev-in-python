<template>
    <div>
        <h2>Добавление роли</h2>

        <form class="form" action="." method="post" accept-charset="utf-8">
            <div id="tab" class="demo">
                <label for='name'>Наименование</label>
    			<input v-model="name" id='name' class="form-control" name='name' type='text'/>

    			<div v-if="statusm == 0" class="message">{{ message }}</div>
    			<div v-else-if="statusm == -1" class="message alert-danger">{{ message }}</div>
    			<div v-else="statusm == 1" class="message alert-success">{{ message }}</div>

    			<button type="submit" class="btn btn-primary sub" v-on:click.prevent="addObject">Добавить</button>
            </div>
        </form>
    </div>
</template>


<script>
    export default {
        data: function(){
    		return {
                name: 		"",
        		statusm: 	0,
        		message:	"",
    		}
    	},

        methods: {

    		addObject: function(){

    			let o    = this;
    			let data = new FormData();

    			data.append("name", o.name);

    			axios.post(o.$store.state.domain + window.location.pathname, data).then(function(response){
    				if(response.data.response){
    					o.name 		= '';
    					o.statusm 	= 1;
    					o.message	= "Добавлен!";
    				}else{
    					o.statusm 	= -1;
    					o.message	= response.data.err;
    				}

    			}).catch(function (error){
    				o.statusm 	= -1;
    				o.message	= "Неизвестная ошибка!";
    			})

    		}

    	}

    }
</script>
