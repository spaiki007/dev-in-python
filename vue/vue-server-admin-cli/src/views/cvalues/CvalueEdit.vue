<template>
    <div>
        <h2>Изменение значения характеристики</h2>
        <form class="form" action="." method="post" accept-charset="utf-8">

			<div class="name">{{ parent.name }}</div>
			<div class="wrap_select_block">
				<div class="select_block">
					<div class="active_select form-control">{{ parent.text }}</div>
					<div class="change" @click="parent.active = parent.active ? false : true"><i class="fas fa-sort-down"></i></div>
				</div>
				<div v-if="parent.active" class="select_elements">
					<div v-for="obj in parent.objects" :key="obj.id" @click="changeParent(obj.id, obj.name)" class="select_element">{{ obj.name }}</div>
				</div>
			</div>

			<label for='name'>Наименование</label>
			<input v-model="name" id='name' class="form-control" name='name' type='text'/>

            <div v-if="statusm == 0" class="message">{{ message }}</div>
            <div v-else-if="statusm == -1" class="message alert-danger">{{ message }}</div>
            <div v-else="statusm == 1" class="message alert-success">{{ message }}</div>

            <button type="submit" class="btn btn-primary sub" v-on:click.prevent="editObject">Изменить</button>

        </form>

    </div>
</template>

<script>
    export default {
        data: function(){
    		return {
				name:	"",

				parent: {
					name: "Характеристики",
					text: "выберите характеристику...",
					active: false,
					object: 0,
					objects: [],
				},

				statusm: 0,
				message: "",
    		}
    	},

        mounted: function (){
            this.$nextTick(function(){
                let o = this;
                axios.get(o.$store.state.domain + '/cvalues/' + o.$route.params.id).then(function(response){
                    o.name = response.data.name;

					let parentID = response.data.parent;
					axios.get(o.$store.state.domain + '/characteristics/get').then(function(response){
	    				o.parent.objects = JSON.parse(response.data.objects);

						for(let i=0; i<o.parent.objects.length; i++){

							if(o.parent.objects[i].id == parentID){
								o.parent.object = o.parent.objects[i].id;
								o.parent.text = o.parent.objects[i].name;
							}
						}

	    			}).catch(function (error){
	    				console.log(error);
	    			});


                }).catch(function (error){
                    console.log(error);
                });
            })
        },

        methods: {
			
			changeParent: function(id, name){
				this.parent.object 	= id;
				this.parent.active 	= false;
				this.parent.text 	= name;
			},

            editObject: function(){

                let o       = this;
                let data    = new FormData();

                data.append("name", o.name);
				data.append("parent", o.parent.object);

                axios.post(o.$store.state.domain + '/cvalues/' + o.$route.params.id + '/update', data).then(function(response){

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
