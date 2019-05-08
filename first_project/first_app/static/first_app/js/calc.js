$(document).ready(function(){

    $("#add").click(function(){
        calculate("add");
    })

    $("#subtract").click(function(){
        calculate("subtract");
    })

    $("#multiply").click(function(){
        calculate("multiply");
    })

    $("#divide").click(function(){
        calculate("divide");
    })

    $("#clear").click(function(){
        $("#input1").val("");
        $("#input2").val("");
        $("#result").html("");
    })

})

function calculate(methodName){
    var csrfmiddlewaretoken = readCSRF();
    var number1 = $("#input1").val();
    var number2 = $("#input2").val();
    $.post("/calc",
    {
        csrfmiddlewaretoken: csrfmiddlewaretoken,
        methodName : methodName,
        number1    : number1,
        number2    : number2
    },
    function(mydata, status){
        var xml   = $(mydata);
        var result  = xml.find("result").text();
        $("#result").html(result);
        if(xml.find("code").text()!=0){
            alert (xml.find("msg").text());
        }
    }); // end post
}

function readCSRF(){
    return $("#background").find("[name='csrfmiddlewaretoken']").val();
}