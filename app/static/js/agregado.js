function create_product(){
    console.log("Create Product");
    var categoria = $('#categoria').val();
    var nombre = $('#nombre').val();
    var descripcion = $('#descripcion').val();
    var precio = $('#precio').val();

    var credentials = {'categoria':categoria, 'nombre':nombre, 'descripcion':descripcion, 'precio':precio};
    $.post({
        url: '/create',
        type: 'post',
        dataType: 'json',
        contentType: 'application/json',
        success: function(data){
            console.log("Created successfully!");
            alert("Created successfully!!!");
            //window.location='/static/html/catalogo.html'
        },
        data: JSON.stringify(credentials)
    });
}
