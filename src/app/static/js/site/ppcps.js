$(document).ready(function () {

  $(".select2").select2({
    width: '100%'
  });

  const searchForm = $("#searchForm");

  if (!searchForm.length) {
    console.error('Formulário com o ID "searchForm" não encontrado.');
    return;
  }

  searchForm.on("submit", function (event) {
    event.preventDefault();

    const formData = new FormData(this);

    const xhr = new XMLHttpRequest();

    xhr.open("POST", "/ppcps", true);

    xhr.onload = function () {
      const resultsDiv = $("#results");

      if (!resultsDiv.length) {
        console.error('Elemento com o ID "results" não encontrado.');
        return;
      }

      resultsDiv.html("");

      if (xhr.status === 200) {
        const results = JSON.parse(xhr.responseText);

        if (results.length) {
          results.forEach(function (result) {
            const div = $("<div>");
            div.addClass("col-md-6 col-sm-12 existing_ppcps");

            div.html(`
              <p>Instituição Ofertante: ${result.offering_institution_name}</p>
              <p>Formação/ocupação: ${result.occupation_training_name}</p>
              <p>Sistema Profissional: ${result.professional_system_name}</p>
              <p>Eixo Tecnológico: ${result.qualification_level_name}</p>
              <p>Nível de Qualificação: ${result.technological_axe_name}</p>
              <p>Unidade Federativa: ${result.federative_unit_name}</p>
              <p>Nome do PDF: ${result.pdf_filename}</p>
              <a href="/ppcp_pdf/${result._id}">Ver PDF</a>
            `);

            // Adiciona a classe "fade-in" ao elemento assim que ele é adicionado ao DOM
            resultsDiv.append(div).fadeIn("2000");
          });
        } else {
          const div = $("<div>");
          div.addClass("col-md-6 col-sm-12 existing_ppcps");
          const p = $("<p>");
          p.text("Nenhum resultado encontrado.");
          div.append(p);
          resultsDiv.append(div).fadeIn("2000");
        }
      } else {
        console.error("Erro ao buscar dados:", xhr.responseText);
      }
    };

    xhr.send(formData);
  });
});
