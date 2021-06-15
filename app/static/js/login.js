function goRegister(){
    window.location = '/static/html/register.html';
}

function login(){
  console.log("Login User");
  var username = $('#username').val();
  var password = $('#password').val();
  console.log("DATA", username, password);
  var credentials = {'username':username, 'password':password};
  $.post({
      url: '/authenticate',
      type: 'post',
      dataType: 'json',
      contentType: 'application/json',
      success: function(data){
          console.log("Authenticated!");
          alert("Authenticated");
          window.location='/static/html/catalogo.html'
      },
      data: JSON.stringify(credentials)
  });
}
