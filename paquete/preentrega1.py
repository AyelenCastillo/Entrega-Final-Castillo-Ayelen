import json

def load_users():
    try:
        with open('users.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_users(users):
    with open('users.json', 'w') as file:
        json.dump(users, file, indent=4)

def register():
    users = load_users()
    user_name = input("Ingresa un nombre de usuario: ")
    if user_name in users:
        print("El usuario ya existe. Intenta con otro nombre.")
    else:
        password = input("Ingresa una contraseña: ")
        users[user_name] = password
        save_users(users)
        print("Usuario registrado correctamente.")

def log_in():
    users = load_users()
    user_name = input("Ingresa tu nombre de usuario: ")
    password = input("Ingresa tu contraseña: ")
    if user_name in users and users[user_name] == password:
        print("Inicio de sesión exitoso.")
        return user_name
    else:
        print("Nombre de usuario o contraseña incorrectos.")
        return None

def show():
    users = load_users()
    print("\nUsuarios registrados:")
    for user, password in users.items():
        print(f"Usuario: {user}, Contraseña: {password}")

def obtener_user_name():
    return log_in()
