
#Las clases en python se definen en Pascal Case (por convencion)
class Celular:
    def __init__(self, modelo, marca, memoria, precio):
        self.modelo = modelo
        self.marca = marca
        self.memoria = memoria
        self.precio = precio
        self.en_produccion = False

    def iniciar_produccion(self):
        self.en_produccion = True
        print(f"Produccion del celular {self.modelo} Ha comenzado")

    def finalizar_produccion(self):
        self.en_produccion = False
        print(f"Producción del celular {self.modelo} ha finalizado.")

    def obtener_info(self):
        return f'{self.marca} {self.modelo} - {self.memoria}GB - ${self.precio}'