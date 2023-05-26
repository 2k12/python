# * imports
# !--------
import ejercicio_eliminar_letras
import ejercicio_eliminacion_figuras
import ejercicio_extraer_lineas_cdb
import ejercicio_extrear_numeros_cdb
# !--------
import formatos
import formatos2
# !--------
import procesamiento
import procesamiento2
import procesamiento3
import procesamiento4
# !--------
import morfologia
import morfologia2
import morfologia3
import morfologia4
import morfologia5
# !--------
import segmentacion
import segmentacion2
import segmentacion3
import segmentacion4
# !--------
import descripcion
import descripcion2
# !--------
import clasificacion


def ingreso():
    n = input("$ ")
    return n

def menu():
    print("-------------------MENU-INTERACTIVO-------------------")
    print("-------INGRESE-NUMERO-CORRESPONDIENTE-A-LA-OPCION-----")
    print("-----------------AUTOR:-Pastillo-Joan-----------------")
    print("-----------------COLABORADOR:-Cadena-Edwin------------")
    print("-----------------COLABORADOR:-Perez-Jairo-------------")
    print("-----------------COLABORADOR:-Ortega-Dylan------------")
    print("------------------------------------------------------")        
    print("0 -> SALIR")
    print("------------------------------------------------------")
    print("a -> ElIMINAR LETRAS.1     ||   b -> ELIMINAR FIGURAS.2")
    print("c -> EXTRAER  LINEAS.3     ||   d -> EXTRAER  NUMEROS.4")
    print("------------------------------------------------------")
    print("1 -> EJERCICIOS FORMATOS1  || 2 -> EJERCICIOS FORMATOS2")
    print("------------------------------------------------------")
    print("3 -> EJERCICIOS PROCESA.1  || 4 -> EJERCICIOS PROCESA.2")
    print("5 -> EJERCICIOS PROCESA.3  || 6 -> EJERCICIOS PROCESA.4")
    print("------------------------------------------------------")
    print("7 -> EJERCICIOS MORFOLO.1  || 8 -> EJERCICIOS MORFOLO.2")
    print("9 -> EJERCICIOS MORFOLO.3  || 10 -> EJERCICIOS MORFOLO.4")
    print("11 -> EJERCICIOS MORFOLO.5")
    print("--------------------------------------------------------")
    print("12 -> EJERCICIOS SEGMENT.1 || 13 -> EJERCICIOS SEGMENT.2")
    print("14 -> EJERCICIOS SEGMENT.3 || 15 -> EJERCICIOS SEGMENT.4")
    print("--------------------------------------------------------")
    print("16 -> EJERCICIOS DESCRIP.1 || 17 -> EJERCICIOS DESCRIP.2")
    print("--------------------------------------------------------")
    print("18 -> EJERCICIOS CLASIFI.1 ")
    print("--------------------------------------------------------")



def aplicativo():
    menu()
    n=ingreso()

    while isinstance(n, (int,str)) :
        if n == "a":
            ejercicio_eliminar_letras.eliminarletras()
            n=ingreso()
        elif n == "b":
            ejercicio_eliminacion_figuras.main()
            n=ingreso()
        elif n == "c":
            ejercicio_extraer_lineas_cdb.obtenerlineasdelcbd()
            n=ingreso()
        elif n == "d":
            ejercicio_extrear_numeros_cdb.extraer_numeros_codigo_barras()
            n=ingreso()
        elif n == "1":
            formatos.cargarimagen()
            n=ingreso()
        elif n == "2":
            formatos2.cargarvideo()
            n=ingreso()
        elif n == "3":
            procesamiento.main()
            n=ingreso()
        elif n == "4":
            procesamiento2.main()
            n=ingreso()
        elif n == "5":
            procesamiento3.main()
            n=ingreso()
        elif n == "6":
            procesamiento4.main()
            n=ingreso()
        elif n == "7":
            morfologia.main()
            n=ingreso()
        elif n == "8":
            morfologia2.ejercicio()
            n=ingreso()
        elif n == "9":
            morfologia3.puntaspinon()
            n=ingreso()
        elif n == "10":
            morfologia4.ejercicio_clavos()
            n=ingreso()
        elif n == "11":
            morfologia5.llaves()
            n=ingreso()
        elif n == "12":
            segmentacion.main()
            n=ingreso()
        elif n == "13":
            segmentacion2.main()
            n=ingreso()
        elif n == "14":
            segmentacion3.main()
            n=ingreso()
        elif n == "15":
            segmentacion4.main()
            n=ingreso()
        elif n == "16":
            descripcion.orientacion_img()
            n=ingreso()
        elif n == "17":
            descripcion2.boundin_centr_llaves()
            n=ingreso()
        elif n == "18":
            clasificacion.main()
        else:
            break



aplicativo()