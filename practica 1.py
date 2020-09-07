#punto 1
print(type(4<2))

#punto 2
nombre = input("ingrese su nombre: ")
print("bienvenido : " + nombre)

#punto3
numero = input("ingrese su numero : ")
operacion = int(numero) % 2
if operacion == 0 :
    print(numero + " es par")
else:
    print(numero + " es impar")
#punto 4
a = 6
b = 4
if a > b :
    print("su resultado es verdadero")
else:
    print("su resultado es falso")

#punto 5
dolares = input("igrese la cantidad de dolares : ")
dolares = float(dolares)
valor = 58.45
print(dolares * valor)

#punto 6
celsius = input("ingrese su grado celsius : ")
celsius = float(celsius)
fahrenheit = 9/5
print(celsius * fahrenheit + 32)

#punto 7
nota1 = 90
nota2 = 95
nota3 = 77
nota4 = 92
sumatoria = nota1 + nota2 + nota3 + nota4
promedio = sumatoria / 4

if promedio <= 60:
    print("calificacion : F")
elif promedio <= 70:
    print("calificacion : D")
elif promedio <= 80:
    print("calificacion : c")
elif promedio <= 90:
    print("calificacion : B")
else:
    print("calificacion : A")

#punto 8
monto = input("igrese el monto: ")
monto = float(monto)
cuotas = input("igrese cantidad de cuota :")
cuotas = int(cuotas)
interes = input("ingrese el porcetaje del interes : ")
interes = float(interes)
ic_1 = (1+ interes) ** cuotas
ic_2 = ( interes * ic_1) / (ic_1 - 1)
resultado = monto * ic_2
print(resultado)