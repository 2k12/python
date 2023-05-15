from math import *
#Escribe un programa que calcule la suma de dos números ingresados por el usuario.

def ejerciciosbasicos1():
    n1=input("ingrese primer numero")
    n2=input("ingrese segundo numero")
    res = int(n1)+int(n2)
    print(f" La suma es {res}")

#ejerciciosbasicos1()


def ejerciciosbasicos2():
    for numero in range(1, 101):
        if numero % 3 == 0:
            numero = "Fizz"
        elif numero % 5 == 0:
            numero = "Buzz"
        elif numero % 3 == 0 and numero % 5 == 0:
            numero = "Fizz_Buzz"
        print(numero)


#ejerciciosbasicos2()


def ordeninversodepalabras():
    palabra = input("Ingrese una palabra: --> ")
    aux =""
    aux1 =""

    for letra in palabra:
        if letra != " ":
            aux = letra+aux
        elif letra == " ":
            letra=""
            aux = letra+aux

    print(aux)

#ordeninversodepalabras()

def factorial():
    ni=input("Ingrese el numero para calcular su factorial: ")
    n=int(ni)+1
    aux=0
    res=1
    for i in range(1,n):
        aux= i
        res*=aux

    print(f"El factorial de {ni}! -> {res} ")


#factorial()


def suma_promedio_desviacionestandar():
    salir=" "
    valor=0
    lista = []
    aux=0
    res=0
    iterador=0

    #variables para la desviacion
    u = 0
    distancia = []
    sumatoria=0

    print("ingrese una lista de numeros y luego ingrese la palabra calcular!: ")
    while salir ==" ":
        valor = input("numeros: ")
        if valor== "calcular":
            salir == valor
            break
        else:
            lista.append(int(valor))
            iterador += 1

    for n in lista:
        aux = int(n)
        res += aux     

    u = res/iterador  

    for  n in lista:
        distancia.append(pow(n-u,2))

    for nl in distancia:
        aux2 = nl 
        sumatoria += aux2
    

    print (f"LA SUMA ES: {res} || EL PROMEDIO ES: {u} || LA DESVIACION ES: { sqrt(sumatoria/iterador) }")


#suma_promedio_desviacionestandar()

def primos():
    
    n=int(input("Ingrese un numero: "))
    contador=0
    res = ""
    while n == 1:
        n=int(input("Ingrese un numero distinto de -> 1: "))

    for x in range(2,100000):
        if  n % x == 0:
            contador+=1
            if contador <= 2:
                res = "primo"
            else:
                res= "no primo"
    print(f"numero {n} es {res} ")


#primos()
