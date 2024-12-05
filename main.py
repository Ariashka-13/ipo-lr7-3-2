import json

with open("dump.json", "r", encoding="UTF-8") as file:
    data = json.load(file)

n = input("Введите номер квалификации: ")

for skill in data:
    if skill.get("model") == "data.skill":
        if skill["fields"].get("code") == n:
            skill_title = skill["fields"].get("title")
            skill_specialty = skill["fields"].get("specialty")
            break
            
if skill_title and skill_specialty:            
    for specialty in data:
        if specialty.get("model") == "data.specialty":
            if skill_specialty == specialty.get("pk"):
                specialty_code = specialty["fields"].get("code")
                specialty_title = specialty["fields"].get("title")
                specialty_educational = specialty["fields"].get("c_type")
                break  

if skill_title and specialty_title:
    print("Найдено".center(30, '='))
    print(f"{specialty_code} >> Специальность '{specialty_title}' , {specialty_educational}")
    print(f"{n} >> Квалификация '{skill_title}'")
else:
    print("Не Найдено".center(30, '='))   
