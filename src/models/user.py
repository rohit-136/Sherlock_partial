import uuid

from flask import session

from src.common.database import Database
from src.models.score import Score


class User(object):
    def __init__(self,email,password,score_id = None, _id=None):
        self.email = email
        self.password = password
        self.score_id = uuid.uuid4().hex if score_id is None else score_id
        self._id = uuid.uuid4().hex if _id is None else _id


    #checks wheather the user specified by the email exists or not
    @classmethod
    def get_by_email(cls, email):
        data = Database.find_one("users", {"email": email})
        if data is not None:
            return cls(**data)
        else:
            return None


    #checks if the user login is valid or not
    @staticmethod
    def login_valid(email,password):
        Email = User.get_by_email(email)
        if Email is not None:
            return password == Email.password
        else:
            return False


    #registers a user in case of new users
    @classmethod
    def register_user(cls,email,password):
        new_user = cls.get_by_email(email)
        if new_user is None:
            new_user = cls(email, password)
            new_user.save_to_mongo()
            session['email'] = email
            return True
        else:
            return False


    #only sets the session['email'] to the user email
    @staticmethod
    def login(user_email):
        session['email'] = user_email


    #logs out the user deletes the session email
    @staticmethod
    def logout():
        session['email'] = None


    #gets the scores of the user from the previous games finds by their score_id and not their _id
    def get_previous_scores(self):
        return Score.get_from_mongo_score(self.score_id)



    #this function is called once the user plays a new game. it stores the new score
    def new_game(self, score):
        game = Score(score,self.score_id)
        game.save_to_mongo_score()




    def json(self):
        return {
            "email":self.email,
            "password":self.password,
            "_id":self._id,
            "score_id":self.score_id
        }

    #saves a new user to the database
    def save_to_mongo(self):
        Database.insert("users" , self.json())
