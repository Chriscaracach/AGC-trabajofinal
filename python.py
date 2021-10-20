# #Funcion para generar letras random
import random

# def textoRandom(texto):
#     resultado = ""
#     for letra in texto:
#         if(letra == " "):
#             resultado = resultado + " "
#         else:
#             resultado = resultado + random.choice("abcdefghijklmnopqrstuvwxyz")

#     return resultado

# print(textoRandom("Hola que tal"))




#print(random.choice("abcdefghijklmnopqrstuvwxyz"))

#Recursion
# def buscar(lista, n):
#     i = 0
#     for elemento in lista:
#         if(elemento == n):
#             return i
#             i += 1
#     return None

# print("buscar 1")
# print(buscar([1,4,3,2,5,4,4,4], 6))


# def buscar2(lista, n, i=0):
#     if lista[i] == n:
#         return i
#     return buscar2(lista, n, i+1)

# print("buscar2")
# print(buscar2([1,4,3,2,5,4,4,4], 6))

#Factorial


# def fibonacciNormal(n):

#     contador = 2
#     fib = 1
#     seq = [1,1]
#     punteroMenosDos = len(seq)-2
#     punteroMenosUno = len(seq)-1
#     while(contador<n):
#         seq.append(punteroMenosDos + punteroMenosUno)
#         contador +=1
#     return seq[punteroMenosUno]


# print(fibonacciNormal(5))



#Clase bicicleta

# class Bicicleta:
#     def __init__(self, ruedas, color, velocidadActual):
#         self.ruedas = ruedas
#         self.color = color
#         self.velocidadActual = velocidadActual

#     def aumentarVelocidad(self):
#         if(velocidadActual < 80):
#             self.velocidadActual *= 1
#         else:
#             print("velocidad máxima alcanzada")

#     def reducirVelocidad(self):
#         if(velocidadActual >0):
#             self.velocidadActual -= 1
#         else: 
#             print("Velocidad mínima alcanzada")

#     def __str__(self):
#         print("Hola, soy un mensaje amigable. La cantidad de ruedas es " + self.ruedas + " y la velocidad actual es " + self.velocidadActual + ".")

#     def eq(self, otraBici):
#         if(self.ruedas == otraBici.ruedas and self.color == otraBici.color):
#             print("Las bicis son iguales.")
#         else:
#             print("Las bicis NO son iguales.")

#     def multiplicar(self):
#         biciNueva = Bicicleta(self.ruedas * 2, "rojo")
#         return biciNueva


# class Animal:
#     def __init__(self):
#         self.energia = 10

#     def caminar(self):
        



#Carrera de vehículos

class Vehiculo:
    def __init__(self):
        self.posicion = 1
        
    def tirarDado(self):
        dado = random.randint(1, 6)
        self.posicion = self.posicion + dado
        info = [dado, self.posicion]

        return info

class Auto(Vehiculo):
    def __init__(self):
        super().__init__()

class Moto(Vehiculo):
    def __init__(self):
        super().__init__()


def carrera():
    auto = Auto()
    moto = Moto()

    print("Bienvenidos a la carrera")
    print("En ésta carrera están corriendo un auto vs una moto")
    print("Apretá ENTER para hacer avanzar los vehículos. El primero que llega a 100, gana")
    mayorPosicion = 1
    while(mayorPosicion<100):
        enter = input()
        infoAuto = auto.tirarDado()
        infoMoto = moto.tirarDado()
        print("Movimiento del auto. " + str(infoAuto[0]) + " lugares. La nueva posición es " + str(infoAuto[1]))
        if(infoAuto[1] >= 100):
            print("El auto llegó a la posición 100. Ganó el juego!!")
            quit()
        print("Movimiento del moto. " + str(infoMoto[0]) + " lugares. La nueva posición es " + str(infoMoto[1]))
        if(infoMoto[1] >= 100):
            print("La moto llegó a la posición 100. Ganó el juego!!")
            quit()


print(carrera())

def crearCorredor():
    print("Ingresá el nombre del corredor/a: ")
    nombre = input()
    print("Ingresá el color del vehículo: ")
    color = input()
    print("Ingresá el número del vehículo: ")
    numero = input()
    print("Si querés que tu vehículo sea una moto, escribi 'moto'. Si querés que sea un auto, escribí 'auto':")
    tipo = input()
    if(tipo == "moto"):
        corredor = Moto(color, numero, nombre)
        print(corredor.creacion())
        corredores.append(corredor)
    else:
        corredor = Auto(color, numero, nombre)
        print(corredor.creacion())
        corredores.append(corredor)





# def carrera():
#     print("Bienvenidos a la carrera")








# print(crearCorredor())


# class Util:
#     def __init__(self, grosor, color):
#         self.grosor = grosor
#         self.tinta = 100

#     def escribir(self):
#         self.tinta -= 1

    
# class Cartuchera:
#     def __init__(self):
#         self.espacio = 10

    


