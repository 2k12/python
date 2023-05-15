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
