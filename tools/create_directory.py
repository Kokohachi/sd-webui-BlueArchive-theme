import json
import os

student_info = json.loads(open("students/student_info.json", "r", encoding="utf-8").read())
schools = student_info.keys()

for school in schools:
    print(f"[+] Creating directory for {school}")
    os.makedirs("students/" + school, exist_ok=True)
    os.makedirs("assets/" + school, exist_ok=True)

    print(f"[+] Creating .gitkeep for {school}")
    with open("students/" + school + "/.gitkeep", "w") as f:
        pass
    with open("assets/" + school + "/.gitkeep", "w") as f:
        pass
    students = student_info[school]
    for student in students:
        name = student["en"]
        print(f"[+] Creating directory for {name}")
        os.makedirs("students/" + school + "/" + name, exist_ok=True)
        os.makedirs("assets/" + school + "/" + name, exist_ok=True)
        print(f"[+] Creating .gitkeep for {name}")
        with open("students/" + school + "/" + name + "/.gitkeep", "w") as f:
            pass
        with open("assets/" + school + "/" + name + "/.gitkeep", "w") as f:
            pass
        student_types = student["css"][0]
        for student_type in student_types:
            print(f"[+] Creating directory for {name} - {student_type}")
            os.makedirs("students/" + school + "/" + name + "/" + student_type, exist_ok=True)
            os.makedirs("assets/" + school + "/" + name + "/" + student_type, exist_ok=True)
            print(f"[+] Creating .gitkeep for {name} - {student_type}")
            with open("students/" + school + "/" + name + "/" + student_type + "/.gitkeep", "w") as f:
                pass
            with open("assets/" + school + "/" + name + "/" + student_type + "/.gitkeep", "w") as f:
                pass
            file_name = f"{name.lower().replace(' ', '_')}_{student_type.lower().replace(' ', '_')}.css"
            if student_type == "default":
                file_name = f"{name.lower().replace(' ', '_')}.css"
            print(f"[+] Creating {file_name}")
            with open("students/" + school + "/" + name + "/" + student_type + "/" + file_name, "w") as f:
                pass