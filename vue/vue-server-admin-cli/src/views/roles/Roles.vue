<template>
    <div>
        <div class="page-name">
            <h2>Роли</h2>
            <div class="add_object">
                <router-link :to="{name: 'roleAdd'}" class="btn btn-success" >Добавить</router-link>
            </div>
        </div>

        <form id="listObjects" class="form-delete" action="." method="post" accept-charset="utf-8" enctype="application/x-www-form-urlencoded">
			<div v-for="object in objects" :key="object.id" :class="['object']">

				<input
					class="remove_obj"
					name="objects[]"
					type="checkbox"
					:value="object.id"
					:checked='object.checked'
					v-on:click="customChecked(object.id)"
				/>

				<div class="separator">|</div>

                <router-link :to="{name: 'roleEdit', params: { id: object.id }}" class="object_name" >{{ object.name }}</router-link>

			</div>


			<div class="deleteBlock">
				<div class="customDeleteBlock">
					<button type="submit" class="btn btn-info" v-on:click.prevent="chekedAll">Выбрать все</button>
					<button type="submit" class="btn btn-light" v-on:click.prevent="unCheckedAll">Снять выбор</button>
				</div>

				<button type="submit" class="btn btn-danger buttonList" v-on:click.prevent="deleteObjects">Удалить выбранное</button>
			</div>
        </form>
    </div>
</template>


<script>
    export default {
        data: function(){
    		return {
    			objects: [],
    		}
    	},

    	mounted: function (){
    		this.$nextTick(function(){

    			let o = this;

    			axios.get(o.$store.state.domain + '/roles/get').then(function(response){
    				o.objects = JSON.parse(response.data.objects);
    			}).catch(function (error){
    				console.log(error);
    			});

    		})
    	},

    	methods: {

    		deleteObjects: function(){

    			let o        = this;
    			let formData = new FormData();

    			for(let i=0; i<o.objects.length; i++){
    				if(o.objects[i].checked){
    					formData.append("objects", o.objects[i].id);
    				}
    			}

    			axios.post(o.$store.state.domain + '/roles/delete', formData).then(function(response){
					axios.get(o.$store.state.domain + '/roles/get').then(function(response){
	    				o.objects = JSON.parse(response.data.objects);
	    			}).catch(function (error){
	    				console.log(error);
	    			});
    			}).catch(function (error) {
    				console.log(error);
    			});

    		},

			customChecked: function(id){
				for(let i=0; i<this.objects.length; i++){
					if(this.objects[i].id == id){
						this.objects[i].checked = this.objects[i].checked ? false : true;
						break;
					}
				}
			},

    		chekedAll: function(){
    			for(let i=0; i<this.objects.length; i++){
    				this.objects[i].checked = true;
    			}
    		},

    		unCheckedAll: function(){
    			for(let i=0; i<this.objects.length; i++){
    				this.objects[i].checked = false;
    			}
    		},

    	},
    }
</script>
