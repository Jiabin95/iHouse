var timerRef;

function doSomething() {
    var iurl = window.location.href;
        $.ajax(iurl, {
            success: function(data) {
                $("#refresh_this").html(data);
                
            },
        });
}



$(function() {
    clearInterval(timerRef);
    timerRef = setInterval(doSomething,3000);
});




var frm = $('#add_story_form');
    frm.submit(function () {
        $.ajax({
            type: frm.attr('method'),
            url: window.location.href,
            data: frm.serialize(),
            success: function (data) {
                $("#refresh_this").html(data);
                document.getElementById("context").value = "";
            },
            error: function(data) {
                $("#card").html("<h1>You did not login yet.</h1>");
            }
        });
        return false;
    });
    