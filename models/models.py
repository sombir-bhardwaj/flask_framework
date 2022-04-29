from run import db

class user(db.Model):
    __tablename__ = "user"
    id = db.column('id', db.Interger,primary_key=True)
    name = db.column('name',db.String(20), unique=True, index=True)
    age = db.column('age', db.String(50),unique=True, index=True)
    gender = db.column(db.Integer, server_default="1", nullable=False)

    def __init__(self,name):
        self.name=name
# heloo my name is vivek