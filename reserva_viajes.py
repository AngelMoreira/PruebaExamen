usuarios_registrados = []

reservas = []

def registrar_usuario():
    """
    Función para registrar un nuevo usuario en el sistema.
    """
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    if nombre_usuario in usuarios_registrados:
        print("El nombre de usuario ya existe. Por favor, elija otro.")
    else:
        usuarios_registrados.append(nombre_usuario)
        print("Usuario registrado con éxito.")

def reservar_viaje():
    """
    Función para reservar un viaje.
    """
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    if nombre_usuario not in usuarios_registrados:
        print("No estás registrado. ¿Deseas registrarte ahora? si/no")
        respuesta = input().lower()
        if respuesta == "si":
            registrar_usuario()
            reservar_viaje()
        else:
            print("No puedes reservar un viaje sin estar registrado.")
            return
    destino = input("Ingrese el destino del viaje: ")
    fecha = input("Ingrese la fecha del viaje dia/mes/año: ")
    reserva = {"nombre_usuario": nombre_usuario, "destino": destino, "fecha": fecha}
    reservas.append(reserva)
    print("Reserva realizada con éxito.")

def ver_reservas():
    """
    Función para ver las reservas de un usuario.
    """
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    if nombre_usuario not in usuarios_registrados:
        print("No estás registrado.")
        return
    reservas_usuario = [reserva for reserva in reservas if reserva["nombre_usuario"] == nombre_usuario]
    if not reservas_usuario:
        print("No tienes reservas.")
    else:
        print("Tus reservas:")
        for reserva in reservas_usuario:
            print(f"Destino: {reserva['destino']}, Fecha: {reserva['fecha']}")

def cancelar_reserva():
    """
    Función para cancelar una reserva.
    """
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    if nombre_usuario not in usuarios_registrados:
        print("No estás registrado.")
        return
    reservas_usuario = [reserva for reserva in reservas if reserva["nombre_usuario"] == nombre_usuario]
    if not reservas_usuario:
        print("No tienes reservas.")
    else:
        print("Tus reservas:")
        for i, reserva in enumerate(reservas_usuario):
            print(f"{i+1}. Destino: {reserva['destino']}, Fecha: {reserva['fecha']}")
        numero_reserva = int(input("Ingrese el número de la reserva que desea cancelar: "))
        if numero_reserva < 1 or numero_reserva > len(reservas_usuario):
            print("Número de reserva inválido.")
        else:
            reserva_a_cancelar = reservas_usuario[numero_reserva - 1]
            reservas.remove(reserva_a_cancelar)
            print("Reserva cancelada con éxito.")

def menu_principal():
    """
    Función para mostrar el menú principal del sistema.
    """
    while True:
        print("Menú principal:")
        print("1. Registrar un usuario")
        print("2. Reservar un viaje")
        print("3. Ver reservas")
        print("4. Cancelar una reserva")
        print("5. Salir del programa")
        opcion = input("Ingrese su opción: ")
        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            reservar_viaje()
        elif opcion == "3":
            ver_reservas()
        elif opcion == "4":
            cancelar_reserva()
        elif opcion == "5":
            print("Gracias por utilizar el sistema de reservas.")
            break
        else:
            print("Opción inválida. Por favor, inténtelo de nuevo.")

if __name__ == "__main__":
    menu_principal()