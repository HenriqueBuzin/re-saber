$(document).ready(function () {

    var videoURL = 'https://www.youtube.com/embed/cbveIsGpUbI?si=gJXDZZcOYV1qF1bH&mute=1';

    var iframe = $('<iframe>', {
        width: '100%',
        height: '500',
        src: videoURL + '&autoplay=1',
        allowfullscreen: true,
        allow: 'autoplay'
    });

    if (navigator.userAgent.toLowerCase().indexOf('mobile') !== -1) {
        iframe.on('load', function () {
            iframe.play();
        });
    }

    $('#video-container').replaceWith(iframe);

});
