from app.models import mongo

class TechnologicalAxe:
    def __init__(self):
        self.mongo = mongo
        self.db = self.mongo.db
        self.collection = self.db.technological_axes
        self.create_unique_index()

    def create_unique_index(self):
        self.collection.create_index("name", unique=True)

    def technological_axes_count(self):
        technological_axes_count = self.collection.count_documents({})
        return technological_axes_count

    def get_all_technological_axes(self):
        technological_axes = list(self.collection.find({}))
        return technological_axes

    def insert_technological_axe(self, name):
        try:
            result = self.collection.insert_one({"name": name})
            return str(result.inserted_id)
        except:
            return None
