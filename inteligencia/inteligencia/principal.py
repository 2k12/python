import formatos
import formatos2


def ingreso():
    n = int(input("$ "))
    return n


def menu():
    print("------------MENU-INTERACTIVO--------------")
    print("INGRESE-NUMERO-CORRESPONDIENTE-A-LA-OPCION")
    print("-----------AUTOR:-Pastillo-Joan-----------")
    print("------------------------------------------")
    print("0 -> SALIR")
    print("1 -> EJERCICIOS FORMATOS1")
    print("2 -> EJERCICIOS FORMATOS2")


def aplicativo():
    menu()
    n=ingreso()
    while n > 0 :
        if n == 1:
            formatos.cargarimagen()
            n=ingreso()
        elif n == 2:
            formatos2.cargarvideo()
            n=ingreso()
        else:
            break



aplicativo()