
function actualizar(){
    console.log("aaaaaaaaaaaaaaaa")
    let lista_li = document.getElementsByClassName("productochecklist")
    console.log(lista_li.length)
    for(let i = 0 ; i < lista_li.length; i++){
        //let childmenos  = lista_li[i].getElementsByTagName("a")[0]
        //let childmas  = lista_li[i].getElementsByTagName("a")[1]
        //console.log(lista_li[i])
        //childmas.addEventListener("onclik",agregar(lista_li[i].dataset.producto))
        //console.log(lista_li[i].dataset.producto, "HOLAAA" )
        //childmenos.addEventListener("onclik",quitar(lista_li[i].dataset.producto))
    }
}


function quitar(name){
    console.log(name)
}


function agregar(name){
    console.log(name)
}

function minus(name){
    let a_ = document.createElement("a")

    a_.setAttribute("onclick","quitar("+name+")")

    let span_ = document.createElement("span")
    span_.className = "uk-icon"
    span_.setAttribute("uk-icon","icon: minus; ratio: 1;")
    a_.appendChild(span_)
    return  a_
}

function plus(name){
    let a_ = document.createElement("a")
    //a_.setAttribute("onclick","agregar("+name+")")
    //a_.addEventListener("onclick",agregar(name))
    a_.setAttribute("name","mas")
    console.log(name)


    a_.setAttribute("onclick","agregar("+name+")")
    let span_ = document.createElement("span")
    span_.className = "uk-icon"
    span_.setAttribute("uk-icon","icon: plus; ratio: 1;")
    a_.appendChild(span_)
    return  a_
}

window.onload = function() {
    let products = localStorage.getItem('products')
    if (products != undefined){
        let productlist = JSON.parse(products)
        for(let i = 0 ; i < productlist.length; i++){
            let div_carrito = document.getElementById('carrito')
            let li_ = document.createElement("li")
            let badge = document.createElement("span")
            badge.className = "uk-badge"
            badge.textContent = productlist[i]
            badge.style = "font-size: 90%;"
            li_.appendChild(badge)
            //li_.setAttribute("value","productochecklist")
            //li_.className = "productochecklist"
            li_.setAttribute ("class","productochecklist")
            li_.setAttribute("data-producto",productlist[i])
            //li_.appendChild(minus(productlist[i]))
            //li_.appendChild(plus(productlist[i]))
            div_carrito.appendChild(li_)
        }
    }
}

function updatecarrito(newelement){
    let div_carrito = document.getElementById('carrito')
    let li_ = document.createElement("li")
    let badge = document.createElement("span")
    badge.className = "uk-badge"
    badge.textContent = newelement
    badge.style = "font-size: 90%;"

    //li_.setAttribute("class", "productochecklist")
    //li_.setAttribute("data-producto",newelement)
    //li_.appendChild(minus(newelement))
    //li_.appendChild(plus(newelement))
    div_carrito.appendChild(li_)
    li_.appendChild(badge)
    li_.setAttribute("class","productochecklist")    
    actualizar()
}

function addtocart(item){
    let products = localStorage.getItem('products')
    if (products != undefined){
        let productlist = JSON.parse(products)
        if (productlist.indexOf(item) === -1){
            console.log(item)
            productlist.push(item)
        }
        else{
            console.log("This item already exists");
        }
     
        localStorage.setItem('products', JSON.stringify(productlist))
        //updatecarrito(item)
    }else{
        let productlist = [item]
        updatecarrito(item)
        console.log(productlist)
        localStorage.setItem('products', JSON.stringify(productlist))
    }
}
function logout(){
    localStorage.removeItem('products')
    window.location = '/logout'
}
function findduplicates(productlist, item){
    var indexes = [], i = -1;
    while ((i = productlist.indexOf(item, i+1)) != -1){
        indexes.push(i);
    }
    return indexes.length;
}


function comprar(){
    let payload_ = {}
    let products = localStorage.getItem('products')
    if (products != undefined){
        let productlist = JSON.parse(products)
        let productos = []
        for(let i = 0 ; i < productlist.length; i++){
            let obj = {
                'name': productlist[i],
                'quantity': findduplicates(productlist, productlist[i])
            }
            productos.push(obj)
        }
        console.log(payload_)
        try{
            fetch('/buy', {
                method: 'POST',
                body: JSON.stringify(productos),
                headers: {
                    'Content-Type': 'application/json'
                }
            }).then(function(response){
                return response.json()
            }).then(function (response){
                console.log("response: ",response['message'])
                setTimeout(function(){
                    UIkit.notification({
                    message: response['message'],
                    status: 'danger'
                    })
                }, 1000)
            }).catch(function (response){
                console.log("response: ",response)
                UIkit.notification({
                    message: response.message,
                    status: 'danger'
                    })
            });
    }catch (exception)
    {
        console.log(exception)
    }
    }


}