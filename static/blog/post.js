$(document).ready(function () {
    var flag = true;
    $('#left-bottom-info').click(function () {
        $('#pop_over').slideToggle();
        $('#foo').addClass('rotate');
        if(flag){
            $('#foo').addClass('rotate');
            $('#foo').removeClass('rotate-reset');
            flag=false
        }else{
            $('#foo').removeClass('rotate');
            $('#foo').addClass('rotate-reset');
            flag=true
        }
    });
});