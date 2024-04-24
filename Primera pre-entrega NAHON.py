usuarios = {}

def registrar_usuario():
    nombre = input("Ingrese un nombre de usuario: ")
    if nombre in usuarios:
        print("Ese nombre ya está en uso.")
        return  

    while True: 
        contraseña = input("Ingrese una contraseña que contenga una mayuscula y un caracter especial: ")
        if any(caracter.isupper() for caracter in contraseña) and any(caracter in "!@#$%^&*()-_=+[]{};:',.<>/?\\" for caracter in contraseña):
            usuarios[nombre] = contraseña
            print("Usuario registrado.")
            break
        else:
            print("Error: la contraseña debe tener una mayúscula y un caracter especial.")

def mostrar_usuarios():
    if usuarios:
        print("Estos son todos los usuarios registrados:")
        for usuario, contraseña in usuarios.items():
            print(f"Usuario: {usuario}, Contraseña: {contraseña}")
    else:
        print("Sin usuarios registrados en el sistema.")

def ingresar():
    while True:  
        nombre = input("Ingrese nombre de usuario: ")
        if nombre in usuarios:
            while True:  
                contraseña = input("Ingrese contraseña: ")
                if contraseña == usuarios[nombre]:
                    print("Acceso permitido! Bienvenido/a. al sistema")
                    input("Presione cualquier tecla para volver al menú principal...")
                    return
                else:
                    print("Cntraseña erronea. Intente nuevamente.")
        else:
            print("Nombre de usuario no encontrado. Intente de nuevo.")


def menu():
    while True:
        print("\n1. Registrar un usuario nuevo")
        print("2. Mostrar todos los usuarios")
        print("3. Entrar a tu usuario")
        print("4. Salir del programa")
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            registrar_usuario()
        elif opcion == '2':
            mostrar_usuarios()
        elif opcion == '3':
            ingresar()
        elif opcion == '4':
            print("Hasta luego!")
            break
        else:
            print("Opción inexistente, intentar nuevamente.")

menu()
