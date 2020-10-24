from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    fullname = db.Column(db.String(255))
    emailAddress = db.Column(db.String(255),unique = True,index = True)
    biography = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password = db.Column(db.String(255))

    @property
    def password(self):

        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password,password)

    @login_manager.user_loader
    def load_user(user_id):
    return User.query.get(int(user_id))

    def __repr__(self):
        return f'User {self.username}'