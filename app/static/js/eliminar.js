function eliminar_producto(){

  /*  var nombre = $('#nombre').val();
    var credentials = {'nombre':nombre};
    $.delete({
        url: 'http://34.213.47.88:80/nombre',
        type: 'delete',
        dataType: 'json',
        contentType: 'application/json',
        success: function(data){
	console.log("Deleted");
        },
        data: JSON.stringify(credentials)
    });

*/


    var nombre = $('#nombre').val()

$.ajax({
    url: '/http://34.213.47.88:80/nombre',
    type: 'DELETE',
    success: function(result) {
        console.log(result)
    }


});

}
