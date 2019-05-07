$(document).ready(function(){

    $("#add").click(function(){
        var csrfmiddlewaretoken = readCSRF();
        var number1 = $("#input1").val();
        var number2 = $("#input2").val();
        $.post("/add",
        {
            csrfmiddlewaretoken: csrfmiddlewaretoken,
            number1   : number1,
            number2   : number2
        },
        function(mydata, status){

            var xml   = $(mydata);
            var result  = xml.find("result").text();
            $("#result").html(result);
        }); // end post
    })

    $("#subtract").click(function(){
        var csrfmiddlewaretoken = readCSRF();
        var number1 = $("#input1").val();
        var number2 = $("#input2").val();
        $.post("/subtract",
        {
            csrfmiddlewaretoken: csrfmiddlewaretoken,
            number1   : number1,
            number2   : number2
        },
        function(mydata, status){
            var xml   = $(mydata);
            var result  = xml.find("result").text();
            $("#result").html(result);
        }); // end post
    })

    $("#multiply").click(function(){
        var csrfmiddlewaretoken = readCSRF();
        var number1 = $("#input1").val();
        var number2 = $("#input2").val();
        $.post("/multiply",
        {
            csrfmiddlewaretoken: csrfmiddlewaretoken,
            number1   : number1,
            number2   : number2
        },
        function(mydata, status){
            var xml   = $(mydata);
            var result  = xml.find("result").text();
            $("#result").html(result);
        }); // end post
    })

    $("#clear").click(function(){
        $("#input1").val("");
        $("#input2").val("");
        $("#result").html("");
    })


})

function readCSRF(){
    return $("#background").find("[name='csrfmiddlewaretoken']").val();
}