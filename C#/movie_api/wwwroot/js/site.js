// Write your Javascript code.
$(document).ready(function(){
    $('button').click(function(){
        var title = $('input').val()
        $.post("/movie/"+title, "json");
    });
})