from app.models import mongo

class ProfessionalEducationSystem:
    def __init__(self):
        self.mongo = mongo
        self.db = self.mongo.db
        self.collection = self.db.professional_education_systems
        self.create_unique_index()

    def create_unique_index(self):
        self.collection.create_index("name", unique=True)

    def professional_education_system_count(self):
        professional_education_system_count = self.collection.count_documents({})
        return professional_education_system_count

    def get_all_professional_education_systems(self):
        professional_education_systems = list(self.collection.find({}))
        return professional_education_systems

    def insert_professional_education_system(self, name):
        try:
            result = self.collection.insert_one({"name": name})
            return str(result.inserted_id)
        except:
            return None
