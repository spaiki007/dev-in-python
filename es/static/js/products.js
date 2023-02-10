'use struct';

$(function(){

	//инициализируем слайдер изображений под основным изображением
	function init(){
		
		sliders = [];
		
		$(".slider-images > div").each(function(indx, element){
			sliders.push({
				'id': $(element).attr("data-image-id"),
				'src': $(element).find('.pagination-image').attr("src"),
				'active': false,
				'visible': false,
			});
		});
		
		
		$(sliders).each(function(indx, element){
			indx += 1
			if(indx == 1){
				element.active = true;
			}
			if(indx <= visible_elements){
				element.visible = true;
			}
		});
		
		eachSlider(sliders[0].src);
	}

	//слайдер изображений под основным изображением
	function eachSlider(src){
		
		$(sliders).each(function(i, sElement){
			$(".slider-images > div").each(function(i2, element){
				let elementID = $(element).attr("data-image-id");
				if(sElement.id == elementID){
					
					if(sElement.active){
						$(element).addClass('visible').addClass('active').find('.slider-active').addClass('active');
					}else{
						$(element).removeClass('visible').removeClass('active').find('.slider-active').removeClass('active');
					}
					
					if(sElement.visible){
						$(element).addClass('visible');
					}else{
						$(element).removeClass('visible');
					}

				}
			});
		});
		
		$("#main-img").animate({left: '100%', opacity: '0'}, 250, function(){
			$("#main-img").attr('src', src);
		}).animate({left: '-100%'}, 0).delay(100).animate({left: '0%', opacity: '1'}, 500);

	}
	
	//инициализируем
	let visible_elements = 2;
	
	let display_width = $('body').width();
	if(display_width >= 1200){
		visible_elements = 4;
	}
	
	let sliders = [];
	
	init();
	
	//кликаем на изображение в пагинации
	$("body").on('click', '.product-pagination-sub-images', function(){
		if($(this).hasClass('active')) return false;
		
		let thisID = $(this).attr("data-image-id");
		let src = "";
		
		
		$(sliders).each(function(indx, element){
			if(element.id == thisID){
				element.active = true;
				src = element.src;
			}else{
				element.active = false;
			}
		});
		
		eachSlider(src);
	});
	
	//кликаем на кнопку вперед
	$("#images-next").on('click', function(){
		
		//вычисляем текущий активный элемент
		let this_active = 0;
		$(sliders).each(function(indx, element){
			if(element.active){
				this_active = indx;
			}
		});
		
		//вычисляем количество скрытых элементов справа
		let right_hidden = [];
		$(sliders).each(function(indx, element){
			if(indx >= this_active && !element.visible){
				right_hidden.push(element.id);
			}
		});
		
		//если нету справа скрытых элементов то ни чего не делаем
		if(!right_hidden.length) return false;
		
		//вычисляем количество видимых элементов слево
		let left_visible = [];
		$(sliders).each(function(indx, element){
			if(indx <= this_active && element.visible){
				left_visible.push(element.id);
			}
		});

		//устанавливаем активный элемент в неактивное состояние
		$(sliders).each(function(indx, element){
			if(this_active == indx){
				element.active = false;
			}
		});
		
		//если слева есть видимые елементы то берем поледний из них и делаем его неактивным 
		//иначе берем текуй элемент и делаем его неактивным
		if(left_visible.length){
			$(sliders).each(function(indx, element){
				if(left_visible[0] == element.id){
					element.visible = false;
				}
			});
		}else{
			sliders[this_active].visible = false
		}
		
		let src = "";
		
		let new_active = 0;
		$(sliders).each(function(indx, element){
			
			//устанавливаем слудующий активный элемент
			if(this_active == indx){
				new_active = indx+1;	
			}
			
		});

		$(sliders).each(function(indx, element){
			
			if(new_active == indx){
				element.active 	= true;
				src = element.src;
			}
			
		});

		$(sliders).each(function(indx, element){
			//делаем первый элемент справа видимым
			if(right_hidden[0] == element.id){
				element.visible = true;
			}
		});
		
		eachSlider(src);
		
	});
	
	//кликаем на кнопку назад
	$("#images-prev").on('click', function(){

		//вычисляем текущий активный элемент
		let this_active = 0;
		$(sliders).each(function(indx, element){
			if(element.active){
				this_active = indx;
			}
		});
		
		//вычисляем количество скрытых элементов слева
		let left_hidden = [];
		$(sliders).each(function(indx, element){
			if(indx <= this_active && !element.visible){
				left_hidden.push(element.id);
			}
		});
		
		//если слева нету скрытых элементов то ни чего не делаем
		if(!left_hidden.length) return false;
		
		
		//вычисляем количество видимых элементов слева
		let right_visible = [];
		$(sliders).each(function(indx, element){
			if(indx >= this_active && element.visible){
				right_visible.push(element.id);
			}
		});

		//устанавливаем активный элемент в неактивное состояние
		$(sliders).each(function(indx, element){
			if(this_active == indx){
				element.active = false;
			}
		});
		
		//если слева есть видимые елементы то берем поледний из них и делаем его неактивным 
		//иначе берем текуй элемент и делаем его неактивным
		if(right_visible.length){
			$(sliders).each(function(indx, element){
				if(right_visible[right_visible.length-1] == element.id){
					element.visible = false;
				}
			});
		}else{
			sliders[this_active].visible = false
		}
		
		let src = "";
		
		let new_active = 0;
		$(sliders).each(function(indx, element){
			//устанавливаем следующий активный элемент
			if(this_active == indx){
				new_active = indx-1;	
			}
		});
		
		$(sliders).each(function(indx, element){
			if(new_active == indx){
				element.active 	= true;
				src = element.src;
			}
		});

		$(sliders).each(function(indx, element){
			//делаем послений скрытый элемент слева видимым
			if(left_hidden[left_hidden.length-1] == element.id){
				element.visible = true;
			}
		});
		
		eachSlider(src);
		
	});
	
	function changeColor(){
		
		$(".main-category-select.x320 .colors").animate({opacity: "0"}, 100);
		
		let articleID 	= $(this).attr("data-article-id");
		let articleName = $(this).attr("data-article-name");
		
		$('#article').text(articleName);
		
		let cid = $(this).attr("data-color-id");
		
		$.get("/shop/images/get", { cid: cid }, function(response){
			let objects = JSON.parse(response.objects);
			
			//если количество изображение больше чем в слайдере
			if(objects.length > sliders.length){

				let count = objects.length - sliders.length;
				for(let i=0; i<count; i++){
					$(".slider-images").append(`
						<div class="product-pagination-sub-images" data-image-id="">
							<img src="/static/img/product-slider-arrow-top.png" class="slider-active">
							<img class="pagination-image" src="">
						</div>
					`);
				}

				$(".slider-images .product-pagination-sub-images").each(function(indx, element){
					$(element).attr('data-image-id', objects[indx].id).find('.pagination-image').attr('src', objects[indx].path);
				});

			}
			
			//если количество изображение меньше чем в слайдере
			if(objects.length < sliders.length){

				let count_images = $(".slider-images .product-pagination-sub-images").length - (sliders.length - objects.length);
				
				$(".slider-images .product-pagination-sub-images").each(function(indx, element){
					if(indx >= count_images){
						$(element).remove();
					}
				});
				
				$(".slider-images .product-pagination-sub-images").each(function(indx, element){
					$(element).attr('data-image-id', objects[indx].id).find('.pagination-image').attr('src', objects[indx].path);
				});
	
			}
			
			//если количество изображений равно
			if(objects.length == sliders.length){
				$(".slider-images .product-pagination-sub-images").each(function(indx, element){
					$(element).attr('data-image-id', objects[indx].id).find('.pagination-image').attr('src', objects[indx].path);
				});
			}
			
			init();
			
		});

		$(".wrap-advantages-images .advantages-images").removeClass("active");
		$(this).addClass("active");
		
		$(".wrap-advantages-images .advantages-color").find(".advantages-color-active").removeClass("true");
		$(this).find(".advantages-color-active").addClass("true");
		
	}


	//кликаем на цвета в десктопе
	$(".wrap-advantages-images .advantages-images").on('click', changeColor);
	
	//кликаем на цвета в мобилке
	$(".main-category-select.x320 .name").on('click', function(){
		$(".main-category-select.x320 .colors").animate({opacity: "1"}, 100);
	});
	
	$(".main-category-select.x320 .color-block").on('click', changeColor);

	
	$('.slider-advantages-images').slick({
		dots: false,
		infinite: false,
		speed: 300,
		slidesToShow: 1,
		centerMode: true,
		variableWidth: true,
		
		responsive: [
		{
			breakpoint: 320,
				settings: {
					slidesToShow: 1,
					slidesToScroll: 1,
					infinite: false,
				}
		},

		]
		
	});
	
	$('.product-cart-advantages .slick-arrow').css('display', 'none');
	
	$('#color-next').on('click', function(){
		$('.slider-advantages-images .slick-next.slick-arrow').click();
	});
	
	$('#color-prev').on('click', function(){
		$('.slider-advantages-images .slick-prev.slick-arrow').click();
	});


	//slider pickings
	$('.slider-pickings-images').slick({
		dots: false,
		infinite: true,
		speed: 300,
		slidesToShow: 1,
		centerMode: true,
		variableWidth: true,
	});
	
	$('.slider-pickings-images .slick-arrow').css('display', 'none');

	$('#pickings-next').on('click', function(){
		$('.slider-pickings-images .slick-next.slick-arrow').click();
	});
	
	$('#pickings-prev').on('click', function(){
		$('.slider-pickings-images .slick-prev.slick-arrow').click();
	});
	
	//options
	let options = [];
	$('.product-additional-option').on('click', function(){
		
		let id = $(this).attr('data-id');
		if($(this).find('.filter-checkbox-check').hasClass('check-active')){
			
			$(this).find('.filter-checkbox-check').removeClass('check-active');
			
			for(let i=0; i<options.length; i++){
				if(options[i] == id){
					options.splice(1, i);
				}
			}
			
		}else{
			
			$(this).find('.filter-checkbox-check').addClass('check-active');
			options.push(id);
			
		}
		
	});

	//gifts
	//кликаем на выберите подарок
	let giftID = $('#stocks-default').attr('data-id') || false;
	$(".stocks .filters-select").on('click', function(){
		if($(this).parent().find('.gifts-block').hasClass('active')){
			$(this).parent().find('.gifts-block').removeClass('active');
		}else{
			$(this).parent().find('.gifts-block').addClass('active');
		}
	});
	
	$(".stocks .gift").on('click', function(){
		giftID = $(this).attr('data-id');
		$('#stocks-default').text($(this).attr('data-name')).attr('data-id', $(this).attr('data-id'));
		$(this).parent().removeClass('active');
	});
	
	$("#add-basket").on('click', function(){
		
		let cid = $('#article').attr('data-cid');
		let order 	= {id: cid, giftID: giftID, optionIDS: options};

		$.post("/shop/products/add-basket", {order: JSON.stringify(order)}, function(response){
			response = JSON.parse(response.response);
			if(response){
				location.reload();
			}
		});
		
	});
	
	
	//tabs
	let active_tab = 1;
	$(".product-tab-name").on('click', function(){
		
		if($(this).parent().hasClass('tabs-block')){
			$('.tabs-mobile.filters-select.x320 .main-category-products-bottom-name').text($(this).text());
			$(this).parent().removeClass('active');
		}
		
		let id_tab = $(this).attr('data-id');	
		if(active_tab != id_tab){
			
			$(".product-tab-name").removeClass('active');
			$(this).addClass('active');
			
			active_tab = id_tab;
			$(".product-content .content").fadeOut(250).delay(50).parent().find("[data-id='"+id_tab+"']").fadeIn(250);
		}
		
	});
	
	$(".product-feat-all").on('click', function(){
		
		let id_tab = $(this).attr('data-id');
		
		if(active_tab != id_tab){
			
			$(".product-tab-name").removeClass('active');
			$('.product-tab-name[data-id=' + id_tab + ']').addClass('active');
			
			active_tab = id_tab;
			$(".product-content .content").fadeOut(250).delay(50).parent().find("[data-id='"+id_tab+"']").fadeIn(250);
		}

	});
	
	$(".tabs-mobile .main-category-select").on('click', function(){
		if($(this).parent().find('.tabs-block').hasClass('active')){
			$(this).parent().find('.tabs-block').removeClass('active');
		}else{
			$(this).parent().find('.tabs-block').addClass('active');
		}
	});
	
	
	$(".quick-order").on('click', function(){
		$('.callback-block.static').css('display', 'block');
	});
	
	$(".callback-form-head.close").on('click', function(){
		$('.callback-block.static').css('display', 'none');
	});
	
	$(".send-request.static").on('click', function(){
		
		let article = $('#article').attr('data-article-id');
		let name 	= $('#quick-order-name').val();
		let phone 	= $('#quick-order-phone').val();
		let comment = $('#quick-order-comment').val();
		
		
		$.post('/shop/quick-order', {
			'article': article,
			'name': name,
			'phone': phone,
			'comments': comment,
		}, function(response){
			response = JSON.parse(response.response);
			if(response){
				location.reload();
			}
		});
		
		$('.callback-block.static').css('display', 'none');

	});
	
	
});
	





