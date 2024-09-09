import csv

class Suscripcion:

    def suscribirse(id, password, confirmacion):

        if confirmacion == '1':
            # Solo escribimos la información de suscripción directamente en el archivo
            with open('usuarios.csv', mode='a', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['id', 'password', 'suscrito']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                # Si el archivo es nuevo, agregamos el encabezado
                csvfile.seek(0, 2)  # Mueve el cursor al final del archivo
                if csvfile.tell() == 0:
                    writer.writeheader()

                # Escribimos la nueva suscripción
                writer.writerow({
                    'id': id,
                    'password': password,
                    'suscrito': 'True'
                })

            print(f"Usuario {id} suscrito correctamente.")
            return True
        return False
