<template>
    <div>
        <h2>Изменение комплектации</h2>
        <form class="form" action="." method="post" accept-charset="utf-8">
            <div id="tab" class="demo">

				<label for='name'>Наименование</label>
				<input v-model="name" id='name' class="form-control" name='name' type='text'/>

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

                <button type="submit" class="btn btn-primary sub" v-on:click.prevent="editObject">Изменить</button>

            </div>
        </form>

    </div>
</template>

<script>
    export default {
        data: function(){
    		return {

				name: 		"",
				poster:		"",

				statusm: 0,
				message: "",
    		}
    	},

        mounted: function (){
            this.$nextTick(function(){

                let o = this;

                axios.get(o.$store.state.domain + '/pickings/' + o.$route.params.id).then(function(response){

                    o.name = response.data.name;
                    o.poster = response.data.img;

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
    			data.append("poster", o.poster);

                axios.post(o.$store.state.domain + '/pickings/' + o.$route.params.id + '/update', data).then(function(response){
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
