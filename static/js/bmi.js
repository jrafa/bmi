$(function() {
    $('button').click(function(event) {
        event.preventDefault();
        var weight = $('#weight').val();
        var height = $('#height').val();
        $.ajax({
            url: '/bmi',
            data: $('form').serialize(),
            type: 'POST',
            dataType: 'json',
            success: function(response, bmi) {

                if (response.errors) {
                    $("#msg").addClass("errors").removeClass("result").text(response.errors);
                }
                else {
                    $("#msg").addClass("result").removeClass("errors").text('Result: ' + response.bmi + ' ' +response.answer);
                }

            },
            error: function(jqXHR, textStatus, errorThrown) {
                console.log(jqXHR, textStatus, errorThrown);
            }
        });
    });
});
