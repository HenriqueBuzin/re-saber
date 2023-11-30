$(document).ready(function() {

    function bindCollapseToImage(collapseId, imageId) {

        const collapseElement = $('#' + collapseId);
        const image = $('#' + imageId);
        
        if (collapseElement.length && image.length) {

            collapseElement.on('show.bs.collapse', function() {

                image.attr('src', image.attr('data-open'));

            });

            collapseElement.on('hide.bs.collapse', function() {

                image.attr('src', image.attr('data-closed'));

            });

        }

    }

    function toggleBootstrapCollapse(collapseId) {

        const collapseElement = $('#' + collapseId);

        const bsCollapse = new bootstrap.Collapse(collapseElement[0], {

            toggle: true

        });

    }

    window.toggleBootstrapCollapse = toggleBootstrapCollapse;

    $("[id^='collapse']").each(function() {

        const collapseId = this.id;
        const imageId = "image" + collapseId.replace('collapse', '');
        
        bindCollapseToImage(collapseId, imageId);

    });

});
