import random #para generar el tablero
import csv #para escribir archivos
import time #para hacer mas fachero el programa


class Programa:
    def __init__(self):
        programa = 1
    
    def main(self, obtenerDatos, generadorTablero, escritor):
        print("Bienvenido/a al programa para crear tableros de SOPAS DE LETRAS")
        obtenerDatos.obtener_datos_usuario()
        obtenerDatos.obtener_datos_tablero()
        nombreArchivo = obtenerDatos.devolveNombreArchivo()
        nombreSolucion = nombreArchivo + "-solucion"
        print("Generando tablero...")
        generadorTablero.generar(obtenerDatos.devolverN(), obtenerDatos.devolverLista())
        time.sleep(2)
        print("Tablero generado")
        nuevoTablero = generadorTablero.devolverTablero()
        soluciones = generadorTablero.mostrarSolucion()
        print("Generando archivos...")
        escritor.escribir_tablero(nuevoTablero, nombreArchivo)
        escritor.escribir_solucion(nombreSolucion, soluciones)
        time.sleep(2)
        print("Archivos generados")
        print("Tu tablero está listo para jugar, podés jugarlo desde el programa 'sopa de letras'")
        
class Escritor:
    def __init__(self):
      escritor = 1

    def escribir_tablero(self, matriz, nombre):
        nombre_del_archivo = nombre + ".csv"

        archivo = open(nombre_del_archivo, 'w')
        with archivo:
            writer = csv.writer(archivo)
            for lista in matriz:
                writer.writerow(lista)
               
    def escribir_solucion(self, nombre, diccionario):
        nombre_del_archivo_solucion = nombre + ".csv"

        solucion = open(nombre_del_archivo_solucion, 'w')
        with solucion:
            titulos = ["x_inicial", "x_final", "y_inicial", "y_final", "palabra"]
            writer = csv.writer(solucion)
            writer.writerow(titulos)
            for item in diccionario:
                writer.writerow(item.values())

class Obtener_Datos:
    def __init__(self):
        self.nombreUsuario = ""
        # self.tablero = ""
        self.N = 0
        self.lista = []
        self.nombre = ""

    def obtener_datos_usuario(self):
        while(len(self.nombreUsuario) == 0):
            nomUsuario = input("Ingresá tu nombre de usuario: ")
            if(nomUsuario.isalnum()):
                self.nombreUsuario = nomUsuario
                print("Nombre de usuario elegido: " + self.nombreUsuario)
            else:
                print("El nombre de usuario no es válido, por favor ingresalo nuevamente")
        
    def obtener_datos_tablero(self):
        print("Ahora vamos a crear el tablero")
        #Ingresamos cantidad de columnas y filas
        numeroValido = False
        while(numeroValido == False):
            self.N = int(input("Ingrese un número para la cantidad de filas y columnas (máx. 20): "))
            if(self.N < 21):
                print("El numero es válido")
                numeroValido = True
            else:
                print("El numero que ingresaste no es válido.")
            
        #Ingresamos lista de palabras
        self.lista = []
        palabras_posibles = int(self.N/3)
        print("Ahora ingresá las palabras. Podés ingresar hasta " + str(palabras_posibles) + " palabras.")
        print("Y recordá que la longitud de la palabra tiene que ser menor a " + str(self.N) + ".")
        print("Para finalizar la carga escribí fin")
        palabra = ""
        while(len(self.lista) < palabras_posibles and palabra != "fin"):
            palabra = input("Palabra: ")
            if(palabra.isalpha() and palabra not in self.lista):
                self.lista.append(palabra)
                print("Palabra guardada")
            else:
                print("La palabra que ingresaste ya existe en la lista o contiene caracteres no válidos, ingrese de nuevo")
                
        #Ingresamos nombre del archivo
        print("Ahora ingresá el nombre del archivo. Tiene que tener un máximo de 30 caracteres")
        nombreValido = False
        while (nombreValido == False):
            self.nombre = input("Nombre: ")
            if(self.nombre.isalnum() and len(self.nombre) <= 30):
                    nombreValido = True
            else:
                print("El nombre que ingresaste contiene caracteres no válidos. Por favor intentalo nuevamente")
        return (self.N, self.lista, self.nombre)

    def devolverN(self):
        return self.N

    def devolverLista(self):
        return self.lista

    def devolverNombreUsuario(self):
        return self.nombreUsuario

    def devolveNombreArchivo(self):
        return self.nombre

class Generador_Tableros:
    def __init__(self):
        self.tableroCompleto = []
        self.solucion = []
        self.ubicaciones = []

    def generar(self, n, listaPalabras):
        contador = 0 
        tablero = [] #Tablero
        contadorRandom = "" #Sirve para el random, es un string con números
        while(contador < n):
            tablero.append([]) #creo tablero con listas
            contadorRandom = contadorRandom + str(contador) #String de numeros para el random líneas 105 y 117
            contador += 1 #Contador
        #Lleno el tablero de espacios
        for array in tablero:
            for item in range(0, n):
                array.append(" ")

                    
        def generarTableroEnBlanco():
            tablero = [] #el tablero se pone en blanco
            contadorTablero = 0 #para el while
            while(contador < n):
                tablero.append([]) #igual que al principio
                contadorTablero += 1
            for array in tablero:
                for item in range(0, n):
                    array.append(" ")
            
        def generarUbicacionAleatoriaHorizontal(y, x_inicial, pal):
            ubicacion = {
                "x_inicial": x_inicial, # punto en x donde comienza la palabra
                "x_final": int(x_inicial) + len(pal)-1, #punto en x donde termina
                "y_inicial" : y,
                "y_final" : y 
            }
            # print("ubicación generada: ") #debug
            # print(ubicacion)
            return ubicacion

        def generarUbicacionAleatoriaVertical(y_inicial, x, pal):
            ubicacion = {
                "x_inicial" : x,
                "x_final": x,
                "y_inicial": y_inicial, #idem funcion anterior
                "y_final": int(y_inicial) + len(pal)-1
            }
            return ubicacion

        def buscarEnElCursor(x,y): #ésta funcion busca si hay algo en el lugar del tablero que se especifica
            if(tablero[y][x] == " "):
                return True
            else:
                return False

        def insertarPalabraHorizontal(pal, x_inicial, y):
            cursor = x_inicial #uso este cursor para buscar en el tablero
            cursorPalabra = 0 #uso éste cursor para insertar la letra en el tablero
            while(cursorPalabra < len(pal)):
                if(buscarEnElCursor(cursor, y)): #si el lugar está libre
                    tablero[y][cursor] = pal[cursorPalabra] #se inserta la palabra
                    cursor += 1 #aumentan los cursores
                    cursorPalabra += 1
                    # print("letra cargada") #feedback
                else:
                    # print("fallo carga de letra") #feedback
                    return False
            if(cursorPalabra == len(pal)): #cuando el cursor iguala el largo de la palabra, quiere decir que ya se cargó toda la palabra
                # print("palabra cargada")
                return True
            else:
                # print("fallo al cargar palabra") #feedback, no se si ésto está funcionando
                return False

        def insertarPalabraVertical(pal, y_inicial, x): #idem funcion anterior
            cursor = y_inicial
            cursorPalabra = 0
            while (cursorPalabra < len(pal)):
                if(buscarEnElCursor(x, cursor)):
                    tablero[cursor][x] = pal[cursorPalabra]
                    cursor += 1
                    cursorPalabra += 1
                    # print("letra cargada")
                else:
                    # print("fallo carga de letra")
                    return False
            if(cursorPalabra == len(pal)):
                # print("palabra cargada")
                return True
            else:
                # print("fallo al cargar palabra")
                return False

        #Con éste for meto palabras en tablero
        for palabra in listaPalabras: #por cada palabra
            ####AGREGADO PARA OBTENER SOLUCION######
            self.solucion.append(palabra)


            ########################################
            microContadorRandom = "" #string de numeros para el random
            microContador = 0 #para el while
            ub = n-len(palabra) # ubicación posible de acuerdo al tamaño del tablero y de la palabra
            while(microContador<=ub):
                microContadorRandom = microContadorRandom + str(microContador) #llenamos el micro contador para el random, string con numeros
                microContador += 1
            
            if(random.choice("ab") == "a"): #a o b para ver si la carga es horizontal o vertical
                # print("horizontal") #feedback
                cargaExitosa = False #con ésta variable corroboro que la carga haya sido exitosa
                while(cargaExitosa == False): #mientras la carga no sea exitosa
                    #Genero ubicación aleatoria
                    ubicacion = generarUbicacionAleatoriaHorizontal(random.choice(contadorRandom), random.choice(microContadorRandom), palabra)
                    #Inserto la palabra
                    if(insertarPalabraHorizontal(palabra, int(ubicacion["x_inicial"]), int(ubicacion["y_inicial"])) == False):
                        generarTableroEnBlanco() #si la funcion devuelve False, blanqueo el Tablero
                        #No se si ésto está funcionando
                    else:
                        self.ubicaciones.append(ubicacion)
                        cargaExitosa = True

            else: #vertical
                # print("vertical")
                cargaExitosa = False
                while(cargaExitosa == False):
                    #Genero ubicación aleatoria
                    ubicacion = generarUbicacionAleatoriaVertical(random.choice(microContadorRandom), random.choice(contadorRandom), palabra)
                    #inserto palabra
                    if(insertarPalabraVertical(palabra, int(ubicacion["y_inicial"]), int(ubicacion["x_inicial"])) == False):
                        generarTableroEnBlanco()
                    else:
                        self.ubicaciones.append(ubicacion)
                        cargaExitosa = True

        #Con éste for, recorro todos los lugares de la matriz, si están vacíos, los lleno con letras random
        for array in tablero:
            contador = 0
            while(contador < len(array)):
                if(array[contador] == " "):
                    array[contador] = random.choice("qwertyuiopasdfghjklzxcvbnm")
                    contador += 1
                else:
                    contador += 1

        self.tableroCompleto = tablero
        
    def imprimirTablero(self, tablero):
        for lista in tablero:
            print(*lista, sep="|")

    def mostrarSolucion(self):
        datosSolucion = []
        for item in self.ubicaciones:
            datosSolucion.append(item)  
        contador = 0
        for item in datosSolucion:
            item["palabra"] = self.solucion[contador]
            contador +=1
        return datosSolucion

    def devolverTablero(self):
        return self.tableroCompleto

### EJECUCION ###

datos = Obtener_Datos()
escritor = Escritor()
generador = Generador_Tableros()
main = Programa()

print(main.main(datos, generador, escritor))