<template>
    <div>
        <div class="page-name">
            <h2>Слайдер</h2>
            <div class="add_object">
                <router-link :to="{name: 'sliderAdd'}" class="btn btn-success" >Добавить</router-link>
            </div>
        </div>

        <div class="form-delete">

			<div v-for="object in objects" :key="object.id" :class="['object']">

				<input
					class="remove_obj"
					name="objects[]"
					type="checkbox"
					:value="object.id"
					:checked='object.checked'
					@click="customChecked(object.id)"
				/>

				<div class="separator">|</div>
                <router-link :to="{name: 'sliderEdit', params: { id: object.id }}" class="object_name" >{{ object.name }}</router-link>

			</div>

			<div class="deleteBlock">
				<div class="customDeleteBlock">
					<button type="submit" class="btn btn-info" @click.prevent="chekedAll">Выбрать все</button>
					<button type="submit" class="btn btn-light" @:click.prevent="unCheckedAll">Снять выбор</button>
				</div>

				<button type="submit" class="btn btn-danger buttonList" @click.prevent="deleteObjects">Удалить выбранное</button>

			</div>

		</div>

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
    			axios.get(o.$store.state.domain + '/main-sliders/get').then(function(response){
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

    			axios.post(o.$store.state.domain + '/main-sliders/delete', formData).then(function(response){
					axios.get(o.$store.state.domain + '/main-sliders/get').then(function(response){
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
