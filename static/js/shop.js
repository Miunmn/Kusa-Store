function logout() {
    localStorage.removeItem('products')
    window.location = '/logout'
}

function comprar(productoname) {
    try {
        fetch('/buy', {
            method: 'POST',
            body: JSON.stringify({
                "producto": productoname
            }),
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(function (response) {
            return response.json()
        }).then(function (response) {
            console.log("response: ", response['message'])
            setTimeout(function () {
                UIkit.notification({
                    message: response['message'],
                    status: 'danger'
                })
            }, 1000)
        }).catch(function (response) {
            console.log("response: ", response)
            UIkit.notification({
                message: response.message,
                status: 'danger'
            })
        });
    } catch (exception) {
        console.log(exception)
    }



}