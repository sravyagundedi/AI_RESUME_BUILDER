import os

class Config:

    SECRET_KEY="resume123"

    SQLALCHEMY_DATABASE_URI="sqlite:///resume.db"

    SQLALCHEMY_TRACK_MODIFICATIONS=False

    GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")