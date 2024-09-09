class Alarmas:
    alarmas = []

    @classmethod
    def generarAlarma(self, token, texto, metodos, fecha):
        nueva_alarma = "Alarma creada"
        self.alarmas.append(nueva_alarma)
        return nueva_alarma

    @classmethod
    def mostrarAlarmas(self, token):
        if self.alarmas:
            print("Mostrando alarmas:")
            for alarma in self.alarmas:
                print(f"- {alarma}")
        else:
            print("No hay alarmas.")
        return self.alarmas

    @classmethod
    def eliminarAlarma(self, token, id):
        self.alarmas.clear()
        print("Alarma eliminada.")
        return True
