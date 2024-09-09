import csv

class Sugerencia:
    archivo_csv = 'sugerencias.csv'
    
    @classmethod
    def guardarInfo(self, token, alarma):
        # Guardamos la información de la alarma asociada al token para generar sugerencias más adelante
        info = {"token": token, "alarma": alarma}

        # Escribimos la información en el archivo CSV
        with open(self.archivo_csv, mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["token", "alarma"])
            # Si es la primera vez que se escribe en el archivo, añadimos el encabezado
            if file.tell() == 0:
                writer.writeheader()
            writer.writerow(info)

        return True

    
    @classmethod
    def generarSugerencia(self, token):
        sugerencia = "Sugerencia"
        return sugerencia
