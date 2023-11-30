from flask import render_template, request
from urllib.parse import urlparse

def get():
    recurso = request.args.get('recurso')
    item = request.args.get('item')

    host = urlparse(request.base_url)
    hostname = host.hostname

    try:
        recurso = int(recurso)
        item = int(item)
    except (ValueError, TypeError):
        return "Recurso e item devem ser números inteiros."

    result_map = {
        1: {
            0: [
                "Neste livro, você descobrirá do que trata a Coleção Oficinas do Re-Saber, para quem e com que propósito ela foi produzida.",
                hostname + "../../../../pdfs/livro0.pdf"
               ],
            1: [
                "Adaptação do livro multimídia produzido para a Unidade Curricular 1 das Oficinas do Re-Saber (IFSC & Setec/MEC), “Epistemologia e Estrutura da Educação Profissional”, que aborda conceitos básicos, como: técnica, tecnologia, trabalho e educação profissional; o fazer como fonte de saber; além da educação profissional no Brasil, suas normas e estrutura básica.",
                hostname + "../../../../pdfs/livro1.pdf"
               ],
            2: [
                "Adaptação do livro multimídia produzido para a Unidade Curricular 2 das Oficinas do Re-Saber (IFSC & Setec/MEC), “Certificação de Competências no Re-Saber”, que aborda a portaria do Re-Saber; quem e como avaliar para certificar; o sistema brasileiro de certificação de saberes e competências; além do Re-Saber no SISTEC.",
                hostname + "../../../../pdfs/livro2.pdf"
               ],
            3: [ 
                "Adaptação do livro multimídia produzido para a Unidade Curricular 3 das Oficinas do Re-Saber (IFSC & Setec/MEC), “Projeto Pedagógico de Certificação Profissional”, que aborda a Estrutura do PPCP; a busca ativa; a escolha do curso de referência; a análise da atividade; um modelo básico do PPCP; além do perfil da equipe de implementação.",
                hostname + "../../../../pdfs/livro3.pdf"
               ],
            4: [
                "",
                hostname + "../../../../pdfs/livro4.pdf"
               ],
            5: [
                "Adaptação do livro multimídia produzido para a Unidade Curricular 5 das Oficinas do Re-Saber (IFSC & Setec/MEC), “Adesão e Credenciamento Institucional ao Sistema Re-Saber”, que aborda os procedimentos realizados junto aos órgãos deliberativos; a documentação necessária, o plano de trabalho e o roteiro para adesão ao Sistema Re-Saber; além da formação de comunidade de práticas em certificação.",
                hostname + "../../../../pdfs/livro5.pdf"
               ],
            6: [ 
                "Adaptação do livro multimídia produzido para a Unidade Curricular 6 das Oficinas do Re-Saber (IFSC & Setec/MEC), “Documento Orientador para Oferta do Re-Saber”, que aborda o levantamento do perfil de certificação da instituição; a organização do grupo de trabalho; exemplos de documento base; além da construção do Documento Orientador.",
                hostname + "../../../../pdfs/livro6.pdf"
               ]
        },
        2: {
            0: [
                "Neste breve áudio, você descobrirá do que trata a Coleção Oficinas do Re-Saber, para quem e com que propósito ela foi produzida. Depois, confira os cinco audiobooks em nosso canal. Boa escuta!",
                "https://podcasters.spotify.com/pod/show/oficinas-re-saber/embed/episodes/Oficinas-do-Re-Saber---Apresentao-e1usaap/a-a9audq1"
               ],
            1: [
                "Audiobook (adaptação do livro multimídia) produzido para a Unidade Curricular 1 das Oficinas do Re-Saber (IFSC & Setec/MEC), “Epistemologia e Estrutura da Educação Profissional”, que aborda conceitos básicos, como: técnica, tecnologia, trabalho e educação profissional; o fazer como fonte de saber; além da educação profissional no Brasil, suas normas e estrutura básica.",
                "https://podcasters.spotify.com/pod/show/oficinas-re-saber/embed/episodes/UC1---Epistemologia-da-EP-e1ujhmu/a-a9a1h1c"
               ],
            2: [
                "Audiobook (adaptação do livro multimídia) produzido para a Unidade Curricular 2 das Oficinas do Re-Saber (IFSC & Setec/MEC), “Certificação de Competências no Re-Saber”, que aborda a portaria do Re-Saber; quem e como avaliar para certificar; o sistema brasileiro de certificação de saberes e competências; além do Re-Saber no SISTEC.",
                "https://podcasters.spotify.com/pod/show/oficinas-re-saber/embed/episodes/UC2---Certificao-no-Re-Saber-e20sgt5/a-a9hjvnv"
               ],
            3: [
                "Audiobook (adaptação do livro multimídia) produzido para a Unidade Curricular 3 das Oficinas do Re-Saber (IFSC & Setec/MEC), “Projeto Pedagógico de Certificação Profissional”, que aborda a Estrutura do PPCP; a busca ativa; a escolha do curso de referência; a análise da atividade; um modelo básico do PPCP; além do perfil da equipe de implementação.",
                "https://podcasters.spotify.com/pod/show/oficinas-re-saber/embed/episodes/UC3---PPCP-e1uk7ca/a-a9a3gih"
               ],
            5: [
                "Audiobook (adaptação do livro multimídia) produzido para a Unidade Curricular 5 das Oficinas do Re-Saber (IFSC & Setec/MEC), “Adesão e Credenciamento Institucional ao Sistema Re-Saber”, que aborda os procedimentos realizados junto aos órgãos deliberativos; a documentação necessária, o plano de trabalho e o roteiro para adesão ao Sistema Re-Saber; além da formação de comunidade de práticas em certificação.",
                "https://podcasters.spotify.com/pod/show/oficinas-re-saber/embed/episodes/UC5---Adeso-ao-Re-Saber-e1ukaqq/a-a9a3qpe"
               ],
            6: [
                "Audiobook (adaptação do livro multimídia) produzido para a Unidade Curricular 6 das Oficinas do Re-Saber (IFSC & Setec/MEC), “Documento Orientador para Oferta do Re-Saber”, que aborda o levantamento do perfil de certificação da instituição; a organização do grupo de trabalho; exemplos de documento base; além da construção do Documento Orientador.",
                "https://podcasters.spotify.com/pod/show/oficinas-re-saber/embed/episodes/UC6---Oferta-do-Re-Saber-e1ukf0d/a-a9a49qj"
               ]
        }
    }

    if recurso in result_map and item in result_map[recurso]:
        result = result_map[recurso][item]
    else:
        result = None

    return render_template('site/multimedia.html', recurso=recurso, result=result)
