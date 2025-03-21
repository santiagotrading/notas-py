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
