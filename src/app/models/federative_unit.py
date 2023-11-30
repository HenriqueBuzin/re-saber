from app.models import mongo

class FederativeUnit:
    def __init__(self):
        self.mongo = mongo
        self.db = self.mongo.db
        self.collection = self.db.federative_units
        self.create_unique_index()

    def create_unique_index(self):
        self.collection.create_index("name", unique=True)

    def federative_unit_count(self):
        federative_units_count = self.collection.count_documents({})
        return federative_units_count

    def get_all_federative_units(self):
        federative_units = list(self.collection.find({}))
        return federative_units

    def insert_federative_unit(self, name):
        try:
            result = self.collection.insert_one({"name": name})
            return str(result.inserted_id)
        except:
            # Handle the unique constraint violation or other exceptions
            return None
