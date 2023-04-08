from selenium import webdriver
import json
import time

def main() :
    overall_grades = json.loads(open("niche_overall_grades.json", "r").read())
    academic_grades = json.loads(open("niche_academic_grades.json", "r").read())
    value_grades = json.loads(open("niche_value_grades.json", "r").read())
    diversity_grades = json.loads(open("niche_diversity_grades.json", "r").read())
    campus_grades = json.loads(open("niche_campus_grades.json", "r").read())
    athletics_grades = json.loads(open("niche_athletics_grades.json", "r").read())
    party_scene_grades = json.loads(open("niche_party_scene_grades.json", "r").read())
    professors_grades = json.loads(open("niche_professors_grades.json", "r").read())
    location_grades = json.loads(open("niche_location_grades.json", "r").read())
    dorms_grades = json.loads(open("niche_dorms_grades.json", "r").read())
    campus_food_grades = json.loads(open("niche_campus_food_grades.json", "r").read())
    student_life_grades = json.loads(open("niche_student_life_grades.json", "r").read())
    safety_grades = json.loads(open("niche_safety_grades.json", "r").read())

    f = open("Included Schools.txt", "r")
    for school in f.readlines() :
        school = school[:-1]
        time.sleep(5)
        niche_grades = fetch_niche_grades(school)
        overall_grades[school] = niche_grades[0]
        academic_grades[school] = niche_grades[1]
        value_grades[school] = niche_grades[2]
        diversity_grades[school] = niche_grades[3]
        campus_grades[school] = niche_grades[4]
        athletics_grades[school] = niche_grades[5]
        party_scene_grades[school] = niche_grades[6]
        professors_grades[school] = niche_grades[7]
        location_grades[school] = niche_grades[8]
        dorms_grades[school] = niche_grades[9]
        campus_food_grades[school] = niche_grades[10]
        student_life_grades[school] = niche_grades[11]
        safety_grades[school] = niche_grades[12]
    with open("niche_overall_grades.json", "w") as g :
        json.dump(overall_grades, g)
    with open("niche_academic_grades.json", "w") as g :
        json.dump(academic_grades, g)
    with open("niche_value_grades.json", "w") as g :
        json.dump(value_grades, g)
    with open("niche_diversity_grades.json", "w") as g :
        json.dump(diversity_grades, g)
    with open("niche_campus_grades.json", "w") as g :
        json.dump(campus_grades, g)
    with open("niche_athletics_grades.json", "w") as g :
        json.dump(athletics_grades, g)
    with open("niche_party_scene_grades.json", "w") as g :
        json.dump(party_scene_grades, g)
    with open("niche_professors_grades.json", "w") as g :
        json.dump(professors_grades, g)
    with open("niche_location_grades.json", "w") as g :
        json.dump(location_grades, g)
    with open("niche_dorms_grades.json", "w") as g :
        json.dump(dorms_grades, g)
    with open("niche_campus_food_grades.json", "w") as g :
        json.dump(campus_food_grades, g)
    with open("niche_student_life_grades.json", "w") as g :
        json.dump(student_life_grades, g)
    with open("niche_safety_grades.json", "w") as g :
        json.dump(safety_grades, g)
    

def fetch_niche_grades(school_name) :
    from googlesearch import search
    google_results = search("university " + school_name + " niche", num_results=1, sleep_interval=1)
    link = ""
    for result in google_results :
        link = result
    print(school_name)
    niche_grades = [-1] * 13
    try :
        niche_grades = extract_niche_grades(link)
    except Exception :
        print("Failed")
    return niche_grades

def extract_niche_grades(link) :
    grades = []
    driver = webdriver.Chrome("scripts/chromedriver.exe")
    driver.get(link)
    source = driver.page_source

    #overall
    source = source[source.index('<div class="overall-grade__niche-grade">'):]
    source = source[source.index('<span class="visually-hidden">grade&nbsp;</span>') + 45:]
    source = source[source.index(">")+1:]
    overall_grade = source[:source.index("<")].replace(" minus", "-")
    print("Overall : " + overall_grade)
    grades.append(overall_grade)
    #overall

    #academics
    source = source[source.index('<div class="profile-grade__label">Academics</div>'):]
    source = source[source.index('<span class="visually-hidden">grade&nbsp;</span>') + 45:]
    source = source[source.index(">")+1:]
    academics_grade = source[:source.index("<")].replace(" minus", "-")
    print("Academics : " + academics_grade)
    grades.append(academics_grade)
    #academics

    #value
    source = source[source.index('<span class="visually-hidden">grade&nbsp;</span>'):]
    source = source[source.index("</span>")+7:]
    value_grade = source[:source.index("<")].replace(" minus", "-")
    print("Value : " + value_grade)
    grades.append(value_grade)
    #value

    #diversity
    source = source[source.index('<span class="visually-hidden">grade&nbsp;</span>'):]
    source = source[source.index("</span>")+7:]
    diversity_grade = source[:source.index("<")].replace(" minus", "-")
    print("Diversity : " + diversity_grade)
    grades.append(diversity_grade)
    #diversity

    #campus
    source = source[source.index('<span class="visually-hidden">grade&nbsp;</span>'):]
    source = source[source.index("</span>")+7:]
    campus_grade = source[:source.index("<")].replace(" minus", "-")
    print("Campus : " + campus_grade)
    grades.append(campus_grade)
    #campus

    #athletics
    source = source[source.index('<span class="visually-hidden">grade&nbsp;</span>'):]
    source = source[source.index("</span>")+7:]
    athletics_grade = source[:source.index("<")].replace(" minus", "-")
    print("Athletics : " + athletics_grade)
    grades.append(athletics_grade)
    #athletics

    #party scene
    source = source[source.index('<span class="visually-hidden">grade&nbsp;</span>'):]
    source = source[source.index("</span>")+7:]
    party_scene_grade = source[:source.index("<")].replace(" minus", "-")
    print("Party Scene : " + party_scene_grade)
    grades.append(party_scene_grade)
    #party scene

    #professors
    source = source[source.index('<span class="visually-hidden">grade&nbsp;</span>'):]
    source = source[source.index("</span>")+7:]
    professors_grade = source[:source.index("<")].replace(" minus", "-")
    print("Professors : " + professors_grade)
    grades.append(professors_grade)
    #professors

    #location
    source = source[source.index('<span class="visually-hidden">grade&nbsp;</span>'):]
    source = source[source.index("</span>")+7:]
    location_grade = source[:source.index("<")].replace(" minus", "-")
    print("Location : " + location_grade)
    grades.append(location_grade)
    #location

    #dorms
    source = source[source.index('<span class="visually-hidden">grade&nbsp;</span>'):]
    source = source[source.index("</span>")+7:]
    dorms_grade = source[:source.index("<")].replace(" minus", "-")
    print("Dorms : " + dorms_grade)
    grades.append(dorms_grade)
    #dorms

    #campus food
    source = source[source.index('<span class="visually-hidden">grade&nbsp;</span>'):]
    source = source[source.index("</span>")+7:]
    campus_food_grade = source[:source.index("<")].replace(" minus", "-")
    print("Campus Food : " + campus_food_grade)
    grades.append(campus_food_grade)
    #campus food

    #student life
    source = source[source.index('<span class="visually-hidden">grade&nbsp;</span>'):]
    source = source[source.index("</span>")+7:]
    student_life_grade = source[:source.index("<")].replace(" minus", "-")
    print("Student Life : " + student_life_grade)
    grades.append(student_life_grade)
    #student life

    #safety
    source = source[source.index('<span class="visually-hidden">grade&nbsp;</span>'):]
    source = source[source.index("</span>")+7:]
    safety_grade = source[:source.index("<")].replace(" minus", "-")
    print("Safety : " + safety_grade)
    grades.append(safety_grade)
    #safety

    return grades

main()