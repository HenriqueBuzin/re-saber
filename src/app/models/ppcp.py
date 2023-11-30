from bson.errors import InvalidId
from app.models import mongo
from bson import ObjectId
from unidecode import unidecode

class Ppcp:
    def __init__(self):
        self.mongo = mongo
        self.db = self.mongo.db
        self.collection = self.db.ppcps

    def insert_ppcp(self, offering_institution_id, 
                           training_occupation, 
                           professional_system_id,
                           qualification_level_id,
                           technological_axe_id,
                           federative_unit_id,
                           pdf_filename,
                           pdf_binary):
        
        result = self.collection.insert_one({"offering_institution_id": offering_institution_id, 
                                             "occupation_training_id": training_occupation,
                                             "professional_system_id": professional_system_id,
                                             "qualification_level_id": qualification_level_id,
                                             "technological_axe_id": technological_axe_id,
                                             "federative_unit_id": federative_unit_id,
                                             "pdf_filename": pdf_filename,
                                             "pdf_binary": pdf_binary})

        if result.inserted_id:
            return str(result.inserted_id)
        else:
            return None

    def get_all_ppcps(self):
        all_ppcps = self.collection.find()
        return list(all_ppcps)

    def get_all_ppcps_with_names(self):
        all_ppcps = self.collection.find()

        ppcps_with_names = []

        for ppcp in all_ppcps:
            ppcp_with_names = self._translate_foreign_keys(ppcp)
            ppcps_with_names.append(ppcp_with_names)

        return ppcps_with_names

    def _translate_foreign_keys(self, ppcp):
        offering_institution = self._get_name_by_id('offering_institutions', ppcp.get('offering_institution_id'))
        occupation_training = self._get_name_by_id('occupation_training', ppcp.get('occupation_training_id'))
        professional_system = self._get_name_by_id('professional_education_systems', ppcp.get('professional_system_id'))
        qualification_level = self._get_name_by_id('qualification_levels', ppcp.get('qualification_level_id'))
        technological_axe = self._get_name_by_id('technological_axes', ppcp.get('technological_axe_id'))
        federative_unit = self._get_name_by_id('federative_units', ppcp.get('federative_unit_id'))

        ppcp_with_names = ppcp.copy()
        ppcp_with_names['occupation_training_id'] = occupation_training
        ppcp_with_names['offering_institution_id'] = offering_institution
        ppcp_with_names['professional_system_id'] = professional_system
        ppcp_with_names['qualification_level_id'] = qualification_level
        ppcp_with_names['technological_axe_id'] = technological_axe
        ppcp_with_names['federative_unit_id'] = federative_unit

        return ppcp_with_names

    def _get_name_by_id(self, collection_name, item_id):
        collection = self.db[collection_name]
        item = collection.find_one({"_id": ObjectId(item_id)})
        if item:
            return item.get('name', '')
        return ''

    def delete_ppcp_by_id(self, ppcp_id):
        result = self.collection.delete_one({"_id": ObjectId(ppcp_id)})
        return result.deleted_count > 0
    
    def get_ppcp_by_id(self, ppcp_id):
        try:
            ppcp = self.collection.find_one({"_id": ObjectId(ppcp_id)})
            return ppcp
        except InvalidId:
            return None
    
    def update_ppcp(self, ppcp_id, new_data):
        result = self.collection.update_one(
            {"_id": ObjectId(ppcp_id)},
            {"$set": new_data}
        )

        return result.modified_count > 0
    
    def advanced_search(self, general_search_term=None, **kwargs):

        def remove_accents(input_str):
            return unidecode(input_str)

        filter_query = {}
        valid_keys = [
            "occupation_training_id",
            "offering_institution_id",
            "technological_axe_id",
            "professional_system_id",
            "qualification_level_id",
            "federative_unit_id"
        ]

        for key in valid_keys:
            if key in kwargs and kwargs[key]:
                filter_query[key] = kwargs[key]

        documents = self.collection.find(filter_query)
        results = []

        occupation_training = {str(x["_id"]): x["name"] for x in self.db['occupation_training'].find()}
        offering_institutions = {str(x["_id"]): x["name"] for x in self.db['offering_institutions'].find()}
        professional_systems = {str(x["_id"]): x["name"] for x in self.db['professional_education_systems'].find()}
        qualification_levels = {str(x["_id"]): x["name"] for x in self.db['qualification_levels'].find()}
        technological_axes = {str(x["_id"]): x["name"] for x in self.db['technological_axes'].find()}
        federative_units = {str(x["_id"]): x["name"] for x in self.db['federative_units'].find()}

        for doc in documents:
            doc['occupation_training_name'] = occupation_training.get(doc['occupation_training_id'])
            doc['offering_institution_name'] = offering_institutions.get(doc['offering_institution_id'])
            doc['professional_system_name'] = professional_systems.get(doc['professional_system_id'])
            doc['qualification_level_name'] = qualification_levels.get(doc['qualification_level_id'])
            doc['technological_axe_name'] = technological_axes.get(doc['technological_axe_id'])
            doc['federative_unit_name'] = federative_units.get(doc['federative_unit_id'])

            if general_search_term:
                general_search_term = remove_accents(general_search_term.lower())
                fields_to_check = [
                    remove_accents(doc['pdf_filename']),
                    remove_accents(doc['occupation_training_name']),
                    remove_accents(doc['offering_institution_name']),
                    remove_accents(doc['professional_system_name']),
                    remove_accents(doc['qualification_level_name']),
                    remove_accents(doc['technological_axe_name']),
                    remove_accents(doc['federative_unit_name'])
                ]
                if any(general_search_term in (field or "").lower() for field in fields_to_check):
                    results.append(doc)
            else:
                results.append(doc)

        return results
