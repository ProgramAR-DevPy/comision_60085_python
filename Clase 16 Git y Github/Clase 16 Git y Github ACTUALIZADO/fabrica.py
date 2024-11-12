from celular import Celular

class Fabrica:
    def __init__(self, nombre):
        self.nombre = nombre
        self.celulares_en_produccion = []

    def fabricar_celular(self, modelo, marca, memoria, precio):
        celular = Celular(modelo, marca, memoria, precio)
        celular.iniciar_produccion()
        self.celulares_en_produccion.append(celular)
        return celular

    def finalizar_celular(self, celular):
        celular.finalizar_produccion()
        print(f"{celular.obtener_info()} ha sido fabricado.")

    def mostrar_celulares(self):
        print(f"Celulares en producción en la fábrica {self.nombre}:")
        for celular in self.celulares_en_produccion:
            print(celular.obtener_info())

