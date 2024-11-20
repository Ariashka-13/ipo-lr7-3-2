import json

with open("C:\\Users\\Dell\\Desktop\\py\\json2\\dump.json", "r", encoding="UTF-8") as file:
    data = json.load(file)

n = int(input("Введите номер квалификации: "))

for skill in data:
    if skill.get("model") == "data.skill":
        if skill["fields"].get("specialty") == n:
            skill_code = skill["fields"].get("code")
            skill_title = skill["fields"].get("title")
            
            for profession in data:
                if profession.get("model") == "data.specialty":
                    specialty_code = profession["fields"].get("code")
                    if specialty_code in skill_code:
                        specialty_title = profession["fields"].get("title")
                        specialty_educational = profession["fields"].get("c_type")
                        
            print("=============== Найдено ===============")
            print(f"{specialty_code} >> Специальность '{specialty_title}' , {specialty_educational}")
            print(f"{skill_code} >> Квалификация '{skill_title}'")
            break
else:
    print("=============== Не Найдено ===============")
