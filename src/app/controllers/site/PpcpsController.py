from flask import render_template, Response, request, jsonify

from app.models.professional_education_system import ProfessionalEducationSystem
from app.models.qualification_level import QualificationLevel
from app.models.technological_axe import TechnologicalAxe
from app.models.federative_unit import FederativeUnit
from app.models.offering_institution import OfferingInstitution
from app.models.occupation_training import OcupationTraining
from app.models.ppcp import Ppcp

def ppcps_get():

   occupation_training_instance = OcupationTraining()
   occupation_training = occupation_training_instance.get_all_ocupation_training()

   offering_institution_instance = OfferingInstitution()
   offering_institution = offering_institution_instance.get_all_offering_institutions()

   professional_system_instance = ProfessionalEducationSystem()
   professional_systems = professional_system_instance.get_all_professional_education_systems()

   qualification_level_instance = QualificationLevel()
   qualification_levels = qualification_level_instance.get_all_qualification_levels()

   technological_axes_instance = TechnologicalAxe()
   technological_axes = technological_axes_instance.get_all_technological_axes()

   federative_units_instance = FederativeUnit()
   federative_units = federative_units_instance.get_all_federative_units()

   return render_template('site/ppcps.html', occupation_training=occupation_training,
                                             offering_institution=offering_institution, 
                                             professional_systems=professional_systems,
                                             qualification_levels=qualification_levels,
                                             technological_axes=technological_axes,
                                             federative_units=federative_units)

def ppcps_post():

   ppcp_instance = Ppcp()
   results = []

   if request.method == 'POST':
      general_search_term = request.form.get('general_search_term')

      input_data = {
         'offering_institution_id': request.form.get('offering_institution_id'),
         'occupation_training_id': request.form.get('occupation_training_id'),
         'technological_axe_id': request.form.get('technological_axe_id'),
         'professional_system_id': request.form.get('professional_system_id'),
         'qualification_level_id': request.form.get('qualification_level_id'),
         'federative_unit_id': request.form.get('federative_unit_id')
      }

      kwargs = {}
      for k, v in input_data.items():
         if v:
            kwargs[k] = v

      results = ppcp_instance.advanced_search(general_search_term, **kwargs)

      for item in results:
         item['_id'] = str(item['_id'])
    
         item.pop('pdf_binary', None)
         
         for key, value in item.items():
            if isinstance(value, bytes):
               item[key] = str(value)

      return jsonify(results)

def ppcp_get(ppcp_id):

   if not ppcp_id:
      return "Parâmetro 'ppcp_id' é obrigatório.", 400

   ppcp_instance = Ppcp()
   get_ppcp = ppcp_instance.get_ppcp_by_id(ppcp_id)
    
   if not get_ppcp:
      return "PPCP não encontrado para o ID fornecido.", 404
        
   return render_template('site/ppcp_get.html', ppcp_id=ppcp_id)

def ppcp_file_get(ppcp_id):

   ppcp_instance = Ppcp()
   get_ppcp = ppcp_instance.get_ppcp_by_id(ppcp_id)
    
   if not get_ppcp or 'pdf_binary' not in get_ppcp:
      return "PDF não encontrado para o ID fornecido.", 404
    
   response = Response(get_ppcp['pdf_binary'], content_type='application/pdf')
   return response
