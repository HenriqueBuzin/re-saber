function initScrollReveal() {
    const sr = ScrollReveal({
        origin: 'bottom',
        distance: '50px',
        duration: 1000,
        delay: 0,
        reset: true,
        viewFactor: 0.3,
        beforeReveal: function(domEl) {
            $(domEl).css({opacity: '1', visibility: 'visible'});
        }
    });

    sr.reveal('.imagem-infografico, .imagem-overlay', { interval: 200 });
}

function openVideoModal(videoUrl) {
    var videoIframe = $('#videoIframe');
    videoIframe.attr('src', videoUrl);

    var videoModal = $('#videoModal');
    videoModal.addClass('show').css('display', 'block');

    $('body').addClass('modal-open');
}

function closeVideoModal() {
    var videoIframe = $('#videoIframe');
    videoIframe.removeAttr('src');

    var videoModal = $('#videoModal');
    videoModal.removeClass('show').css('display', 'none');

    $('body').removeClass('modal-open');
}

$(window).on('load', function() {
    initScrollReveal();

    $('.modal-trigger').on('click', function(event) {
        event.preventDefault();
        var videoUrl = $(this).data('video');
        openVideoModal(videoUrl);
    });

    $('.btn-close').on('click', closeVideoModal);
    $('.modal-backdrop').on('click', closeVideoModal);

    $('.btn.btn-secondary').on('click', closeVideoModal);
});
