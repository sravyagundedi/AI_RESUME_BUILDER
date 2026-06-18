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

@app.route("/generate", methods=["POST"])
def generate():

    try:

        data = {

            "name": request.form.get("name",""),

            "email": request.form.get("email",""),

            "education": request.form.get("education",""),

            "skills": request.form.get("skills",""),

            "experience": request.form.get("experience",""),

            "projects": request.form.get("projects",""),

            "achievements": request.form.get("achievements",""),

            "objective": request.form.get("objective","")

        }

        resume = generate_resume(data)

        return render_template(
            "result.html",
            resume=resume
        )

    except Exception as e:

        return str(e)



if __name__=="__main__":

    app.run(debug=True)