(function(t){function a(a){for(var i,o,r=a[0],n=a[1],l=a[2],u=0,v=[];u<r.length;u++)o=r[u],Object.prototype.hasOwnProperty.call(c,o)&&c[o]&&v.push(c[o][0]),c[o]=0;for(i in n)Object.prototype.hasOwnProperty.call(n,i)&&(t[i]=n[i]);d&&d(a);while(v.length)v.shift()();return e.push.apply(e,l||[]),s()}function s(){for(var t,a=0;a<e.length;a++){for(var s=e[a],i=!0,r=1;r<s.length;r++){var n=s[r];0!==c[n]&&(i=!1)}i&&(e.splice(a--,1),t=o(o.s=s[0]))}return t}var i={},c={app:0},e=[];function o(a){if(i[a])return i[a].exports;var s=i[a]={i:a,l:!1,exports:{}};return t[a].call(s.exports,s,s.exports,o),s.l=!0,s.exports}o.m=t,o.c=i,o.d=function(t,a,s){o.o(t,a)||Object.defineProperty(t,a,{enumerable:!0,get:s})},o.r=function(t){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(t,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(t,"__esModule",{value:!0})},o.t=function(t,a){if(1&a&&(t=o(t)),8&a)return t;if(4&a&&"object"===typeof t&&t&&t.__esModule)return t;var s=Object.create(null);if(o.r(s),Object.defineProperty(s,"default",{enumerable:!0,value:t}),2&a&&"string"!=typeof t)for(var i in t)o.d(s,i,function(a){return t[a]}.bind(null,i));return s},o.n=function(t){var a=t&&t.__esModule?function(){return t["default"]}:function(){return t};return o.d(a,"a",a),a},o.o=function(t,a){return Object.prototype.hasOwnProperty.call(t,a)},o.p="/";var r=window["webpackJsonp"]=window["webpackJsonp"]||[],n=r.push.bind(r);r.push=a,r=r.slice();for(var l=0;l<r.length;l++)a(r[l]);var d=n;e.push([0,"chunk-vendors"]),s()})({0:function(t,a,s){t.exports=s("56d7")},"56d7":function(t,a,s){"use strict";s.r(a);s("cadf"),s("551c"),s("f751"),s("097d");var i=s("2b0e"),c=function(){var t=this,a=t.$createElement,s=t._self._c||a;return s("div",{staticClass:"categories-app",attrs:{id:"catalog-app"}},[s("div",{staticClass:"catalog-products"},[s("div",{staticClass:"filters"},[s("div",{staticClass:"filters-name-block"},[s("img",{staticClass:"filters-name-icon",attrs:{src:t.domain+"/static/img/filter-name-icon.png"}}),s("div",{staticClass:"filters-name"},[t._v("фильтры")])]),s("div",{staticClass:"filter"},[s("div",{staticClass:"filter-name"},[t._v("Цена (рубли)")]),s("div",{staticClass:"icon-border"}),s("div",{staticClass:"user-slider"},[s("range-slider",{staticClass:"slider",attrs:{min:t.staticMin,max:t.staticMax,step:"100"},model:{value:t.valMin,callback:function(a){t.valMin=a},expression:"valMin"}}),s("range-slider",{staticClass:"slider",attrs:{min:t.staticMin,max:t.staticMax,step:"100"},model:{value:t.valMax,callback:function(a){t.valMax=a},expression:"valMax"}})],1),s("div",{staticClass:"filter-range"},[s("div",{staticClass:"filter-start"},[t._v(t._s(t.valMin))]),s("div",{staticClass:"filter-end"},[t._v(t._s(t.valMax))])])]),s("div",{staticClass:"filter"},[s("div",{staticClass:"filter-name"},[t._v("Наличие")]),s("div",{staticClass:"icon-border"}),s("div",{staticClass:"filters-radio-button"},[s("div",{staticClass:"filter-radio-button-block",on:{click:function(a){t.avalible=!1}}},[s("div",{staticClass:"filter-radio-button-wrap"},[s("div",{class:["filter-radio-button",{"radio-active":!t.avalible}]})]),s("div",{staticClass:"filter-checkbox-name"},[t._v("Все товары")])]),s("div",{staticClass:"filter-radio-button-block",on:{click:function(a){t.avalible=!0}}},[s("div",{staticClass:"filter-radio-button-wrap"},[s("div",{class:["filter-radio-button",{"radio-active":t.avalible}]})]),s("div",{staticClass:"filter-checkbox-name"},[t._v("Товары в наличии")])])])]),s("div",{staticClass:"filter"},[s("div",{staticClass:"filter-name"},[t._v("Производитель")]),s("div",{staticClass:"icon-border"}),s("div",{staticClass:"filters-select"},[s("div",{staticClass:"main-category-select",on:{click:function(a){t.manufacturer.active=!t.manufacturer.active}}},[s("div",{staticClass:"main-category-products-bottom-name"},[t._v(t._s(t.manufacturer.name))]),s("img",{staticClass:"main-arrow-top-bottom",attrs:{src:t.domain+"/static/img/arrow-top-bottom.png"}})]),t.manufacturer.active?s("div",{staticClass:"sort-by-list"},[s("div",{staticClass:"sort-by",on:{click:function(a){return t.changeManufacturers(!1,"Выберите бренд")}}},[t._v("Выберите бренд")]),t._l(t.manufacturer.objects,function(a){return s("div",{key:a.id,staticClass:"sort-by",on:{click:function(s){return t.changeManufacturers(a.id,a.name)}}},[t._v(t._s(a.name))])})],2):t._e()])]),s("div",{staticClass:"filter"},[s("div",{staticClass:"filter-name"},[t._v("Категории")]),s("div",{staticClass:"icon-border"}),s("div",{staticClass:"filter-categories"},t._l(t.categories,function(a,i){return s("div",{key:i,staticClass:"filter-category"},[s("a",{staticClass:"name",attrs:{href:"/shop/categories/"+a.category.slug}},[t._v(t._s(a.category.name))]),t._l(a.subCat,function(a,i){return i<3?s("a",{key:a.id,staticClass:"sub-name",attrs:{href:"/shop/categories/"+a.slug}},[t._v(t._s(a.name))]):t._e()}),t._l(a.subCat,function(i,c){return c>3&&a.active?s("a",{key:i.id,staticClass:"sub-name",attrs:{href:"/shop/categories/"+i.slug}},[t._v(t._s(i.name))]):t._e()}),a.subCat.length>3?s("div",{staticClass:"sub-cat-open",on:{click:function(t){a.active=!a.active}}},[t._v("\n\t\t\t\t\t\t\tраскрыть "),s("svg",{staticClass:"svg-inline--fa fa-chevron-down fa-w-14 fa-2x",attrs:{"aria-hidden":"true",focusable:"false","data-prefix":"fas","data-icon":"chevron-down",role:"img",xmlns:"http://www.w3.org/2000/svg",viewBox:"0 0 448 512"}},[s("path",{attrs:{fill:"currentColor",d:"M207.029 381.476L12.686 187.132c-9.373-9.373-9.373-24.569 0-33.941l22.667-22.667c9.357-9.357 24.522-9.375 33.901-.04L224 284.505l154.745-154.021c9.379-9.335 24.544-9.317 33.901.04l22.667 22.667c9.373 9.373 9.373 24.569 0 33.941L240.971 381.476c-9.373 9.372-24.569 9.372-33.942 0z"}})])]):t._e()],2)}),0)]),s("div",{staticClass:"filter-search"},[s("div",{staticClass:"wrap-callback",on:{mouseover:function(a){t.buttonIsActive=!0},mouseout:function(a){t.buttonIsActive=!1},click:t.getProducts}},[s("div",{class:["callback-background",{active:t.buttonIsActive}]},[s("div",{staticClass:"wrap-callback-background"})]),t._m(0)]),s("div",{staticClass:"wrap-callback",on:{mouseover:function(a){t.buttonIsActive2=!0},mouseout:function(a){t.buttonIsActive2=!1},click:function(a){return t.location.reload()}}},[s("div",{class:["callback-background",{active:t.buttonIsActive2}]},[s("div",{staticClass:"wrap-callback-background"})]),t._m(1)])])]),s("div",{staticClass:"sort-and-category-products"},[s("div",{staticClass:"sort-block"},[s("div",{staticClass:"filter-sort",on:{click:function(a){t.sort.active=!t.sort.active}}},[s("div",{staticClass:"name"},[t._v("Сортировка по "+t._s(t.sort.activeName))]),s("img",{staticClass:"icon",attrs:{src:t.domain+"/static/img/arrow-top-bottom.png"}})]),s("div",{staticClass:"sort-by-list",style:{display:t.sort.active?"block":"none"}},t._l(t.sort.variant,function(a){return s("div",{key:a.id,staticClass:"sort-by",on:{click:function(s){return t.selectSort(a.id,a.name)}}},[t._v(t._s(a.name))])}),0)]),s("div",{staticClass:"main-action-category-products catalog"},[t.quickOrderOpen?s("callback",{attrs:{close:t.close,product:t.activeProduct}}):t._e(),t.color.active?s("addbasket",{attrs:{product:t.color.product},on:{"close-color":t.closeColor}}):t._e(),s("div",{staticClass:"products"},t._l(t.objects.slice(t.pagination.active*t.pagination.max),function(a,i){return s("div",{directives:[{name:"show",rawName:"v-show",value:i<t.pagination.max,expression:"index < pagination.max"}],key:a.id,staticClass:"product"},[s("div",{staticClass:"wrap-product"},[s("div",{staticClass:"product-block-1"},[s("div",{staticClass:"product-image-block",style:[{backgroundImage:"url("+a.poster+")"}]}),s("a",{staticClass:"product-name",attrs:{href:t.domain+"/shop/products/"+a.slug}},[t._v(t._s(a.name))]),s("div",{staticClass:"product-rating"},[s("img",{staticClass:"star",attrs:{src:t.domain+"/static/img/raiting-fill.png"}}),s("img",{staticClass:"star",attrs:{src:t.domain+"/static/img/raiting-fill.png"}}),s("img",{staticClass:"star",attrs:{src:t.domain+"/static/img/raiting-fill.png"}}),s("img",{staticClass:"star",attrs:{src:t.domain+"/static/img/raiting-fill.png"}}),s("img",{staticClass:"star",attrs:{src:t.domain+"/static/img/raiting.png"}})])]),s("div",{staticClass:"product-block-2"},[s("div",{staticClass:"product-price"},[t._v(t._s(a.price)+" руб.")]),0!=a.old_price?s("div",{staticClass:"product-action-block"},[s("div",{staticClass:"old-price"},[t._v(t._s(a.old_price)+" руб.")]),s("div",{staticClass:"all-categories-count"},[t._v("-"+t._s(t.procent(a))+"%")])]):t._e()]),s("div",{staticClass:"product-block-3"},[s("div",{staticClass:"characteristic"},[s("div",{staticClass:"product-parameter-name"},[t._v("Цвета")]),s("div",{staticClass:"product-parameter-key colors"},t._l(a.colors,function(a,i){return i<4?s("div",{key:a.id,staticClass:"product-colors",style:t.getBack(a)}):t._e()}),0)])]),s("div",{staticClass:"product-block-4"},[s("div",{staticClass:"product-basket",on:{click:function(s){return t.openColor(a)}}},[s("img",{attrs:{src:t.domain+"/static/img/slider-icon-2.png"}}),s("div",{staticClass:"product-basket-name"},[t._v("В корзину")])]),s("div",{staticClass:"quick-order",on:{click:function(s){return t.quickOrder(a)}}},[s("img",{attrs:{src:t.domain+"/static/img/slider-icon-1.png"}}),s("div",{staticClass:"product-basket-name"},[t._v("Быстрый заказ")])])])])])}),0)],1),t.objects.length>t.pagination.max?s("div",{staticClass:"pagination-block"},[s("div",{staticClass:"pagination-name"},[t._v("Страницы:")]),t._l(t.pagination.countPages,function(a,i){return s("div",{class:["pagination-link",{"pagination-active-link":i==t.pagination.active}],on:{click:function(a){t.pagination.active=i}}},[t._v(t._s(a))])})],2):t._e()])])])},e=[function(){var t=this,a=t.$createElement,s=t._self._c||a;return s("div",{staticClass:"callback"},[s("div",{staticClass:"callback-name"},[t._v("Найти")])])},function(){var t=this,a=t.$createElement,s=t._self._c||a;return s("div",{staticClass:"callback"},[s("div",{staticClass:"callback-name"},[t._v("Сбросить фильтры")])])}],r=(s("6b54"),s("a481"),s("7f7f"),s("55dd"),s("28a5"),s("bc3a")),n=s.n(r),l=function(){var t=this,a=t.$createElement,s=t._self._c||a;return s("div",{staticClass:"callback-block"},[s("div",{staticClass:"callback-back"}),s("div",{staticClass:"callback-form-block"},[s("div",{staticClass:"callback-form"},[t.message?s("div",{staticClass:"callback-messge"},[t._v("Заявка оформлена, ожидайте звонка оператора.")]):t._e(),s("div",{staticClass:"callback-form-head",on:{click:function(a){return t.$parent.close()}}},[s("div",{staticClass:"name"},[t._v("Быстрый заказ товара")]),s("img",{attrs:{src:t.domain+"/static/img/close.png"}})]),s("div",{staticClass:"icon-border"}),s("div",{staticClass:"order-form-input-block"},[t._m(0),s("div",{staticClass:"wrap_select_block"},[s("div",{staticClass:"select_block",on:{click:function(a){t.color.active=!0}}},[s("div",{staticClass:"select-block-wrap-name"},[s("div",{staticClass:"active_select form-control active",style:t.color.img}),s("div",{staticClass:"active_select form-control"},[t._v(t._s(t.color.text))])]),s("div",{staticClass:"change"},[s("img",{attrs:{src:t.domain+"/static/img/arrow-top-bottom.png"}})])]),t.color.active?s("div",{staticClass:"select_elements"},t._l(t.color.objects,function(a){return s("div",{key:a.id,staticClass:"select_element",on:{click:function(s){return t.changeColor(a)}}},[s("div",{staticClass:"active_select form-control active",style:t.getBack(a)}),t._v("\n\t\t\t\t\t\t\t\t"+t._s(a.name)+"\n\t\t\t\t\t\t\t")])}),0):t._e()])]),s("div",{staticClass:"order-form-input-block"},[s("div",{staticClass:"order-form-input-head"},[s("div",{staticClass:"order-form-input-name"},[t._v("\n\t\t\t\t\t\t\tИмя *\n\t\t\t\t\t\t")]),s("div",{staticClass:"order-form-input-check"},[t.checkForms.name?s("img",{staticClass:"social",attrs:{src:t.domain+"/static/img/order-check.png"}}):s("img",{staticClass:"social",attrs:{src:t.domain+"/static/img/order-uncheck.png"}})])]),s("div",{staticClass:"wrap-order-form-input"},[s("input",{directives:[{name:"model",rawName:"v-model",value:t.name,expression:"name"}],staticClass:"order-form-input",attrs:{placeholder:"Степан"},domProps:{value:t.name},on:{input:function(a){a.target.composing||(t.name=a.target.value)}}})])]),s("div",{staticClass:"order-form-input-block"},[s("div",{staticClass:"order-form-input-head"},[s("div",{staticClass:"order-form-input-name"},[t._v("\n\t\t\t\t\t\t\tТелефон *\n\t\t\t\t\t\t")]),s("div",{staticClass:"order-form-input-check"},[t.checkForms.phone?s("img",{staticClass:"social",attrs:{src:t.domain+"/static/img/order-check.png"}}):s("img",{staticClass:"social",attrs:{src:t.domain+"/static/img/order-uncheck.png"}})])]),s("div",{staticClass:"wrap-order-form-input"},[s("input",{directives:[{name:"model",rawName:"v-model",value:t.phone,expression:"phone"}],staticClass:"order-form-input",attrs:{placeholder:"например +7(999)-999-99-99"},domProps:{value:t.phone},on:{input:function(a){a.target.composing||(t.phone=a.target.value)}}})])]),t._m(1),s("div",{class:["send-request",{active:t.checkForms.name&&t.checkForms.phone}],on:{click:t.createCallbaks}},[t._m(2)])])])])},d=[function(){var t=this,a=t.$createElement,s=t._self._c||a;return s("div",{staticClass:"order-form-input-head"},[s("div",{staticClass:"order-form-input-name"},[t._v("Доступные цвета для товара")])])},function(){var t=this,a=t.$createElement,s=t._self._c||a;return s("div",{staticClass:"order-form-input-block"},[s("div",{staticClass:"order-form-input-name"},[t._v("Комментарий")]),s("div",{staticClass:"order-form-textarea-block"},[s("div",{staticClass:"wrap-order-form-textarea"},[s("textarea",{staticClass:"order-form-textarea",attrs:{placeholder:"Просьба курьеру позвонить перед доставкой."}})])])])},function(){var t=this,a=t.$createElement,s=t._self._c||a;return s("div",{staticClass:"wrap-callback"},[s("div",{staticClass:"callback-background"},[s("div",{staticClass:"wrap-callback-background"})]),s("div",{staticClass:"callback"},[s("div",{staticClass:"callback-name"},[t._v("Заказать")])])])}],u={props:["product"],data:function(){return{color:{img:this.getBack(this.product.colors[0]),active:!1,text:this.product.colors[0].name,object:this.product.colors[0].id,objects:this.product.colors},domain:"http://localhost",name:"",phone:"",comments:"",checkForms:{name:!1,phone:!1},message:!1}},watch:{name:function(t){t.length?this.checkForms.name=!0:this.checkForms.name=!1},phone:function(t){11==t.replace(/\D+/gi,"").length?this.checkForms.phone=!0:this.checkForms.phone=!1}},methods:{getBack:function(t){return""==t.poster?{background:t.code}:{"background-image":"url('"+t.poster+"')"}},changeColor:function(t){this.color.img=this.getBack(t),this.color.object=t.id,this.color.active=!1,this.color.text=t.name},close:function(){this.$parent.close(),o.message=!1},createCallbaks:function(){var t=this;if(!t.checkForms.name||!t.checkForms.phone)return!1;t.message=!0;var a=new FormData;a.append("pid",t.product.id),a.append("cid",t.color.object),a.append("name",t.name),a.append("phone",t.phone),a.append("comments",t.comments),n.a.post(t.domain+"/shop/quick-order",a).then(function(t){console.log(t.data)}).catch(function(t){console.log(t)})}}},v=u,m=s("2877"),p=Object(m["a"])(v,l,d,!1,null,null,null),f=p.exports,g=function(){var t=this,a=t.$createElement,s=t._self._c||a;return s("div",{staticClass:"callback-block"},[s("div",{staticClass:"callback-back"}),s("div",{staticClass:"callback-form-block color-window"},[s("div",{staticClass:"callback-form"},[s("div",{staticClass:"callback-form-head",on:{click:function(a){return t.$emit("close-color")}}},[s("div",{staticClass:"name"},[t._v("Выберите цвет")]),s("img",{attrs:{src:t.domain+"/static/img/close.png"}})]),s("div",{staticClass:"icon-border"}),s("div",{staticClass:"order-form-input-block"},t._l(t.product.colors,function(a){return s("div",{key:a.id,staticClass:"select_element",on:{click:function(s){return t.addBasket(a.id)}}},[s("div",{staticClass:"active_select form-control active",style:t.getBack(a)}),t._v("\n\t\t\t\t\t\t"+t._s(a.name)+"\n\t\t\t\t\t")])}),0)])])])},h=[],b={props:["product"],data:function(){return{domain:"http://localhost"}},methods:{getBack:function(t){return""==t.poster?{background:t.code}:{"background-image":"url('"+t.poster+"')"}},addBasket:function(t){var a=this,s=new FormData;s.append("order",JSON.stringify({id:t,giftID:"",optionIDS:[]})),n.a.post(a.domain+"/shop/products/add-basket",s).then(function(t){location.reload()}).catch(function(t){console.log(t)}),this.$emit("close-color")}}},C=b,k=Object(m["a"])(C,g,h,!1,null,null,null),_=k.exports,x=s("c7e3"),y=s.n(x),w=(s("2760"),{name:"catalog-app",components:{callback:f,addbasket:_,RangeSlider:y.a},data:function(){return{valMin:0,valMax:0,staticMin:0,staticMax:0,avalible:!1,color:{active:!1,product:!1},activeProduct:!1,quickOrderOpen:!1,buttonIsActive:!1,buttonIsActive2:!1,domain:"http://localhost",sort:{activeName:"наименованию, a-z",active:!1,variant:[{id:1,name:"наименованию, a-z"},{id:2,name:"наименованию, z-a"},{id:3,name:"цене, от низкой к высокой"},{id:4,name:"цене, от высокой к низкой"}]},pagination:{max:11,countPages:0,active:0},category:!1,objects:[],manufacturer:{id:!1,name:"Выберите бренд",active:!1,objects:[]},categories:{}}},mounted:function(){this.$nextTick(function(){var t=this,a=document.location.pathname.split("/");t.category=a[a.length-1];var s={slug:t.category,min:0,max:0,avalible:!1,manufacturer:t.manufacturer.id};n.a.get(t.domain+"/shop/categories/get-products",{params:s}).then(function(a){var s=JSON.parse(a.data);t.objects=s.products,t.manufacturer.objects=s.manufacturers,t.categories=s.categories,t.objects.length>t.pagination.max&&(t.pagination.countPages=Math.ceil(t.objects.length/t.pagination.max)),t.staticMin=s.constMin,t.valMin=s.constMin,t.staticMax=s.constMax,t.valMax=s.constMax}).catch(function(t){console.log(t)})})},methods:{changeManufacturers:function(t,a){this.manufacturer.id=t,this.manufacturer.name=a,this.manufacturer.active=!1},getProducts:function(){var t=this,a={slug:this.category,min:this.valMin,max:this.valMax,avalible:this.avalible,manufacturer:this.manufacturer.id};n.a.get(t.domain+"/shop/categories/get-products",{params:a}).then(function(a){var s=JSON.parse(a.data);t.objects=s.products,t.objects.length>t.pagination.max&&(t.pagination.countPages=Math.ceil(t.objects.length/t.pagination.max))}).catch(function(t){console.log(t)})},openColor:function(t){var a=this;if(t.colors.length>1)a.color.active=!0,a.color.product=t;else{var s=new FormData;s.append("order",JSON.stringify({id:t.colors[0].article,giftID:"",optionIDS:[]})),n.a.post(a.domain+"/shop/products/add-basket",s).then(function(t){location.reload()}).catch(function(t){console.log(t)})}},closeColor:function(){this.color.active=!1,this.color.product=!1},getBack:function(t){return""==t.poster?{background:t.code}:{"background-image":"url('"+t.poster+"')"}},quickOrder:function(t){this.quickOrderOpen=!0,this.activeProduct=t},close:function(){this.quickOrderOpen=!1,this.activeProduct=!1},procent:function(t){return Math.ceil(100*(t.old_price-t.price)/t.old_price)},getPaginations:function(){this.objects.length>this.pagination.max&&(this.pagination.countPages=Math.ceil(this.objects.length/this.pagination.max))},getObjectID:function(t){for(var a=0;a<t.colors.length;a++)if(t.colors[a].default)return t.colors[a].id},getPrice:function(t){for(var a=0;a<t.length;a++)if(t[a].default)return this.formatPrice(t[a].price)},selectSort:function(t,a){switch(this.sort.activeName=a,this.sort.active=!this.sort.active,t){case 1:this.objects.sort(function(t,a){return t.name<a.name?-1:t.name>a.name?1:void 0});break;case 2:this.objects.sort(function(t,a){return t.name<a.name?-1:t.name>a.name?1:void 0}).reverse();break;case 3:this.objects.sort(function(t,a){return t.price-a.price});break;case 4:this.objects.sort(function(t,a){return a.price-t.price});break}},formatPrice:function(t){var a=t/1;return a.toString().replace(/\B(?=(\d{3})+(?!\d))/g,".")}}}),M=w,j=Object(m["a"])(M,c,e,!1,null,null,null),O=j.exports;i["a"].config.productionTip=!1,new i["a"]({render:function(t){return t(O)}}).$mount("#catalog-app")}});
//# sourceMappingURL=app.3864fe88.js.map