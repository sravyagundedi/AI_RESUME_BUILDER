from flask import Flask,render_template,request
from dotenv import load_dotenv

load_dotenv()
from flask import send_file
from config import Config

from models import db,Student

from ai_generator import *

from pdf_generator import create_pdf


app=Flask(__name__)

app.config.from_object(Config)

db.init_app(app)


with app.app_context():

    db.create_all()



@app.route("/")

def home():

    return render_template("index.html")

@app.route("/download")

def download():

    return send_file(

    "resume.pdf",

    as_attachment=True

    )

@app.route("/generate",methods=["POST"])

def generate():

    data={

    "name":request.form["name"],

    "email":request.form["email"],

    "education":request.form["education"],

    "skills":request.form["skills"],

    "projects":request.form["projects"],

    "experience":request.form["experience"],

    "achievements":request.form["achievements"],

    "objective":request.form["objective"]

    }


    student=Student(**data)

    db.session.add(student)

    db.session.commit()


    resume=generate_resume(data)

    cover=generate_cover_letter(data)

    portfolio=generate_portfolio_intro(data)


    create_pdf(resume)


    return render_template(

    "result.html",

    resume=resume,

    cover=cover,

    portfolio=portfolio

    )



if __name__=="__main__":

    app.run(debug=True)