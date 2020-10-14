from base.service import service
from base.model import model


class test(service):
    def config(self):
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