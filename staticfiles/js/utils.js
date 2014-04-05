// pseudo-ajax
var create_data = function(){
	var result = [];
	var wide = 'images/wide1.jpg';
	var port = 'images/port1.jpg';
	var port_tall = 'images/port-tall1.jpg';
	var result = [wide, port, port_tall, wide, port, wide, port, port];
	return result;
}

var sum = function(args, index){
	var sum = 0;
	if(index == 0){
		sum = 0;
	}
	else if(index > 0){
		for(var i=0; i<index; i++){
			sum += args[i];
		}
	}
	return sum
}

var load_images = function () {
	var articles = document.getElementsByClassName('content content__article-container');
	// debug
	console.log('articles length:' + articles.length);
	// end debug
	var images = create_data();
	if(articles.length > images.length){
		articles.slice = Array.prototype.slice;
		var target_articles = articles.slice(0, images.length);
		for(var i=0; i < target_articles.length;i++){
			target_articles[i].getElementsByClassName('article image')[0].src = images[i];
		}
	}
}

var alerting_articles_metrics = function(){
	var containers = document.getElementsByClassName('content content__article-container');
	var get_params = function(el){
		var rect = el.getBoundingClientRect();
		// end debug
		alert(el.className + ':' + parseInt(rect.width) + ':' + parseInt(rect.height) + '\r\n');
		if(el.children.length > 0){
			get_params(el.children[0]);
		}
	}
	for(var i=0; i<3; i++){
		try{
			get_params(containers[i]);
		}
		catch(err){
			alert(err.message);
		}
	}
}