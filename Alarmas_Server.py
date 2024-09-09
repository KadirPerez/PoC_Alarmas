import csv

class Alarmas:
    archivo_csv = 'alarmas.csv'

    @classmethod
    def generarAlarma(self, token, texto, metodos, fecha):
        nueva_alarma = {"token": token, "texto": texto, "metodos": metodos, "fecha": fecha}
        
        # Escribimos la nueva alarma en el archivo CSV
        with open(self.archivo_csv, mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["token", "texto", "metodos", "fecha"])
            # Si es la primera vez que se escribe en el archivo, añadimos el encabezado
            if file.tell() == 0:
                writer.writeheader()
            writer.writerow(nueva_alarma)

        return nueva_alarma

    @classmethod
    def mostrarAlarmas(self, token):
        alarmas_mostrar = []

        # Leemos las alarmas desde el archivo CSV
        try:
            with open(self.archivo_csv, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    # Filtramos las alarmas que corresponden al token del usuario
                    if row["token"] == token:
                        alarmas_mostrar.append(row)
        except FileNotFoundError:
            print("No hay alarmas registradas.")

        return alarmas_mostrar

    @classmethod
    def eliminarAlarma(self, token, id):
        alarmas_restantes = []

        # Leemos las alarmas y eliminamos la que corresponde al 'id' dado
        try:
            with open(self.archivo_csv, mode='r') as file:
                reader = csv.DictReader(file)
                for i, row in enumerate(reader):
                    # Solo añadimos las alarmas que no coincidan con el 'id'
                    if str(i) != id or row["token"] != token:
                        alarmas_restantes.append(row)

            # Sobrescribimos el archivo CSV con las alarmas restantes
            with open(self.archivo_csv, mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=["token", "texto", "metodos", "fecha"])
                writer.writeheader()
                writer.writerows(alarmas_restantes)

            print(f"Alarma con ID {id} eliminada.")
            return True

        except FileNotFoundError:
            print("No se encontraron alarmas para eliminar.")
            return False
