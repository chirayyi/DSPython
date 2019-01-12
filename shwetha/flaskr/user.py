import json

class User(object):
    def __init__(self):
        self.odd_recommendations = [{'title':'T1','id':'1'},{'title':'T3','id':'3'}]
        self.even_recommendations = [{'title':'T2','id':'2'}]
        
    def get_recommendations(self, userid):
        if userid % 2 == 0:
            return self.even_recommendations
        else:
            return self.odd_recommendations
