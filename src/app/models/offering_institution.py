from unidecode import unidecode
from app.models import mongo
from bson import ObjectId
import re

class OfferingInstitution:
    def __init__(self):
        self.mongo = mongo
        self.db = self.mongo.db
        self.collection = self.db.offering_institutions
        self.create_unique_index()

    def create_unique_index(self):
        self.collection.create_index("name", unique=True)

    def offering_institution_count(self):
        offering_institutions_count = self.collection.count_documents({})
        return offering_institutions_count

    def get_all_offering_institutions(self):
        offering_institutions = list(self.collection.find({}))
        return offering_institutions

    def insert_offering_institution(self, name):
        try:
            result = self.collection.insert_one({"name": name})
            return str(result.inserted_id)
        except:
            return None

    def search_offering_institutions(self, name):
        name_no_accents = unidecode(name).lower()

        all_institutions = list(self.collection.find({}))

        regex = re.compile(f".*{name_no_accents}.*", re.IGNORECASE)

        filtered_matches = [inst for inst in all_institutions if regex.match(unidecode(inst['name']).lower())]

        return filtered_matches[:5]

    def find_or_create(self, name):
        existing_institution = self.collection.find_one({"name": name})
        if not existing_institution:
            result = self.collection.insert_one({"name": name})
            return str(result.inserted_id)
        else:
            return str(existing_institution["_id"])

    def get_by_id(self, institution_id):
        try:
            institution = self.collection.find_one({"_id": ObjectId(institution_id)})
            return institution
        except:
            return None
