from app.models import mongo

class QualificationLevel:
    def __init__(self):
        self.mongo = mongo
        self.db = self.mongo.db
        self.collection = self.db.qualification_levels
        self.create_unique_index()

    def create_unique_index(self):
        self.collection.create_index("name", unique=True)

    def qualification_level_count(self):
        qualification_level_count = self.collection.count_documents({})
        return qualification_level_count

    def get_all_qualification_levels(self):
        qualification_levels = list(self.collection.find({}))
        return qualification_levels

    def insert_qualification_level(self, name):
        try:
            result = self.collection.insert_one({"name": name})
            return str(result.inserted_id)
        except:
            return None
