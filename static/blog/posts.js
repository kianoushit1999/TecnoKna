$(document).ready(function (){
    var flag = true;
    $('.card').hover(function (){
        $(this).addClass('zoom')
        console.log('added affect')
    })
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
})