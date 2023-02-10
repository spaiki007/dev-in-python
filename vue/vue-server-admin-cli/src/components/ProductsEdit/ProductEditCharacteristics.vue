<template>
    <div>

		<div class="wrap-characteristics">
			<div class="wrap-characteristic">
				<div class="name">Характеристики</div>
				<div class="wrap_select_block">
					<div class="select_block">
						<div class="active_select form-control">{{ characteristic.text }}</div>
						<div class="change" @click="characteristic.active = characteristic.active ? false : true"><i class="fas fa-sort-down"></i></div>
					</div>
					<div v-if="characteristic.active" class="select_elements">
						<div v-for="obj in characteristic.objects" :key="obj.id" @click="changeCharacteristic(obj.id, obj.name)" class="select_element">{{ obj.name }}</div>
					</div>
				</div>
			</div>
			<div class="wrap-characteristic">
				<div class="name">Значения</div>
				<div class="wrap_select_block">
					<div class="select_block">
						<div class="active_select form-control">{{ cvalue.text }}</div>
						<div class="change" @click="cvalue.active = cvalue.active ? false : true"><i class="fas fa-sort-down"></i></div>
					</div>
					<div v-if="cvalue.active" class="select_elements">
						<div v-for="obj in cvalue.objects" v-if="obj.cid == characteristic.object" :key="obj.id" @click="changeCvalue(obj.id, obj.name)" class="select_element">{{ obj.name }}</div>
					</div>
				</div>
			</div>
		</div>

		<div class="characteristics">
			<div class="characteristic" v-for="obj in characteristics" :key="obj.id" @click="delCharacteristics(obj.id)">
				<div class="characteristic-name">{{ obj.characteristic }}</div>
				<div class="characteristic-val">{{ obj.cvalue }}</div>
			</div>
		</div>

		<div class="addCharacteristics">
			<button type="submit" @click.prevent="addCharacteristic" class="btn btn-success">Добавить</button>
		</div>

        <div v-if="statusm == 0" class="message">{{ message }}</div>
        <div v-else-if="statusm == -1" class="message alert-danger">{{ message }}</div>
        <div v-else="statusm == 1" class="message alert-success">{{ message }}</div>

    </div>
</template>


<script>

    export default {

        data(){
    		return {

				characteristics: [],
				characteristic: {
					name: "Характеристики",
					text: "Выберите характеристику",
					active: false,
					object: 0,
					objects: [],
				},

				cvalue: {
					name: "Выберите значение",
					text: "Выберите значение",
					active: false,
					object: 0,
					objects: [],
				},

				caps:		[],

                statusm: 0,
                message: "",
    		}
    	},

        mounted: function (){
            this.$nextTick(function(){
				this.init();
            });
        },

        methods: {

			changeCharacteristic: function(id, name){
    			this.characteristic.object 	= id;
    			this.characteristic.active 	= false;
    			this.characteristic.text 	= name;

				this.cvalue.object 	= 0;
				this.cvalue.text 	= this.cvalue.name;
    		},

			changeCvalue (id, name){
    			this.cvalue.object 	= id;
    			this.cvalue.active 	= false;
    			this.cvalue.text 	= name;
    		},

			delCharacteristics(id){
				let o = this;

				axios.post(o.$store.state.domain + "/caps/"+ id +"/delete").then(function(response){
					o.init();
				}).catch(function (error){
					console.log(error);
				});
			},

			//Добавляем характеристики
			addCharacteristic (){
				let o = this;

				let data = new FormData();
				data.append("pid", o.$route.params.id);
				data.append("cid", o.cvalue.object);

				axios.post(o.$store.state.domain + "/caps/add", data).then(function(response){
					o.message = "Добавил...";
					o.statusm = 1;
					o.init();
				}).catch(function (error){
					o.statusm = -1;
					o.message = "Неизвестная ошибка!";
				});

			},

			init(){
				let o = this;

				//загружаем характеристики
				axios.get(o.$store.state.domain + '/characteristics/get').then(function(response){

					o.characteristic.objects = JSON.parse(response.data.objects);

					//загружаем значение характеристик
					axios.get(o.$store.state.domain + '/cvalues/get').then(function(response){
						o.cvalue.objects = JSON.parse(response.data.objects);

						//загружаем значение характеристик
						axios.get(o.$store.state.domain + '/caps/' + o.$route.params.id ).then(function(response){
							o.caps = JSON.parse(response.data.objects);

							let temp = [];

							//инициализируем характеристики
							for(let i=0; i<o.characteristic.objects.length; i++){
								for(let k=0; k<o.cvalue.objects.length; k++){
									for(let j=0; j<o.caps.length; j++){
										if(o.characteristic.objects[i].id == o.cvalue.objects[k].cid && o.cvalue.objects[k].id == o.caps[j].cvid){

											temp.push({
												'characteristic': o.characteristic.objects[i].name,
												'cvalue': o.cvalue.objects[k].name,
												'id': o.caps[j].id,
											});

											o.characteristic.object = 0;
											o.characteristic.text = o.characteristic.name;

											o.cvalue.object = 0;
											o.cvalue.text = o.cvalue.name;

											break;
										}
									}
								}
							}

							o.characteristics = temp;

							/*
							for(let i=0; i<o.characteristic.objects.length; i++){
								for(let k=0; k<o.cvalue.objects.length; k++){
									for(let j=0; j<o.caps.length; j++){
										if(o.characteristic.objects[i].id == o.cvalue.objects[k].cid && o.cvalue.objects[k].id == o.caps[j].cvid){
											o.characteristic.objects.splice(i, 1);
											break;
										}
									}
								}
							}
							*/

						}).catch(function (error){
							console.log(error);
						});

					}).catch(function (error){
						console.log(error);
					});

				}).catch(function (error){
					console.log(error);
				});

			},


        }

    }
</script>
