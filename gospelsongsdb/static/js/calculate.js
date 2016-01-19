function currencyFormat(nStr) {
    nStr += '';
    x = nStr.split('.');
    x1 = x[0];
    x2 = x.length > 1 ? '.' + x[1] : '';
    var rgx = /(\d+)(\d{3})/;
    while (rgx.test(x1)) {
        x1 = x1.replace(rgx, '$1' + '.' + '$2');
    }
    return x1 + x2;
}

jQuery(document).ready(function($){
    $('input[id$=dizimos], input[id$=ofertas]').live('keyup', function() {
        var $tr = $(this).parents('tr');
        var dizimos = parseInt($tr.find('input[id$=dizimos]').val());
        var ofertas = parseInt($tr.find('input[id$=ofertas]').val());

        if(dizimos && ofertas) {
            $tr.find('input[id$=total]').html(currencyFormat(dizimos + ofertas));
        }
    });
});