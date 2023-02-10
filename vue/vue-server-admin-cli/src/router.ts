import Vue from 'vue';
import Router from 'vue-router';
import Home from './views/Home.vue';

import QuickOrders from './views/quickOrders/QuickOrders.vue';
import QuickOrderEdit from './views/quickOrders/QuickOrderEdit.vue';

import Callbacks from './views/callbacks/Callbacks.vue';
import CallbackEdit from './views/callbacks/CallbackEdit.vue';

import Orders from './views/orders/Orders.vue';
import OrderEdit from './views/orders/OrderEdit.vue';

import Roles from './views/roles/Roles.vue';
import RoleAdd from './views/roles/RoleAdd.vue';
import RoleEdit from './views/roles/RoleEdit.vue';

import Users from './views/users/Users.vue';
import UserAdd from './views/users/UserAdd.vue';
import UserEdit from './views/users/UserEdit.vue';

import Comments from './views/comments/Comments.vue';
import CommentAdd from './views/comments/CommentAdd.vue';
import CommentEdit from './views/comments/CommentEdit.vue';

import Blogs from './views/blogs/Blogs.vue';
import BlogAdd from './views/blogs/BlogAdd.vue';
import BlogEdit from './views/blogs/BlogEdit.vue';

import Pages from './views/pages/Pages.vue';
import PageAdd from './views/pages/PageAdd.vue';
import PageEdit from './views/pages/PageEdit.vue';

import Menus from './views/menus/Menus.vue';
import MenuAdd from './views/menus/MenuAdd.vue';
import MenuEdit from './views/menus/MenuEdit.vue';

import Categories from './views/categories/Categories.vue';
import CategoryAdd from './views/categories/CategoryAdd.vue';
import CategoryEdit from './views/categories/CategoryEdit.vue';

import Manufacturers from './views/manufacturers/Manufacturers.vue';
import ManufacturerAdd from './views/manufacturers/ManufacturerAdd.vue';
import ManufacturerEdit from './views/manufacturers/ManufacturerEdit.vue';

import Products from './views/products/Products.vue';
import ProductAdd from './views/products/ProductAdd.vue';
import ProductEdit from './views/products/ProductEdit.vue';

import Stocks from './views/stocks/Stocks.vue';
import StockAdd from './views/stocks/StockAdd.vue';
import StockEdit from './views/stocks/StockEdit.vue';

import Gifts from './views/gifts/Gifts.vue';
import GiftAdd from './views/gifts/GiftAdd.vue';
import GiftEdit from './views/gifts/GiftEdit.vue';

import Pickings from './views/pickings/Pickings.vue';
import PickingAdd from './views/pickings/PickingAdd.vue';
import PickingEdit from './views/pickings/PickingEdit.vue';

import Options from './views/options/Options.vue';
import OptionAdd from './views/options/OptionAdd.vue';
import OptionEdit from './views/options/OptionEdit.vue';

import Characteristics from './views/characteristics/Characteristics.vue';
import CharacteristicAdd from './views/characteristics/CharacteristicAdd.vue';
import CharacteristicEdit from './views/characteristics/CharacteristicEdit.vue';

import Cvalues from './views/cvalues/Cvalues.vue';
import CvalueAdd from './views/cvalues/CvalueAdd.vue';
import CvalueEdit from './views/cvalues/CvalueEdit.vue';

import Sliders from './views/sliders/Sliders.vue';
import SliderAdd from './views/sliders/SliderAdd.vue';
import SliderEdit from './views/sliders/SliderEdit.vue';

Vue.use(Router);

export default new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [

        {path: '/', name: 'home', component: Home},

		{path: '/main-sliders', name: 'sliders', component: Sliders},
        {path: '/main-sliders/add', name: 'sliderAdd', component: SliderAdd},
        {path: '/main-sliders/:id', name: 'sliderEdit', component: SliderEdit},

		{path: '/quick-orders', name: 'quickOrders', component: QuickOrders},
		{path: '/quick-orders/:id', name: 'quickOrderEdit', component: QuickOrderEdit},

		{path: '/callbacks', name: 'callbacks', component: Callbacks},
		{path: '/callbacks/:id', name: 'callbackEdit', component: CallbackEdit},

		{path: '/orders', name: 'orders', component: Orders},
        {path: '/orders/:id', name: 'orderEdit', component: OrderEdit},

        {path: '/roles', name: 'roles', component: Roles},
        {path: '/roles/add', name: 'roleAdd', component: RoleAdd},
        {path: '/roles/:id', name: 'roleEdit', component: RoleEdit},

        {path: '/users', name: 'users', component: Users},
        {path: '/users/add', name: 'userAdd', component: UserAdd},
        {path: '/users/:id', name: 'userEdit', component: UserEdit},

		{path: '/comments', name: 'comments', component: Comments},
		{path: '/comments/add', name: 'commentAdd', component: CommentAdd},
		{path: '/comments/:id', name: 'commentEdit', component: CommentEdit},

		{path: '/blogs', name: 'blogs', component: Blogs},
        {path: '/blogs/add', name: 'blogAdd', component: BlogAdd},
        {path: '/blogs/:id', name: 'blogEdit', component: BlogEdit},

		{path: '/pages', name: 'pages', component: Pages},
        {path: '/pages/add', name: 'pageAdd', component: PageAdd},
        {path: '/pages/:id', name: 'pageEdit', component: PageEdit},

        {path: '/menus', name: 'menus', component: Menus},
        {path: '/menus/add', name: 'menuAdd', component: MenuAdd},
        {path: '/menus/:id', name: 'menuEdit', component: MenuEdit},

		{path: '/categories', name: 'categories', component: Categories},
		{path: '/categories/add', name: 'categoryAdd', component: CategoryAdd},
		{path: '/categories/:id', name: 'categoryEdit', component: CategoryEdit},

        {path: '/manufacturers', name: 'manufacturers', component: Manufacturers},
        {path: '/manufacturers/add', name: 'manufacturerAdd', component: ManufacturerAdd},
        {path: '/manufacturers/:id', name: 'manufacturerEdit', component: ManufacturerEdit},

        {path: '/products', name: 'products', component: Products},
        {path: '/products/add', name: 'productAdd', component: ProductAdd},
        {path: '/products/:id', name: 'productEdit', component: ProductEdit},

	    {path: '/stocks', name: 'stocks', component: Stocks},
	    {path: '/stocks/add', name: 'stockAdd', component: StockAdd},
	    {path: '/stocks/:id', name: 'stockEdit', component: StockEdit},

	    {path: '/gifts', name: 'gifts', component: Gifts},
	    {path: '/gifts/add', name: 'giftAdd', component: GiftAdd},
	    {path: '/gifts/:id', name: 'giftEdit', component: GiftEdit},

	    {path: '/pickings', name: 'pickings', component: Pickings},
	    {path: '/pickings/add', name: 'pickingAdd', component: PickingAdd},
	    {path: '/pickings/:id', name: 'pickingEdit', component: PickingEdit},

	    {path: '/options', name: 'options', component: Options},
	    {path: '/options/add', name: 'optionAdd', component: OptionAdd},
	    {path: '/options/:id', name: 'optionEdit', component: OptionEdit},

	    {path: '/characteristics', name: 'characteristics', component: Characteristics},
	    {path: '/characteristics/add', name: 'characteristicAdd', component: CharacteristicAdd},
	    {path: '/characteristics/:id', name: 'characteristicEdit', component: CharacteristicEdit},

	    {path: '/cvalues', name: 'cvalues', component: Cvalues},
	    {path: '/cvalues/add', name: 'cvalueAdd', component: CvalueAdd},
	    {path: '/cvalues/:id', name: 'cvalueEdit', component: CvalueEdit},

    ],
});
