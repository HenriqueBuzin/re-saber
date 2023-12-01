from flask import request, redirect, url_for, render_template, jsonify
from bson.binary import Binary

from app.models.professional_education_system import ProfessionalEducationSystem
from app.models.qualification_level import QualificationLevel
from app.models.technological_axe import TechnologicalAxe
from app.models.federative_unit import FederativeUnit
from app.models.offering_institution import OfferingInstitution
from app.models.occupation_training import OcupationTraining
from app.models.ppcp import Ppcp

def get():

    warning = request.args.get('warning')

    warning_class = request.args.get('warning_class')

    professional_system_instance = ProfessionalEducationSystem()
    professional_systems = professional_system_instance.get_all_professional_education_systems()

    qualification_level_instance = QualificationLevel()
    qualification_levels = qualification_level_instance.get_all_qualification_levels()

    technological_axes_instance = TechnologicalAxe()
    technological_axes = technological_axes_instance.get_all_technological_axes()

    federative_units_instance = FederativeUnit()
    federative_units = federative_units_instance.get_all_federative_units()

    return render_template('admin/register.html', professional_systems=professional_systems,
                                                  qualification_levels=qualification_levels,
                                                  technological_axes=technological_axes,
                                                  federative_units=federative_units,
                                                  warning=warning,
                                                  warning_class=warning_class)

def post():

    offering_institution_name = request.form.get('offering_institution')
    training_occupation_name = request.form.get('training_occupation')
    professional_system_id = request.form.get('professional_system_id')
    qualification_level_id = request.form.get('qualification_level_id')
    technological_axe_id = request.form.get('technological_axe_id')
    federative_unit_id = request.form.get('federative_unit_id')
    pdf_file = request.files.get('pdf_file')

    offering_institution_instance = OfferingInstitution()
    offering_institution_id = offering_institution_instance.find_or_create(offering_institution_name)

    occupation_training_instance = OcupationTraining()
    occupation_training_id = occupation_training_instance.find_or_create(training_occupation_name)

    if pdf_file:
        pdf_binary = Binary(pdf_file.read())

        ppcp_instance = Ppcp()
        ppcp_insert = ppcp_instance.insert_ppcp(offering_institution_id,
                                                occupation_training_id,
                                                professional_system_id,
                                                qualification_level_id,
                                                technological_axe_id,
                                                federative_unit_id,
                                                pdf_file.filename,
                                                pdf_binary)

        return redirect(url_for('admin.register_get', warning='Arquivo cadastrado com sucesso!', warning_class='alert-success'))

def edit_get(ppcp_id):

    warning = request.args.get('warning')

    warning_class = request.args.get('warning_class')

    ppcp_instance = Ppcp()
    ppcp = ppcp_instance.get_ppcp_by_id(ppcp_id)

    offering_institution_instance = OfferingInstitution()
    offering_institution = offering_institution_instance.get_by_id(ppcp['offering_institution_id'])
    offering_institution = offering_institution['name']

    training_occupation_instance = OcupationTraining()
    training_occupation = training_occupation_instance.get_by_id(ppcp['occupation_training_id'])
    training_occupation = training_occupation['name']

    professional_system_instance = ProfessionalEducationSystem()
    professional_systems = professional_system_instance.get_all_professional_education_systems()

    qualification_level_instance = QualificationLevel()
    qualification_levels = qualification_level_instance.get_all_qualification_levels()

    technological_axes_instance = TechnologicalAxe()
    technological_axes = technological_axes_instance.get_all_technological_axes()

    federative_units_instance = FederativeUnit()
    federative_units = federative_units_instance.get_all_federative_units()

    if ppcp:
        return render_template('admin/register.html', ppcp=ppcp,
                                                      offering_institution=offering_institution,
                                                      training_occupation=training_occupation,
                                                      professional_systems=professional_systems,
                                                      qualification_levels=qualification_levels,
                                                      technological_axes=technological_axes,
                                                      federative_units=federative_units,
                                                      warning=warning,
                                                      warning_class=warning_class)

def edit_post(ppcp_id):

    offering_institution_name = request.form.get('offering_institution')
    training_occupation_name = request.form.get('training_occupation')
    professional_system_id = request.form.get('professional_system_id')
    qualification_level_id = request.form.get('qualification_level_id')
    technological_axe_id = request.form.get('technological_axe_id')
    federative_unit_id = request.form.get('federative_unit_id')
    pdf_file = request.files.get('pdf_file')

    offering_institution_instance = OfferingInstitution()
    offering_institution_id = offering_institution_instance.find_or_create(offering_institution_name)

    training_occupation_instance = OcupationTraining()
    training_occupation_id = training_occupation_instance.find_or_create(training_occupation_name)

    new_data = {
        "offering_institution_id": offering_institution_id,
        "occupation_training_id": training_occupation_id,
        "professional_system_id": professional_system_id,
        "qualification_level_id": qualification_level_id,
        "technological_axe_id": technological_axe_id,
        "federative_unit_id": federative_unit_id,
    }

    if pdf_file:
        new_data["pdf_filename"] = pdf_file.filename
        new_data["pdf_binary"] = Binary(pdf_file.read())

    ppcp_instance = Ppcp()

    if ppcp_instance.update_ppcp(ppcp_id, new_data):
        return redirect(url_for('admin.admin_page', ppcp_id=ppcp_id, warning='PPCP atualizado com sucesso!', warning_class='alert-success'))
    else:
        return redirect(url_for('admin.edit_ppcp_get', ppcp_id=ppcp_id, warning='Nenhuma alteração foi feita no PPCP.', warning_class='alert-danger'))

def autocomplete_offering_institution_post():
    name = request.json.get('offering_institution')
    offering_institution_instance = OfferingInstitution()
    institutions = offering_institution_instance.search_offering_institutions(name)
    return jsonify([inst['name'] for inst in institutions])

def autocomplete_occupation_training_post():
    name = request.json.get('occupation_training')
    occupation_training_instance = OcupationTraining()
    occupations = occupation_training_instance.search_ocupation_training(name)
    return jsonify([inst['name'] for inst in occupations])
