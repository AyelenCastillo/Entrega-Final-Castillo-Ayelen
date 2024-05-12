from paquete.clientes import Cliente 
from paquete import preentrega1

while True:
    print("\n1. Registrar usuario")
    print("2. Iniciar sesión")
    print("3. Mostrar usuarios")
    print("4. Realizar compra forzada")
    print("5. Salir")
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        preentrega1.register()
    elif opcion == "2":
        user_name = preentrega1.log_in()
        if user_name:  
            print(f"Bienvenido, {user_name}!")
    elif opcion == "3":
        preentrega1.show()
    elif opcion == "4":
        user_name = preentrega1.obtener_user_name()
        if user_name: 
            nombre_producto = input("Ingresa el nombre del producto: ")
            cliente = Cliente(user_name, "example@example.com", "123456789", "Calle Principal 123")
            cliente.buy(nombre_producto)
    elif opcion == "5":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")
