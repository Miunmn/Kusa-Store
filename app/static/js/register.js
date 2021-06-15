function register(){
    console.log("Register User");
    var email = $('#email').val();
    var name = $('#name').val();
    var fullname = $('#fullname').val();
    var username = $('#username').val();
    var password = $('#password').val();
    //console.log("DATA", username, password);
    var credentials = {'email':email, 'name':name, 'fullname':fullname, 'username':username, 'password':password};
    $.post({
        url: '/signup',
        type: 'post',
        dataType: 'json',
        contentType: 'application/json',
        success: function(data){
            console.log("Register success!");
            alert("Register success!!!");
            //window.location='/static/html/catalogo.html'
        },
        data: JSON.stringify(credentials)
    });
}