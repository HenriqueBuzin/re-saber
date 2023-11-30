$(document).ready(function() {
    $('.image-container').click(function() {
        var videoId = $(this).data('video-id');
        var videoUrl = 'https://www.youtube.com/embed/' + videoId;

        $('#videoIframe').attr('src', videoUrl);

    });

    $('#videoModal').on('hide.bs.modal', function() {
        $('#videoIframe').attr('src', '');
    });
});
