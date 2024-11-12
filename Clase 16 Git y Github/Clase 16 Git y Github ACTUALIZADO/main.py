from fabrica import Fabrica

# def main():
#     fabrica = Fabrica("Powered By CodificAr Dev")

#     # Fabricar celulares
#     celular1 = fabrica.fabricar_celular("Galaxy S23", "Samsung", 128, 999)
#     celular2 = fabrica.fabricar_celular("iPhone 14", "Apple", 256, 1199)

#     # Mostrar celulares en producción
#     fabrica.mostrar_celulares()

#     # Finalizar producción y "vender" los celulares
#     fabrica.finalizar_celular(celular1)
#     fabrica.finalizar_celular(celular2)

#     # Mostrar nuevamente los celulares en producción
#     fabrica.mostrar_celulares()

# if __name__ == "__main__":
#     main()


def mostrar_menu():
    print("\t --- Powered By CodificAr Dev ---")
    print("\t 1. Fabricar un nuevo celular")
    print("\t 2. Finalizar la producción de un celular")
    print("\t 3. Mostrar celulares en producción")
    print("\t 4. Salir")

def main():
    fabrica = Fabrica("\t Powered By CodificAr Dev")

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            modelo = input("Ingrese el modelo del celular: ")
            marca = input("Ingrese la marca del celular: ")
            memoria = int(input("Ingrese la memoria (GB): "))
            precio = float(input("Ingrese el precio ($): "))
            celular = fabrica.fabricar_celular(modelo, marca, memoria, precio)
            print(f"Celular {celular.obtener_info()} ha sido fabricado y está en producción.")

        elif opcion == "2":
            if not fabrica.celulares_en_produccion:
                print("No hay celulares en producción para finalizar.")
                continue

            fabrica.mostrar_celulares()
            indice = int(input("Seleccione el número del celular a finalizar (1-{}): ".format(len(fabrica.celulares_en_produccion))))
            if 1 <= indice <= len(fabrica.celulares_en_produccion):
                celular_a_finalizar = fabrica.celulares_en_produccion[indice - 1]
                fabrica.finalizar_celular(celular_a_finalizar)
                fabrica.celulares_en_produccion.remove(celular_a_finalizar)  # Eliminarlo de la lista
            else:
                print("Opción inválida.")

        elif opcion == "3":
            fabrica.mostrar_celulares()

        elif opcion == "4":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
