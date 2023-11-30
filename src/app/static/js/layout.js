$(document).ready(function() {

    $('.dropdown-menu').on('click', function(e) {
        e.stopPropagation();
    });

    if ($(window).width() < 992) {

        $('.navbar .dropdown').on('hidden.bs.dropdown', function() {
            $(this).find('.submenu').each(function() {
                $(this).css('display', 'none');
            });
        });

        $('.dropdown-menu a').on('click', function(e) {
            let nextEl = $(this).next('.submenu');
            if (nextEl.length) {
                e.preventDefault();
                console.log(nextEl);
                if (nextEl.css('display') == 'block') {
                    nextEl.css('display', 'none');
                } else {
                    nextEl.css('display', 'block');
                }
            }
        });
    }

});
