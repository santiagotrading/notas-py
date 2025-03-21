users = []  # Lista para almacenar usuarios
grades = []  # Lista para almacenar las notas

def register_user():
    print("\n--- Registro ---")
    username = input("Ingrese nombre de usuario: ")
    user_type = input("Ingrese tipo (profesor/estudiante): ")
    password = input("Ingrese contraseña: ")
    users.append({"username": username, "user_type": user_type, "password": password})
    print("Usuario registrado con éxito.\n")


