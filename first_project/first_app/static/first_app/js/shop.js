$(document).ready(function(){

    $(".trashIcon").click(function(){
        var csrfmiddlewaretoken = readCSRF();
        var productId = $(this).attr("productId");
        $.post("/delete_product_data",
        {
            csrfmiddlewaretoken: csrfmiddlewaretoken,
            productId    : productId,
        },
        function(mydata, status){
        }); // end post
    })

})

function readCSRF(){
    return $("#productTable").find("[name='csrfmiddlewaretoken']").val();
}