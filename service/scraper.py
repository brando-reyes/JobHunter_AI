import requests
from analyzer import analyze_job

def get_jobs():

    url = "https://remoteok.com/api"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)

    data = response.json()

    jobs = []

    for job in data[1:20]:

        title = job.get("position", "")

        description = job.get("description", "")

        skills = analyze_job(title + " " + description)

        jobs.append({
            "title": title,
            "skills": skills
        })

    return jobs