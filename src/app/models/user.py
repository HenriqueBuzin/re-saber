from app.models import mongo
import bcrypt

class User:
    def __init__(self):
        self.mongo = mongo
        self.db = self.mongo.db
        self.collection = self.db.users
    
    @staticmethod
    def hash_password(password):
        """Gera um hash de uma senha usando bcrypt."""
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed.decode('utf-8')  # para armazenar como string no MongoDB

    @staticmethod
    def check_password(hashed, password):
        """Verifica uma senha contra o hash armazenado."""
        return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

    def users_count(self):
        user_count = self.collection.count_documents({})
        return user_count

    def insert_user(self, email, password):
        hashed_password = self.hash_password(password)
        result = self.collection.insert_one({"email": email, "password": hashed_password})
        
        if result.inserted_id:
            return str(result.inserted_id)
        else:
            return None
            
    def find_user_by_credentials(self, email, password):
        user = self.collection.find_one({"email": email})
        if user and self.check_password(user['password'], password):
            user['_id'] = str(user['_id'])
            return user
        return None

    def find_user_by_email(self, email):
        user = self.collection.find_one({"email": email})
        if user:
            user['_id'] = str(user['_id'])
        return user

    def get_password_by_email(self, email):
        user = self.collection.find_one({"email": email})
        if user:
            user['_id'] = str(user['_id'])
            return user['password']
        else:
            return None

    def update_password_by_email(self, email, new_password):
        hashed_password = self.hash_password(new_password)
        result = self.collection.update_one({"email": email}, {"$set": {"password": hashed_password}})
        return result.modified_count > 0
