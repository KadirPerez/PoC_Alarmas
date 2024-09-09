import csv

class Autenticacion:
    @staticmethod
    def cargar_usuarios():
        usuarios = {}
        try:
            with open('usuarios.csv', mode='r', newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    usuarios[row['id']] = {
                        'password': row['password'],
                        'suscrito': row['suscrito'] == 'True'
                    }
        except FileNotFoundError:
            print("El archivo usuarios.csv no existe. Se creará uno nuevo.")
            with open('usuarios.csv', mode='w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['id', 'password', 'suscrito']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
            usuarios = {}
        return usuarios

    @classmethod
    def Autenticar(self, id, password):
        usuarios = self.cargar_usuarios()
        if id in usuarios and usuarios[id]['password'] == password:
            return "Hola este es un token"
        else:
            return None
