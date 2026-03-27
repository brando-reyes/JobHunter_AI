import spacy

nlp = spacy.load("en_core_web_sm")

skills = [
    "python",
    "flask",
    "django",
    "fastapi",
    "sql",
    "postgresql",
    "mysql",
    "mongodb",
    "docker",
    "kubernetes",
    "aws",
    "gcp",
    "azure",
    "git",
    "github",
    "api",
    "rest api",
    "graphql",
    "javascript",
    "react",
    "node",
    "linux",

]

def analyze_job(description):

    doc = nlp(description.lower())

    found_skills = []

    for skill in skills:
        if skill in doc.text:
            found_skills.append(skill)

    return found_skills