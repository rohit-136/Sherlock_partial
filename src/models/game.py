import uuid

from src.common.database import Database


class Game(object):
    def __init__(self,user,score,_id=None):
        self.user = user
        self.score = score
        self._id = uuid.uuid4().hex if _id is None else _id




    def json(self):
        return {
            "user":self.user,
            "_id":self._id,
            "score":self.score
        }


    #save a complete data about the user score in the database. does not store the email and password here thst's done in user
    def save_to_mongo(self):
        Database.insert("user",self.json())



    #called in from user file to get the previous scores
    @classmethod
    def get_by_user_id(cls,id):
        game = Database.find(collection='scores',query={"_id":id})
        return cls(score=game['score'])


