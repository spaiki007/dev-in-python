<template>
    <div>
        <h2>Добавление акции</h2>

        <form class="form" action="." method="post" accept-charset="utf-8">

			<label for='name'>Наименование</label>
			<input v-model="name" id='name' class="form-control" name='name' type='text'/>

			<label for='start_date'>Дата начала акции</label>
			<datetime v-model="start_date" format="MM/DD/YYYY" input-class="form-control"></datetime>

			<label for='end_date'>Дата окончания акции</label>
			<datetime v-model="end_date" format="MM/DD/YYYY" input-class="form-control"></datetime>

            <div v-if="statusm == 0" class="message">{{ message }}</div>
            <div v-else-if="statusm == -1" class="message alert-danger">{{ message }}</div>
            <div v-else="statusm == 1" class="message alert-success">{{ message }}</div>

            <button type="submit" class="btn btn-primary sub" v-on:click.prevent="addObject">Добавить</button>

        </form>
    </div>
</template>


<script>

	import datetime from 'vuejs-datetimepicker';

    export default {
        data: function(){
    		return {

        		name: 		"",
				start_date: "",
				end_date:	"",

				statusm: 			0,
				message:			"",
    		}
    	},

		components: {
			datetime: datetime,
		},

        methods: {

    		addObject: function(){

    			let o = this;
    			let data = new FormData();

    			data.append("name", this.name);
				data.append("start", this.start_date);
				data.append("end", this.end_date);

    			axios.post(o.$store.state.domain + window.location.pathname, data).then(function(response){
    				if(response.data.response){
    					o.statusm = 1;
						o.message = "Добавлен...";
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
