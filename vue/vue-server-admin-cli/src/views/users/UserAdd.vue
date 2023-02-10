<template>
    <div>
        <h2>Добавление пользователя</h2>

        <form class="form" action="." method="post" accept-charset="utf-8">
            <div id="tab" class="demo">
                <div class="name_field">Выберите роль</div>
                <div class="wrap_select_block">
                    <div class="select_block">
                        <div class="active_select form-control">{{ activeSelectText }}</div>
                        <div class="change" @click="activeSelect ? activeSelect = false : activeSelect = true"><i class="fas fa-sort-down"></i></div>
                    </div>
                    <div v-if="activeSelect" class="select_elements">
                        <div v-for="role in roles" :key="role.id" @click="changeRole(role.id, role.name)" class="select_element">{{ role.name }}</div>
                    </div>
                </div>

                <label for='login'>Логин</label>
                <input v-model="login" class="form-control" type='text'/>

				<label for='name'>Имя</label>
				<input v-model="name" class="form-control" type='text'/>

                <label for='passw'>Пароль</label>
                <input v-model="passw" id='passw' class="form-control" name='passw' type='text'/>

				<label for='city'>Город</label>
				<input v-model="city" id='city' class="form-control" name='city' type='text'/>

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
				login:				"",
                name: 				"",
                passw:				"",
                role:				"",
				city:				"",

                statusm: 			0,
                message:			"",
                activeSelect: 		false,
                activeSelectText: 	"Выберите роль",
                roles:				[],
    		}
    	},

        mounted: function(){
		this.$nextTick(function(){

			let o = this;
			axios.get(o.$store.state.domain + '/roles/get').then(function(response){
				o.roles = JSON.parse(response.data.objects);
			}).catch(function (error){
				console.log(error);
			});

		})
	},

	methods: {

		changeRole: function(role_id, name){
			this.role = role_id;
			this.activeSelect = false;
			this.activeSelectText = name;
		},

		addObject: function(){

			let o    = this;
			let data = new FormData();

			data.append("role", o.role);
			data.append("name", o.name);
			data.append("login", o.login);
			data.append("passw", o.passw);
			data.append("city", o.city);

			axios.post(o.$store.state.domain + window.location.pathname, data).then(function(response){

				if(response.data.response){
					o.statusm 	= 1;
					o.message	= "Добавлен!";
				}else{
					o.statusm 	= -1;
					o.message	= response.data.err;
				}

			}).catch(function (error){
                console.log(error);
				o.statusm 	= -1;
				o.message	= "Неизвестная ошибка!";
			})

		}

	}

    }
</script>
