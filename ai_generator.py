import google.generativeai as genai

from config import Config


genai.configure(

api_key=Config.GEMINI_API_KEY

)


model=genai.GenerativeModel(

"gemini-2.5-flash"

)



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

Education:

{data['education']}

Skills:

{data['skills']}

Projects:

{data['projects']}

Experience:

{data['experience']}

Achievements:

{data['achievements']}

Career Objective:

{data['objective']}

Format professionally.

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