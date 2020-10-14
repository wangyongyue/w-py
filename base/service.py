from flask import json,current_app
from flask_sqlalchemy import SQLAlchemy
from base.model import model


class service:
    re = ''
    def config(self):
        self.re = ""
        return True
    def sql(self):
        return 'select * from word_w'
    def handleData(self,results):
        a = []
        for row in results:
            m = model()
            m.id = row['id']
            m.data = row['data']
            a.append(m)
        self.re = a
        return True

    def run(self):
        if self.config() == False:
            return False
        db = SQLAlchemy(current_app)
        results = db.session.execute(self.sql())
        return self.handleData(results)





