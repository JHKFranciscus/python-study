$("#loadProductButton").on("click", function(){
    $.ajax({
        url: "./products.json",
        type: "GET",
        success: function(response){
            const product = response[1];
            const name = product.name;
            const price = product.price;

            $("#productName").text(name);
            $("#productPrice").text(price);

            console.log(response);
            console.log(response[1]);
            console.log(response[1].price);
        }
    });
});