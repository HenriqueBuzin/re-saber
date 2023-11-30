from unidecode import unidecode
from app.models import mongo
from bson import ObjectId
import re

class OcupationTraining:
    def __init__(self):
        self.mongo = mongo
        self.db = self.mongo.db
        self.collection = self.db.occupation_training
        self.create_unique_index()

    def create_unique_index(self):
        self.collection.create_index("name", unique=True)

    def ocupation_training_count(self):
        ocupation_training_count = self.collection.count_documents({})
        return ocupation_training_count

    def get_all_ocupation_training(self):
        ocupation_training = list(self.collection.find({}))
        return ocupation_training

    def insert_ocupation_training(self, name):
        try:
            result = self.collection.insert_one({"name": name})
            return str(result.inserted_id)
        except:
            return None

    def search_ocupation_training(self, name):
        name_no_accents = unidecode(name).lower()

        all_ocupations = list(self.collection.find({}))

        regex = re.compile(f".*{name_no_accents}.*", re.IGNORECASE)

        filtered_ocupations = [ocupation for ocupation in all_ocupations if regex.match(unidecode(ocupation['name']).lower())]

        return filtered_ocupations[:5]

    def find_or_create(self, name):
        ocupation_training = self.collection.find_one({"name": name})
        if not ocupation_training:
            result = self.collection.insert_one({"name": name})
            return str(result.inserted_id)
        else:
            return str(ocupation_training["_id"])

    def get_by_id(self, institution_id):
        try:
            ocupation_training = self.collection.find_one({"_id": ObjectId(institution_id)})
            return ocupation_training
        except:
            return None
