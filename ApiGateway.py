# Importamos las clases desde otros módulos que manejan la lógica del servidor
from Alarmas_Server import Alarmas
from Autenticacion_Server import Autenticacion
from Suscripcion_Server import Suscripcion
from Sugerencia_Server import Sugerencia

# Definimos la clase APIGateway, que actúa como una puerta de enlace
# que centraliza y coordina las peticiones hacia diferentes servicios.
class APIGateway:

    # Método estático para generar una sugerencia.
    # Se toma un token como argumento para identificar al usuario autenticado.
    def generarSugerencia(self, token):
        # Llama al método generarSugerencia de la clase Sugerencia y le pasa el token.
        return Sugerencia.generarSugerencia(token)

    # Método estático para autenticar al usuario.
    # Toma un 'id' y una 'password' como argumentos para verificar credenciales.
    def autenticarse(self, id, pasword):
        # Llama al método Autenticar de la clase Autenticacion y le pasa las credenciales.
        return Autenticacion.Autenticar(id, pasword)

    # Método para suscribirse a un servicio. 
    # Requiere el 'id', 'password', y la confirmación del password como parámetros.
    def suscribirse(self, id, password, confirmacion):
        # Llama al método suscribirse de la clase Suscripcion para crear una cuenta.
        return Suscripcion.suscribirse(id, password, confirmacion)

    # Método para generar una alarma.
    # Requiere un 'token' de autenticación, el 'texto' de la alarma, los 'metodos' de notificación y la 'fecha' en que se activa.
    def generarAlarma(self, token, texto, metodos, fecha):
        # Llama al método generarAlarma de la clase Alarmas y pasa los datos de la alarma.
        return Alarmas.generarAlarma(token, texto, metodos, fecha)

    # Método para mostrar las alarmas de un usuario autenticado.
    # Se utiliza el 'token' del usuario para identificar qué alarmas mostrar.
    def mostrarAlarmas(self, token):
        # Llama al método mostrarAlarmas de la clase Alarmas para obtener las alarmas del usuario.
        return Alarmas.mostrarAlarmas(token)

    # Método para eliminar una alarma específica.
    # Requiere el 'id' de la alarma y el 'token' del usuario autenticado.
    def eliminarAlarma(self, id, token):
        # Llama al método eliminarAlarma de la clase Alarmas para borrar una alarma específica.
        return Alarmas.eliminarAlarma(id, token)

    def guardarInfo(self, token, alarma):
        return Sugerencia.guardarInfo(token, alarma)