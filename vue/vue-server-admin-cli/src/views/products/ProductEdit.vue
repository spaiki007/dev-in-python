<template>
    <div class="form">
        <h2>Изменение продукта</h2>
		
        <div class="tabs">
            <div class="tabs-head">
                <div v-for="tab in tabs" :id="tab.id" :class="['tab', { active: tab.active }]" @click="changeTabs(tab.id)">{{ tab.name }}</div>
            </div>
            <div class="wrap-tab-content">

                <div class="tab-content tab-1" v-if="currentTab == 1">
					<product-edit></product-edit>
    			</div>

				<div class="tab-content tab-2" v-if="currentTab == 2">
					<edit-products-colors></edit-products-colors>
    			</div>

				<div class="tab-content tab-3" v-if="currentTab == 3">
					<product-edit-images></product-edit-images>
				</div>

				<div class="tab-content tab-4" v-if="currentTab == 4">
					<product-edit-characteristics></product-edit-characteristics>
				</div>

				<div class="tab-content tab-5" v-if="currentTab == 5">
					<product-edit-pickings></product-edit-pickings>
				</div>

				<div class="tab-content tab-6" v-if="currentTab == 6">
					<product-edit-options></product-edit-options>
				</div>

				<div class="tab-content tab-7" v-if="currentTab == 7">
					<product-edit-access></product-edit-access>
				</div>

            </div>
        </div>

    </div>
</template>


<script>

	import ProductEdit from '@/components/ProductsEdit/ProductEdit.vue'
	import ProductEditColors from '@/components/ProductsEdit/ProductEditColors.vue'
	import ProductEditImages from '@/components/ProductsEdit/ProductEditImages.vue'
	import ProductEditCharacteristics from '@/components/ProductsEdit/ProductEditCharacteristics.vue'
	import ProductEditPickings from '@/components/ProductsEdit/ProductEditPickings.vue'
	import ProductEditOptions from '@/components/ProductsEdit/ProductEditOptions.vue'
	import ProductEditAccess from '@/components/ProductsEdit/ProductEditAccess.vue'

    export default {

		components: {
			'product-edit':	ProductEdit,
			'edit-products-colors': ProductEditColors,
			'product-edit-images': ProductEditImages,
			'product-edit-characteristics': ProductEditCharacteristics,
			'product-edit-pickings': ProductEditPickings,
			'product-edit-options': ProductEditOptions,
			'product-edit-access': ProductEditAccess,
        },

        data: function(){
    		return {
				currentTab: 1,
                tabs: [
                    {id: 1, name: 'Информация', active: true},
					{id: 2, name: 'Цвета', active: false},
                    {id: 3, name: 'Изображения', active: false},
                    {id: 4, name: 'Характеристики', active: false},
					{id: 5, name: 'Комплектация', active: false},
					{id: 6, name: 'Опции', active: false},
					{id: 7, name: 'Акссесуары', active: false},
                ],

    		}
    	},

        methods: {

            //меняем табы
            changeTabs: function(id){
                this.currentTab = id;
                for(let i = 0; i<this.tabs.length; i++){
                    this.tabs[i].active = this.tabs[i].id == id ? true : false;
                }
            },

        }

    }
</script>
