from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import CheckConstraint
from flask_login import UserMixin

db = SQLAlchemy()


class users(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column('user_id', db.Integer, primary_key=True, autoincrement=True)
    fname = db.Column(db.VARCHAR(30), nullable=False)
    lname = db.Column(db.VARCHAR(30), nullable=False)
    email = db.Column(db.VARCHAR(30), unique=True, nullable=False)
    password = db.Column(db.VARCHAR(256), nullable=False)
    address = db.Column(db.Text, nullable=False)
    gender = db.Column(db.Boolean, nullable=False)
    hobby = db.Column(db.VARCHAR(50), nullable=False)
    is_active = db.Column(db.Boolean, default=True)

    __table_args__ = (
        CheckConstraint('LENGTH(fname) <= 30', name='check_fname_length'),
        CheckConstraint('LENGTH(lname) <= 30', name='check_lname_length'),
        CheckConstraint('LENGTH(email) <= 30', name='check_email_length'),
    )

    def __init__(self, fname, lname, email, password, address, gender, hobby):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.password = password
        self.address = address
        self.gender = gender
        self.hobby = hobby

    def get_id(self):
        return self.id
