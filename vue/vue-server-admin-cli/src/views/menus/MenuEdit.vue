<template>
    <div>
        <h2>Изменение меню</h2>
        <form class="form" action="." method="post" accept-charset="utf-8">

            <div id="tab" class="demo">

				<div class="name_field">Выберите меню</div>
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

				<div class="name_field">Выберите страницу</div>
				<div class="wrap_select_block">
					<div class="select_block">
						<div class="active_select form-control">{{ page.text }}</div>
						<div class="change" @click="page.active = page.active ? false : true"><i class="fas fa-sort-down"></i></div>
					</div>
					<div v-if="page.active" class="select_elements">
						<div :key="0" @click="changePage(0, 'Без страницы')" class="select_element">Без страницы</div>
						<div v-for="obj in page.objects" :key="obj.id" @click="changePage(obj.id, obj.name)" class="select_element">{{ obj.name }}</div>
					</div>
				</div>

    			<label for='name'>Наименование</label>
    			<input v-model="name" id='name' class="form-control" name='name' type='text'/>

    			<label for='icon'>Иконка SVG</label>
    			<textarea v-model="icon" id='icon' class="form-control" name='icon'></textarea>

				<label for='order'>Сортировка</label>
    			<input v-model="order" id='order' class="form-control" name='order' type='text'/>

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

				parent: {
                    active: 		false,
                    text: 			"Выберите меню",
                    id:				0,
                    objects:		[],
                },

				page: {
					active: 		false,
					text: 			"Выберите страницу",
					id:				0,
					objects:		[],
				},

				parentID:			0,
        		name: 				"",
        		icon:				"",
				order:				0,

        		statusm: 			0,
        		message:			"",

    		}
    	},

        mounted: function (){
            this.$nextTick(function(){

                let o = this;
				axios.get(o.$store.state.domain + '/menus/' + o.$route.params.id).then(function(response){

					o.name 		= response.data.name;
					o.icon 		= response.data.icon;
					o.order		= response.data.order;
					o.pid		= response.data.pid;
					o.parentID	= response.data.parent;

					axios.get(o.$store.state.domain + '/menus/get').then(function(response){
	    				o.parent.objects = response.data.objects;

						for(let i=0; i<o.parent.objects.length; i++){
							if(o.parent.objects[i].id == o.parentID){
								o.parent.id 	= o.parent.objects[i].id;
								o.parent.text 	= o.parent.objects[i].name;
								break;
							}
						}

						axios.get(o.$store.state.domain + '/pages/get').then(function(response){
							o.page.objects = JSON.parse(response.data.objects);

							for(let i=0; i<o.page.objects.length; i++){
								if(o.page.objects[i].id == o.pid){
									o.page.id 	= o.page.objects[i].id;
									o.page.text = o.page.objects[i].name;
									break;
								}
							}

						}).catch(function(error){
							console.log(error);
						});

					}).catch(function (error){
						console.log(error);
					});

    			}).catch(function (error){
    				console.log(error);
    			});


            })
        },

        methods: {

			changePage: function(id, name){
				this.page.id 		= id;
				this.page.active 	= false;
				this.page.text 		= name;
			},

			changeParent: function(id, name){
    			this.parent.id 		= id;
    			this.parent.active 	= false;
    			this.parent.text 	= name;
    		},

            editObject: function(){

                let o = this;
                let data = new FormData();

				data.append("parent", this.parent.id);
				data.append("pid", this.page.id);
    			data.append("name", this.name);
    			data.append("icon", this.icon);
				data.append("order", this.order);

                axios.post(o.$store.state.domain + '/menus/' + o.$route.params.id + '/update', data).then(function(response){
                    if(response.data.response){

						axios.get(o.$store.state.domain + '/menus/get').then(function(response){
		                    o.parent.objects = response.data.objects;
		                }).catch(function(error){
		                    console.log(error);
		                });

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
