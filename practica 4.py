#punto 1
class celular:
    def __int__(self): 
        self.marca = "iphone"
        self.modelo = "xs" 
        self.año = 2019 
        self.bateria = 100

class laptop:
    def __int__(self):
        self.marca = "lenovo"
        self.modelo = "ideapad"
        self.mause = "touch pad"
        self.entradas_usb = 3

class silla:
    def __int__(self):
        self.forma = "cuadrada"
        self.patas = 4
        self.color = "marron"
        self.materia = "madera"

#punto 2
class estudiante:
    promedio = 0

    def __init__(self, promedio):
        self.promedio = promedio

    def valor_del_promedio(self):
        grado = []
        x = 0
        self.promedio = 0
        sum = 0
        while x < 4:
            grados = int(input("escriba la nota: "))
            x += 1
            grado.append(grados)
            for i in grado:
                sum += i
                self.promedio += 1
        promedio = sum / self.promedio
        if promedio > 100:
            print("promedio no valido")
        print("tu promedio es: ",promedio)

#punto 3
class Aritmetica:

    def suma(self, a, b):
        return a + b

    def resta(self, a, b):
        return a - b

    def multiplicacion(self, a, b):
        return a * b

    def divicion(self, a, b):
        return a / b
    
#punto 4
class personaje:
    def mover_arriba(self):
        pass

    def mover_abajo(self):
        pass

    def mover_derecha(self):
        pass

    def mover_izquierda(self):
        pass

class Mario(personaje):
    personaje = personaje()
    personaje.mover_arriba()
    personaje.mover_abajo()
    personaje.mover_derecha()
    personaje.mover_izquierda()


class Koopa(personaje):
    personaje = personaje()
    personaje.mover_arriba()
    personaje.mover_abajo()
    personaje.mover_derecha()
    personaje.mover_izquierda()

#punto 5
class Carro:
    def __init__(self):

        self.cantidad_combustible = 12
        self.acelerador = 6
        self.motor = "apagado"
        


    def Encender(self):
        if self.motor == "apagado":
            self.motor = int(input("Ingrese 7 para encender el motor: "))
            if self.motor == 7:
                print("Motor encendido")
                if self.motor == 7:
                    self.acelerador = int(input("ingrese 6 para acelerar: "))
                    while self.acelerador == 6:
                        while self.cantidad_combustible > 0:
                            print("Pisando acelerador.")
                            print("Acelerando")
                            self.cantidad_combustible = self.cantidad_combustible - 1
                            print(f"El combustible va por:{self.cantidad_combustible} Galones.")
                            self.acelerador = int(input("para dejar de acelerar presione 8: " ))
                            while self.acelerador == 8:
                                print("Usted a dejado de acelerar.")
                                self.acelerador = int(input("ingrese 6 para acelerar: "))
                        
                                while self.cantidad_combustible < 1:

                                    print("galones de combustible insuficientes para acelerar")
                                    self.cantidad_combustible = int(input("Ingrese 12 para rellenar los galones: "))
                                    self.acelerador = int(input("ingrese 6 para acelerar: "))

Lamborghini = Carro()
Lamborghini.Encender()

