from flask import Flask, render_template, request
from analyzer import analyze_job
from scraper import get_jobs
from database import init_db
from stats import count_skills

app = Flask(__name__)

init_db()

@app.route("/", methods=["GET","POST"])
def index():

    skills = []

    if request.method == "POST":

        description = request.form["description"]

        skills = analyze_job(description)

    jobs = get_jobs()

    top_skills = count_skills(jobs)

    return render_template(
        "index.html",
        skills=skills,
        jobs=jobs,
        top_skills=top_skills
    )

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)