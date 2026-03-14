from cubo import Cubo
from paralelepipedo import Paralelepipedo
from cilindro import Cilindro
from esfera import Esfera
from cono import Cono
from figura import Figura


def imprimir_volumen(figura: Figura):
    print("Volumen:")
    print(figura.volumen())
    print()


def main():

    cubo = Cubo(3)
    paralelepipedo = Paralelepipedo(2, 3, 4)
    cilindro = Cilindro(2, 5)
    esfera = Esfera(3)
    cono = Cono(2, 6)

    while True:

        print("1. Volumen del cubo")
        print("2. Volumen del paralelepipedo")
        print("3. Volumen del cilindro")
        print("4. Volumen de la esfera")
        print("5. Volumen del cono")
        print()
        print("Escriba 'finalizar' si desea salir")

        opcion = input().strip().lower()

        if opcion == "finalizar":
            break

        if opcion == "1":
            imprimir_volumen(cubo)

        elif opcion == "2":
            imprimir_volumen(paralelepipedo)

        elif opcion == "3":
            imprimir_volumen(cilindro)

        elif opcion == "4":
            imprimir_volumen(esfera)

        elif opcion == "5":
            imprimir_volumen(cono)

        else:
            print("opcion invalida\n")


main()
