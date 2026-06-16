from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()


class Student(db.Model):

    id=db.Column(db.Integer,primary_key=True)

    name=db.Column(db.String(100))

    email=db.Column(db.String(100))

    education=db.Column(db.Text)

    skills=db.Column(db.Text)

    projects=db.Column(db.Text)

    experience=db.Column(db.Text)

    achievements=db.Column(db.Text)

    objective=db.Column(db.Text)