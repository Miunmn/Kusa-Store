$(document).ready(function(){
	$('.category_item').click(function(){
		$('.category_item').removeClass('ct_item-active');
		$(this).addClass('ct_item-active');
	});
});

function get_productos(){
	$('#lista_productos').empty();
	console.log("Mostrando catalogo de productos");
	$.getJSON( "/productos", function(data){
		get_current();
		let i=0;
		$.each(data, function(){
			var div='<div class="product-item" category="category_" id="_id" ><img src="../images/vista.jpg" ><a>nombre</a><a>Precio: _precio</a></div>';
			div = div.replace("category_", data[i]['categoria']);
			div = div.replace("_id", data[i]['nombre']);
			div = div.replace("vista", data[i]['nombre']);
			div = div.replace("nombre", data[i]['nombre'].replace("_"," ").replace("_"," ").replace("_"," ").replace(/nh/,"ñ").toUpperCase());
			div = div.replace("_precio",data[i]['precio'])
			$('#lista_productos').append(div);
			i=i+1;
		})
	});
}

function get_current(){
	$('#inicio_catalogo').empty();
	console.log("Usuario logueado"); //Usuario logueado
	$.getJSON("/current", function(data){
		console.log(data['username']);
		var div = '<div class="row p-1" id="current" style="margin-left:59rem; background-color:yellow;"><div class="card w-100"><div class="card-body" id="cuerpo"><h5 class="card-title"><b>Welcome @username</b></h5><p class="card-text">nombre apellido</p></div></div></div>';
		div = div.replace('username', data['username'])
		div = div.replace("nombre", data['name'])
		div = div.replace("apellido", data['fullname'])
		$('#inicio_catalogo').append(div);
	  });
}

function logout(){
	$.getJSON("/logout", function(data){
	  alert(data['msg']);
	  window.location = '/static/html/login.html';
	})
}

function get_frutasyverduras(){
	$('#lista_productos').empty();
	console.log("Mostrando catalogo de frutas y verduras");
	$.getJSON( "/frutasyverduras", function(data){
		let i=0;
		$.each(data, function(){
			var div='<div class="product-item" category="category_" id="_id" ><img src="../images/vista.jpg" ><a>nombre</a><a>Precio: _precio</a></div>';
			div = div.replace("category_", data[i]['categoria']);
			div = div.replace("_id", data[i]['nombre']);
			div = div.replace("vista", data[i]['nombre']);
			div = div.replace("nombre", data[i]['nombre'].replace("_"," ").replace("_"," ").replace("_"," ").toUpperCase());
			div = div.replace("_precio",data[i]['precio'])
			$('#lista_productos').append(div);
			i=i+1;
		})
	});
}

function get_carnes(){
	$('#lista_productos').empty();
	console.log("Mostrando catalogo de carnes");
	$.getJSON( "/carnes", function(data){
		let i=0;
		$.each(data, function(){
			var div='<div class="product-item" category="category_" id="_id" ><img src="../images/vista.jpg" ><a>nombre</a><a>Precio: _precio</a></div>';
			div = div.replace("category_", data[i]['categoria']);
			div = div.replace("_id", data[i]['nombre']);
			div = div.replace("vista", data[i]['nombre']);
			div = div.replace("nombre", data[i]['nombre'].replace("_"," ").replace("_"," ").replace("_"," ").toUpperCase());
			div = div.replace("_precio",data[i]['precio'])
			$('#lista_productos').append(div);
			i=i+1;
		})
	});
}

function get_bebidas(){
	$('#lista_productos').empty();
	console.log("Mostrando catalogo de bebidas");
	$.getJSON( "/bebidas", function(data){
		let i=0;
		$.each(data, function(){
			var div='<div class="product-item" category="category_" id="_id" ><img src="../images/vista.jpg" ><a>nombre</a><a>Precio: _precio</a></div>';
			div = div.replace("category_", data[i]['categoria']);
			div = div.replace("_id", data[i]['nombre']);
			div = div.replace("vista", data[i]['nombre']);
			div = div.replace("nombre", data[i]['nombre'].replace("_"," ").replace("_"," ").replace("_"," ").toUpperCase());
			div = div.replace("_precio",data[i]['precio'])
			$('#lista_productos').append(div);
			i=i+1;
		})
	});
}

function get_limpieza(){
	$('#lista_productos').empty();
	console.log("Mostrando catalogo de limpieza");
	$.getJSON( "/limpieza", function(data){
		let i=0;
		$.each(data, function(){
			var div='<div class="product-item" category="category_" id="_id" ><img src="../images/vista.jpg" ><a>nombre</a><a>Precio: _precio</a></div>';
			div = div.replace("category_", data[i]['categoria']);
			div = div.replace("_id", data[i]['nombre']);
			div = div.replace("vista", data[i]['nombre']);
			div = div.replace("nombre", data[i]['nombre'].replace("_"," ").replace("_"," ").replace("_"," ").toUpperCase());
			div = div.replace("_precio",data[i]['precio'])
			$('#lista_productos').append(div);
			i=i+1;
		})
	});
}
