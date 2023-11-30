$(document).ready(function() {

    $(".select2").select2({
        width: '100%'
    });

    // Elementos e dropdowns para offering_institution
    const offeringInstitution = $("#offering_institution");
    const autocompleteDropdownInstitution = $("<div>").addClass("autocomplete-dropdown");
    offeringInstitution.parent().append(autocompleteDropdownInstitution);

    // Elementos e dropdowns para training_occupation
    const trainingOccupation = $("#training_occupation");
    const autocompleteDropdownOccupation = $("<div>").addClass("autocomplete-dropdown");
    trainingOccupation.parent().append(autocompleteDropdownOccupation);

    // Listener para offering_institution
    offeringInstitution.on("input", function() {
        const query = offeringInstitution.val();

        if (query.length >= 3) {
            $.ajax({
                url: "/admin/autocomplete/offering_institution",
                method: "POST",
                contentType: "application/json",
                data: JSON.stringify({ offering_institution: query }),
                success: function(data) {
                    autocompleteDropdownInstitution.empty();

                    $.each(data, function(index, institution) {
                        const item = $("<div>").text(institution);
                        item.click(function() {
                            offeringInstitution.val(institution);
                            autocompleteDropdownInstitution.empty();
                        });
                        autocompleteDropdownInstitution.append(item);
                    });
                }
            });
        } else {
            autocompleteDropdownInstitution.empty();
        }
    });

    // Listener para training_occupation
    trainingOccupation.on("input", function() {
        const query = trainingOccupation.val();

        if (query.length >= 3) {
            $.ajax({
                url: "/admin/autocomplete/occupation_training",
                method: "POST",
                contentType: "application/json",
                data: JSON.stringify({ occupation_training: query }),
                success: function(data) {
                    autocompleteDropdownOccupation.empty();

                    $.each(data, function(index, occupation) {
                        const item = $("<div>").text(occupation);
                        item.click(function() {
                            trainingOccupation.val(occupation);
                            autocompleteDropdownOccupation.empty();
                        });
                        autocompleteDropdownOccupation.append(item);
                    });
                }
            });
        } else {
            autocompleteDropdownOccupation.empty();
        }
    });

    // Listener para fechar os dropdowns quando clicar fora
    $(document).on("click", function(event) {
        if (event.target !== offeringInstitution[0]) {
            autocompleteDropdownInstitution.empty();
        }
        if (event.target !== trainingOccupation[0]) {
            autocompleteDropdownOccupation.empty();
        }
    });

    document.getElementById('pdf_upload').addEventListener('change', function() {
        var fileInput = this;
        var fileName = fileInput.files[0] ? fileInput.files[0].name : 'Escolher arquivo...';
        document.getElementById('file_chosen').textContent = fileName;
    });
    
});

