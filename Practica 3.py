#punto 1
print("bienvenido al calculador de potencicas")

x = int(input("ingrese el valor de la base (x): "))
y = int(input("ingrese el valor de la potensia (y): "))

def potencia():
    resultado = x ** y
    print (f"{x}^{y} = {resultado}")

potencia()

#punto 2
numero = int(input("igrese un numero del uno al diez : > "))


def escrito():

    if numero == 1:
        print("uno")
    elif numero == 2:
        print("dos")
    elif numero == 3:
        print("tres")
    elif numero == 4:
        print("cuatro")
    elif numero == 5:
        print("cinco")
    elif numero == 6:
        print("seis")
    elif numero == 7:
        print("siete")
    elif numero == 8:
        print("ocho")
    elif numero == 9:
        print("nueve")
    elif numero == 10:
        print("diez")
    else:
        print("este numero no esta disponible")

escrito()

#practica 3
x= int(input("ingrese un año: "))


def bisiesto(año):
  res = año % 4
  if res == 0 :
    print(f"{año} Este año es bisiesto")
  else:
    print(f"{año} Este año no es bisiesto")

bisiesto(x)

#punto 4
n1 = input("Ingrese el primer numero: ")
n1 = float(n1)
n2 = input("Ingrese el segundo numero: ")
n2 = float(n2)

def igualdad():
    return n1 == n2

res = igualdad()
print(res)

#punto 5
def isPalindrome(numero):
    if str(numero) == str(numero)[::-1]:
        return True
    else:
        return False
max_Palindrome=1
for numero1 in range(100,999):
    for numero2 in range(100,999):
        producto = numero1 * numero2  
        if isPalindrome(producto):
            if producto > max_Palindrome:
                max_Palindrome = producto
                max_num1 = numero1
                max_num2 = numero2
print (max_Palindrome,max_num1,max_num2)

#punto 6
cedu = input("digite su numero de cedula : ")

def validacion(cedula):
    if len(cedula) == 11:
        print("cedula valida")
        return True
    else:
        print("cedula invalida")

validacion(cedu)

#punto 7
print("ingrese numero al listado: ")
x = int(input("> "))
y = int(input("> "))
z = int(input("> "))


def duplicar(a,b,c):

    return [a*2, b*2, c*2]

res = duplicar(x,y,z)
print(res)
 
#punto 8
n1 = int(input("igrese el primer numero : "))
n2 = int(input("ingrese el numero final que sea mayor al primero : "))

def dp(a,b):
    while a <= b:
        res = 6 * a
        print(f"{6} X {a} = {res}")
        a += 1
if n1 > n2:
     print(f"{n2} no es mayor que {n1}")   

else:
   dp(n1,n2)