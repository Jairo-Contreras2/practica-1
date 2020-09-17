#punto 1
numero = 1
cantidad = 0
suma = 0
while numero != 0:
    numero = int(input("ingrese los numeros: "))
    if numero != 0:
        suma = suma + numero
        cantidad = cantidad + 1
      
print("usted ingreso " + str(cantidad) + " y la suma es = " + str(suma))


#punto 2
def menu():
    print("bienvenido por favor selecione una de la siguientes opciones")
    print("1- convertir de grados celsius a fahrenheit")
    print("2- convertir dolar a pesos")
    print("3- convertir metros a pies")
    print("4- salir")


menu()
seleccione = input("> ")
seleccione = int(seleccione)


while seleccione != 4:
    if seleccione == 1:
        celsius = input("ingrese su temperatura en grados celsius: ")
        celsius = float(celsius)
        res = celsius * 9/5 + 32
        print (str(res) + "grados fahrenheit")

        menu()
        seleccione = input("> ")
        seleccione = int(seleccione)
    elif seleccione == 2:
        dolares = input("ingrese la cantidad de dolares: ")
        dolares = float(dolares)
        valor_de_dolar = 58.52
        pesos = dolares * valor_de_dolar
        print(str(dolares) + "$us equivale a " + str(pesos) + "$RD")

        menu()
        seleccione = input("> ")
        seleccione = int(seleccione)
    elif seleccione == 3:
        metros = input("ingrese la cantidad de metros: ")
        metros = float(metros)
        factor = 3.28
        pies = metros * factor
        print(metros, "m =", pies, "pies")

        menu()
        seleccione  = input("> ")
        seleccione = int(seleccione)
    elif seleccione >= 4:
        print("la opcion seleccionada nose encuentra en el menu")
        print("por favor, selecciones una de las siguentes opciones")

        menu()
        seleccione = input("> ")
        seleccione = int(seleccione)
    if seleccione == 4:
        print("gracias espero que le aya gustado")

#punto 3
n = 5
c = 1

while c <=200:
    print(int(n) * c)
    c = c + 1

#punto 4
sueldo = input("Ingrese su sueldo: ")
sueldo = float(sueldo)
sueldo_anual = sueldo * 12
r_1 = 416220.00 #15%
r_2 = 624329.00 #20%
r_3 = 867123.00 #25%
ars = 0.0304
afp = 0.0287

def cal_1():
  ARS = sueldo_anual * ars
  AFP = sueldo_anual * afp
  print ("Usted paga ", ARS, " de ARS anualmente")
  print ("Usted paga ", AFP, " de AFP anualmente")


if sueldo_anual <= r_1:

  print("Usted esta exento del ISR")
  cal_1()

elif sueldo_anual <= r_2:
  calculo_r2 = sueldo_anual * 0.15
  print ("Usted paga ", calculo_r2, " de IRS")
  cal_1()

elif sueldo_anual <= r_3:
  calculo_r3 = (sueldo_anual * 0.20) + 31216.00
  print ("Usted paga ", calculo_r3, " de IRS")
  cal_1()

else:
  calculo_r4 = (sueldo_anual * 0.25) + 79776.00
  print ("Usted paga ", calculo_r4, " de IRS")
  cal_1()
  
  #punto 5
b1000 = 9
b500 = 19
b100 =  99

def retiro(monto):
       global b1000, b500, b100
       d1 = int(monto / 1000) #Se verifica si se pueden sacar billetes de 1000 y se obtiene la cantidad de billetes que se dispensaran
       monto = monto % 1000 # se obtiene el residuo de la division y se guarda en monto para el proximo billete
       if d1 >= b1000:
         monto = monto + (d1 - b1000) * 1000
         d1 = b1000
       d2 = int(monto / 500)
       monto = monto % 500
       if d2 >= b500:
         monto = monto + (d2 - b500) * 500
         d2 = b500
       d3 = int(monto / 100)
       monto = monto % 100  
       if d3 >= b100:
         monto = monto + (d3 - b100) * 100
         d3 = b100
       return [d1, d2, d3]


print ("Bienvenido al cajero ABC, por favor elegir el banco para su Transacción:  ")
print ("1. Banco ABC")
print ("2. Otros ")
select = input("> ")
select = int(select)


if select == 1:
  c = int(input("Ingrese el monto a retirar: "))
  if c <= 10000:
      res = retiro(c)
      print("Billetes de 1000: " , res[0])
      print("Billetes de 500: ", res[1])
      print("Billetes de 100: ", res[2]) 
  if c == 0:
      print ("Retiro nulo")
  if c >= 10000:
      print("El monto deseado excede el limite") 
  

if select == 2:
  c = int(input("Ingrese el monto a retirar: "))
  if c <= 2000:
      res = retiro(c)
      print("Billetes de 1000: " , res[0])
      print("Billetes de 500: ", res[1])
      print("Billetes de 100: ", res[2]) 
  if c == 0:
      print ("Retiro nulo")
  if c >= 2000:
      print("El monto deseado excede el limite")   
