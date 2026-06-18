import google.generativeai as genai

from config import Config

if not Config.GEMINI_API_KEY:
    raise Exception("GEMINI_API_KEY not found")

genai.configure(

api_key=Config.GEMINI_API_KEY

)


model = genai.GenerativeModel("gemini-2.0-flash")



def ask_ai(prompt):

    response=model.generate_content(

    prompt

    )

    return response.text




def generate_resume(data):
    prompt=f"""

Generate an ATS friendly Resume.

Name:
{data['name']}

Email:
{data['email']}

Education:
{data['education']}

Skills:
{data['skills']}

Experience:
{data['experience']}

Format the resume professionally with headings,
bullet points and ATS-friendly structure.

"""

    return ask_ai(prompt)




def generate_cover_letter(data):

    prompt=f"""

Write professional cover letter.

Name:

{data['name']}

Skills:

{data['skills']}

Projects:

{data['projects']}

"""

    return ask_ai(prompt)




def generate_portfolio_intro(data):

    prompt=f"""

Write attractive portfolio introduction.

Name:

{data['name']}

Skills:

{data['skills']}

Projects:

{data['projects']}

"""

    return ask_ai(prompt)