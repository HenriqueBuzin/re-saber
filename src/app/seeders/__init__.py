from app.models.qualification_level import QualificationLevel
from app.models.technological_axe import TechnologicalAxe
from app.models.professional_education_system import ProfessionalEducationSystem
from app.models.federative_unit import FederativeUnit
from app.models.offering_institution import OfferingInstitution
from app.models.occupation_training import OcupationTraining

from app.seeders.qualification_levels import data as DataQualificationLevels
from app.seeders.technological_axes import data as DataTechnologicalAxes
from app.seeders.professional_education_systems import data as DataProfessionalEducationSystems
from app.seeders.federative_units import data as DataFederativeUnits
from app.seeders.offering_institution import data as DataOfferingInstitution
from app.seeders.occupation_training import data as DataOccupationTraining

class Seeder:
    def __init__(self):
        self.qualification_level_instance = QualificationLevel()
        self.technological_axe_instance = TechnologicalAxe()
        self.professional_education_system_instance = ProfessionalEducationSystem()
        self.federative_unit_instance = FederativeUnit()
        self.offering_institution_instance = OfferingInstitution()
        self.occupation_training_instance = OcupationTraining()

    def check_and_seed_qualification_levels(self):
        if self.qualification_level_instance.qualification_level_count() == 0:
            for name in DataQualificationLevels:
                self.qualification_level_instance.insert_qualification_level(
                    name)

    def check_and_seed_technological_axes(self):
        if self.technological_axe_instance.technological_axes_count() == 0:
            for name in DataTechnologicalAxes:
                self.technological_axe_instance.insert_technological_axe(name)

    def check_and_seed_professional_education_systems(self):
        if self.professional_education_system_instance.professional_education_system_count() == 0:
            for name in DataProfessionalEducationSystems:
                self.professional_education_system_instance.insert_professional_education_system(
                    name)

    def check_and_seed_federative_units(self):
        if self.federative_unit_instance.federative_unit_count() == 0:
            for name in DataFederativeUnits:
                self.federative_unit_instance.insert_federative_unit(
                    name)

    def check_and_seed_offering_institutions(self):
        if self.offering_institution_instance.offering_institution_count() == 0:
            for name in DataOfferingInstitution:
                self.offering_institution_instance.insert_offering_institution(
                    name)
    
    def check_and_seed_occupation_training(self):
        if self.occupation_training_instance.ocupation_training_count() == 0:
            for name in DataOccupationTraining:
                self.occupation_training_instance.insert_ocupation_training(
                    name)

    def seed_all_data(self):
        self.check_and_seed_qualification_levels()
        self.check_and_seed_technological_axes()
        self.check_and_seed_professional_education_systems()
        self.check_and_seed_federative_units()
        self.check_and_seed_offering_institutions()
        self.check_and_seed_occupation_training()
