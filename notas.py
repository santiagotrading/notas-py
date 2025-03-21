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

def menu(user):
    while True:
        print("\n--- Menú ---")
        print("1. Ver Notas")
        if user["user_type"] == "profesor":
            print("2. Agregar Nota")
        print("3. Cerrar Sesión")
        option = input("Seleccione una opción: ")
        match option:
            case "1":
                view_grades()
            case "2":
                if user["user_type"] == "profesor":
                    add_grade()
            case "3":
                print("Cerrando sesión...\n")
                break
            case _:
                print("Opción inválida.\n")

def main():
    while True:
        print("\n--- Sistema de Gestión de Notas ---")
        print("1. Registrar Usuario")
        print("2. Iniciar Sesión")
        print("3. Salir")
        option = input("Seleccione una opción: ")
        match option:
            case "1":
                register_user()
            case "2":
                user = login()
                if user:
                    menu(user)
            case "3":
                print("Saliendo...\n")
                break
            case _:
                print("Opción inválida.\n")

main()