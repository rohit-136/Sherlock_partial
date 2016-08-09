import datetime
import uuid

from src.common.database import Database

#for this class only score and score_id are being sent from the user model
class Score(object):
    def __init__(self, score, score_id, _id=None, date=datetime.datetime.utcnow()):
        self.score = score
        self.date = date
        self.score_id = score_id
        self._id = uuid.uuid4().hex if _id is None else _id

   #we are saving a new score to the score list
    def save_to_mongo_score(self):
        Database.insert("score",self.json())


    def json(self):
        return {
            "score":self.score,
            "score_id":self.score_id,
            "date":self.date,
            "_id":self._id
        }

    #getting an object named number of the type number where number is the returned valued from the database
    @staticmethod
    def get_from_mongo_score(id):
        return [number for number in Database.find(collection="score",query={'score_id':id})]

