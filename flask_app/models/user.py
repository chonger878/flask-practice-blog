from flask_app.config import mysqlconnection

class  User:
    def __init__(self,data):
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.pwd = data['pwd']