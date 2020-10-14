class result:
    code = 0
    data = []
    message = ''

    def sucess(self, data):
        self.code = 1
        self.data = data
        self.message = 'success'

    def fail(self, msg):
        self.code = 0
        self.data = []
        self.message = msg

    def getResult(self,ser):

        if ser.run():
            self.sucess(ser.re)
        else:
            self.fail(ser.re)




