import json
import os

student_info = json.loads(open("characters/student_info.json", "r", encoding="utf-8").read())
schools = student_info.keys()

for school in schools:
    print(f"[+] Creating directory for {school}")
    os.makedirs("characters/" + school, exist_ok=True)
    os.makedirs("assets/" + school, exist_ok=True)

    print(f"[+] Creating .gitkeep for {school}")
    with open("characters/" + school + "/.gitkeep", "w") as f:
        pass
    with open("assets/" + school + "/.gitkeep", "w") as f:
        pass
    characters = student_info[school]
    for student in characters:
        name = student["en"]
        print(f"[+] Creating directory for {name}")
        os.makedirs("characters/" + school + "/" + name, exist_ok=True)
        os.makedirs("assets/" + school + "/" + name, exist_ok=True)
        print(f"[+] Creating .gitkeep for {name}")
        with open("characters/" + school + "/" + name + "/.gitkeep", "w") as f:
            pass
        with open("assets/" + school + "/" + name + "/.gitkeep", "w") as f:
            pass
        student_types = student["css"][0]
        for student_type in student_types:
            print(f"[+] Creating directory for {name} - {student_type}")
            os.makedirs("characters/" + school + "/" + name + "/" + student_type, exist_ok=True)
            os.makedirs("assets/" + school + "/" + name + "/" + student_type, exist_ok=True)
            print(f"[+] Creating .gitkeep for {name} - {student_type}")
            with open("characters/" + school + "/" + name + "/" + student_type + "/.gitkeep", "w") as f:
                pass
            with open("assets/" + school + "/" + name + "/" + student_type + "/.gitkeep", "w") as f:
                pass
            file_name = f"{name.lower().replace(' ', '_')}_{student_type.lower().replace(' ', '_')}.css"
            if student_type == "default":
                file_name = f"{name.lower().replace(' ', '_')}.css"
            print(f"[+] Creating {file_name}")
            with open("characters/" + school + "/" + name + "/" + student_type + "/" + file_name, "w") as f:
                pass