function addtocart(item){
    let products = window.sessionStorage.getItem('products')
    if (products != undefined){
        let productlist = JSON.parse(products)
        productlist.indexOf(item) === -1 ? productlist.push(item) : console.log("This item already exists");
        console.log(productlist)
        window.sessionStorage.setItem('products',JSON.stringify(productlist))
    }else{
        let productlist = [item]
        console.log(productlist)
        window.sessionStorage.setItem('products',JSON.stringify(productlist))
    }
}
function logout(){
    sessionStorage.removeItem('products')
    window.location = '/logout'
}


