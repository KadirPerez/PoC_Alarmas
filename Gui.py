from ApiGateway import APIGateway
import getpass

#Interpretacion de una gui disenada usando el API
def Gui():
    api = APIGateway()
    opcion = '0'

    while opcion != '3':
        print("\n--- Alarmas ---")
        print("1. Iniciar sesión")
        print("2. Suscribirse a alarmas")
        print("3. Salir")
        opcion = input("Ingrese su opción: ")

        if opcion == '1':
            id = input("\nIngresar id: ")
            pasword = getpass.getpass("Ingresar contraseña: ")
            token = api.autenticarse(id, pasword)
            if token != None:
                opcion1 = '0'
                while opcion1 != '4':
                    print("\n--- Sistema de alarmas ---")
                    print("1. Crear una alarma")
                    print("2. Mostrar alarmas")
                    print("3. Borrar alarmas")
                    print("4. Cerrar sesión")
                    opcion1 = input("Ingrese su opción: ")

                    if opcion1 == '1':
                        print(api.generarSugerencia(token))
                        texto = input("Ingrese la descripcion: ")
                        metodos = input("Metodos: ")
                        fecha = input("Fecha: ")
                        nuevaAlarma = api.generarAlarma(token, texto, metodos, fecha)
                        api.guardarInfo(token, nuevaAlarma)
                    elif opcion1 == '2':
                        print(api.mostrarAlarmas(token))
                    elif opcion1 == '3':
                        idDelete = input("Id de la alarma a eliminar: ")
                        api.eliminarAlarma(token, idDelete)
                    elif opcion1 == '4':
                        print("Sesión cerrada.")
                    else:
                        print("Opción inválida. Intente de nuevo.")

        elif opcion == '2':
            id = input("\nIngresar id: ")
            pasword = getpass.getpass("Ingresar contraseña: ")
            print("\n--- PayPal ---")
            print("1. PayPal confirmó el pago")
            print("Cualquier otra tecla: PayPal no confirmó el pago")
            confirmacion = input("Opción: ")

            if api.suscribirse(id, pasword, confirmacion):
                print("Te suscribiste correctamente.")
            else:
                print("No te suscribiste correctamente.")
        
        elif opcion == '3':
            print("¡Adiós!")
        else:
            print("Opción inválida. Inténtelo de nuevo.")

if __name__ == "__main__":
    Gui()
