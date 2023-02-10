<template>
    <div>
        <h2>Изменение акции</h2>
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
			<button type="submit" class="btn btn-primary sub" v-on:click.prevent="editObject">Изменить</button>

        </form>
    </div>
</template>


<script>

	import datetime from 'vuejs-datetimepicker';

    export default {
        data: function(){
    		return {

        		name: 				"",
				start_date:			"",
				end_date:			"",

        		statusm: 			0,
        		message:			"",

    		}
    	},

        mounted: function (){
            this.$nextTick(function(){

                let o = this;

    			axios.get(o.$store.state.domain + '/stocks/' + o.$route.params.id).then(function(response){

    				o.name = response.data.name;
					o.start_date = response.data.start;
					o.end_date = response.data.end;

    			}).catch(function (error){
    				console.log(error);
    			});

            })
        },

        methods: {

            editObject: function(){

                let o = this;
                let data = new FormData();

                data.append("name", o.name);
				data.append("start", this.start_date);
				data.append("end", this.end_date);

                axios.post(o.$store.state.domain + '/stocks/' + o.$route.params.id + '/update', data).then(function(response){
                    if(response.data.response){
                        o.statusm 	= 1;
                        o.message	= "Изменен!";
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
