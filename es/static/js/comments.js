'use struct';

$(function(){
	
	$(".cust-sort-block").on('click', function(){
		
		if($(this).find(".cust-sort-by").hasClass('active')){
			$(this).find('.cust-sort-by').removeClass('active');
		}else{
			$(this).find('.cust-sort-by').addClass('active');
		}
		
	});
	
	$(".add-comments").on('click', function(){
		$('#comments-form').css('display', 'block');
	});
	
	$('#comments-form .callback-form-head').on('click', function(){
		$('#comments-form').css('display', 'none');
	});
	
	let rating = 1;
	$(".comments-rating.set-rating .star").on('click', function(){
		
		let active = +$(this).attr("data-rating");
		rating = active;
		
		$(".comments-rating.set-rating .star").each(function(i, e){
			if(i >= active){
				$(e).attr('src', '/static/img/raiting.png');
			}else{
				$(e).attr('src', '/static/img/raiting-fill.png');
			}
		});
	});
	
	$(".send-request.active.comment").on('click', function(){
		
		let user_name 		= $("#user-name").val();
		let user_city 		= $("#user-city").val();
		let user_positive 	= $("#user-positive").val();
		let user_negative 	= $("#user-negative").val();
		let user_comment 	= $("#user-comment").val();
		
		$.post("/shop/add-main-comments", {
			
			'user_name': 		user_name,
			'user_city': 		user_city,
			'rating': 			rating,
			'user_positive': 	user_positive,
			'user_negative': 	user_negative,
			'user_comment': 	user_comment,
			
			}, function(data){
				
				
				data = JSON.parse(data);
				
				if(!data.response){
					$('.err').text(data.err);
				}else{
					
					$("#user-name").val('');
					$("#user-city").val('');
					$("#user-positive").val('');
					$("#user-negative").val('');
					$("#user-comment").val('');
		
					location.reload();
				}

			}
		);
		
	});
	
	
});
	





