from collections import Counter

def count_skills(jobs):

    all_skills = []

    for job in jobs:
        for skill in job["skills"]:
            all_skills.append(skill)

    counter = Counter(all_skills)

    top_skills = counter.most_common(10)

    return top_skills