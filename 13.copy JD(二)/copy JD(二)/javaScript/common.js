function QRCodeShow(){
        document.getElementById("Login").classList.add("hide");
        document.getElementById("QR").classList.remove("hide");
}
function loginFormShow(){
        document.getElementById("Login").classList.remove("hide");
        document.getElementById("QR").classList.add("hide");
}

function checkbox(){
        var item_list = document.getElementById("item-list");
        var element_list =  item_list.children;
        for(var i=0;i<element_list.length;i++){
            if (element_list[i].firstElementChild.checked) {
                element_list[i].firstElementChild.checked = false;
            } else {element_list[i].firstElementChild.checked = true;}
            }
        }

function add(changeQuantity,p,s){
    var value  = parseInt(document.getElementById(changeQuantity).value);
    document.getElementById(changeQuantity).value=value+1;
    var price  = parseInt(document.getElementById(p).innerText.substring(1));
    var sum = parseInt(document.getElementById(s).innerText.substring(1));
    document.getElementById(s).innerText="￥"+(price + sum);
    var total = parseInt(document.getElementById("total").innerText);
    document.getElementById("total").innerText= total + price
}

function decrease(changeQuantity,p,s){
    var value  = parseInt(document.getElementById(changeQuantity).value);
    if(value>1){
        document.getElementById(changeQuantity).value=value-1;
        var price  = parseInt(document.getElementById(p).innerText.substring(1));
        var sum = parseInt(document.getElementById(s).innerText.substring(1));
        document.getElementById(s).innerText="￥"+(sum-price);
        var total = parseInt(document.getElementById("total").innerText);
        document.getElementById("total").innerText= total - price
    }else{
        alert("都小于1了,求不减")
    }
}

function tips(string){
    alert(string)
}