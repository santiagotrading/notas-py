users = []  # Lista para almacenar usuarios
grades = []  # Lista para almacenar las notas

def register_user():
    print("\n--- Registro ---")
    username = input("Ingrese nombre de usuario: ")
    user_type = input("Ingrese tipo (profesor/estudiante): ")
    password = input("Ingrese contraseña: ")
    users.append({"username": username, "user_type": user_type, "password": password})
    print("Usuario registrado con éxito.\n")


def login():
    print("\n--- Login ---")
    username = input("Usuario: ")
    password = input("Contraseña: ")
    for user in users:
        if user["username"] == username and user["password"] == password:
            print("Login exitoso\n")
            return user
    print("Usuario o contraseña incorrectos.\n")
    return None

def add_grade():
    print("\n--- Agregar Nota ---")
    student = input("Ingrese nombre del estudiante: ")
    subject = input("Ingrese la materia: ")
    grade = float(input("Ingrese la nota: "))
    grades.append({"student": student, "subject": subject, "grade": grade})
    print("Nota agregada con éxito.\n")

def view_grades():
    print("\n--- Ver Notas ---")
    student = input("Ingrese su nombre para ver sus notas: ")
    found_grades = [g for g in grades if g["student"] == student]
    if found_grades:
        for g in found_grades:
            print(f"Materia: {g['subject']}, Nota: {g['grade']}")
    else:
        print("No se encontraron notas.\n")
