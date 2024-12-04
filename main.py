import json

with open("dump.json", "r", encoding="UTF-8") as file:
    data = json.load(file)

n = input("Введите номер квалификации: ")
found = False

for skill in data:
    if skill.get("model") == "data.skill":
        if skill["fields"].get("code") == n:
            skill_title = skill["fields"].get("title")
            skill_specialty = skill["fields"].get("specialty")
            for specialty in data:
                if specialty.get("model") == "data.specialty":
                    if skill_specialty == specialty.get("pk"):
                        specialty_code = specialty["fields"].get("code")
                        specialty_title = specialty["fields"].get("title")
                        specialty_educational = specialty["fields"].get("c_type")
                        print("=============== Найдено ===============")
                        print(f"{specialty_code} >> Специальность '{specialty_title}' , {specialty_educational}")
                        print(f"{n} >> Квалификация '{skill_title}'")
                        found = True
                        break
            if found:
                break        
if not found:
    print("=============== Не Найдено ===============")                
