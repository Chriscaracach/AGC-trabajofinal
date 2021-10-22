from pathlib import Path #Para buscar el archivo del tablero
import re #Para la transformación de la palabra en mayúsculas
import time #Para hacer más fachero el programa

class Main:
    def __init__(self):
        self.tablero = []
        self.datosSolucion = []
        self.palabrasSolucion = []
        self.nombreUsuario = ""
        self.nombreTableroAUsar = ""
        self.palabrasEncontradas = []
        self.puntaje = {
            "cantidadPalabrasEncontradas": len(self.palabrasEncontradas),        
            "palabrasEncontradas": self.palabrasEncontradas,
            "palabrasNoEncontradas": self.palabrasSolucion
        }

    def main(self):# Programa principal
        print("Bienvenido/a a la SOPA DE LETRAS")
        #Ingresa nombre de usuario y valida
        while(len(self.nombreUsuario) == 0): 
            nomUsuario = input("Por favor, ingresá tu nombre de usuario: ")
            if(nomUsuario.isalnum()):
                self.nombreUsuario = nomUsuario
                print("Nombre de usuario elegido: " + self.nombreUsuario)
            else:
                print("El nombre de usuario no es válido, por favor ingresalo nuevamente")
       
        tableroExiste = False
        #Validamos que exista el tablero
        while(tableroExiste == False):
            nomTablero = input("Ingresá el nombre del tablero que vas a jugar: ")

            print("Cargando tablero...")
            time.sleep(2)
            if(main.chequearSiTableroExiste(nomTablero)):
                print("Tablero elegido correctamente.")
                self.nombreTableroAUsar = nomTablero
                tableroExiste = True
            else:
                print("El tablero no existe.")
                
        #Se carga el tablero en las variables de la clase
        main.cargarTablero(self.nombreTableroAUsar) 
        #Se cargan las soluciones
        main.cargarSoluciones(self.nombreTableroAUsar)

        deseaTerminarElJuego = False
        #Juego
        while deseaTerminarElJuego == False:
            main.imprimirTablero() #Imprime el tablero
            palabra = input("Ingresá la palabra que encontraste, para cerrar el juego escribí 'fin': ")
            
            if(palabra == "fin"):
                print("Juego terminado")
                main.mostrarPuntajes()
                quit()
            print("Buscando palabra...")
            time.sleep(2)
            if(main.buscarPalabra(palabra)): #se busca que la palabra exista
                print("¡¡¡Palabra encontrada!!!")
                time.sleep(1)
                main.encontrarPalabra(palabra) #Se hacen mayúsculas las letras de la palabra encontrada
                self.palabrasEncontradas.append(palabra) #Se actualizan variables
                self.palabrasSolucion.remove(palabra)
                #Chequeamos cuando encuentre todas las palabras
                if(len(self.palabrasSolucion) == 0):
                    time.sleep(2)
                    print("¡¡¡Encontraste todas las palabras!!!")
                    main.mostrarPuntajes()
                    quit()
            else:
                print("Palabra equivocada, intentalo de nuevo")
                time.sleep(1)
            
    def cargarTablero(self, tab): #Esta función sirve para leer el tablero y transformarlo en variable del juego
        tableroLeido = []
        tableroListo = []
        with open(tab + ".csv") as tablero:
            for linea in tablero:
                tableroLeido.append(linea)
            
            for str in tableroLeido:
                x = str
                x = x.replace("/", "")
                x = x.split(",")
                x[len(x)-1] = x[len(x)-1][0]
                tableroListo.append(x)
            
            self.tablero = tableroListo

    def imprimirTablero(self): #Esta función sirve para imprimir el tablero 
        for lista in self.tablero:
            print(*lista, sep="|")

    def cargarSoluciones(self, sol): #Esta función sirve para cargar las soluciones desde un archivo .csv y transformarlas en variables para el juego
        soluciones = []
        solucionesListas = []
        with open(sol + "-solucion.csv") as archivoSoluciones:
            for linea in archivoSoluciones:
                soluciones.append(linea)
            soluciones.pop(0)
            for str in soluciones:
                x = str
                x = x.split(",")
                a = re.sub("\n", "", x[len(x)-1])
                x[len(x)-1] = a
                #Creamos un formato de datos que nos sirva
                obj = {
                    "palabra" : x[4],
                    "x_inicial": x[0],
                    "x_final": x[1],
                    "y_inicial": x[2],
                    "y_final": x[3]
                }
                #Agregamos los datos que obtenemos a variables independientes
                self.palabrasSolucion.append(x[4])
                self.datosSolucion.append(obj)

    def devolverDatosSolucion(self): #Esta funcion devuelve los datos de las soluciones
        return self.datosSolucion

    def buscarPalabra(self, palabra): #Esta funcion busca entre las palabras correctas a ver si la palabra ingresada está bien
        if palabra not in self.palabrasSolucion:
            return False
        else:
            return True

    def encontrarPalabra(self, palabra): #Esta funcion es la que transforma la palabra encontrada en mayúsucla
        for item in self.datosSolucion:
            if(palabra == item["palabra"]):
                if(item['x_inicial'] == item['x_final']):
                    x = int(item['x_inicial'])
                    cursor = int(item['y_inicial'])
                    while(cursor <= int(item['y_final'])):
                        may = self.tablero[cursor][x].upper()
                        self.tablero[cursor][x] = may
                        cursor += 1
                else:
                    y = int(item['y_inicial'])
                    cursor = int(item['x_inicial'])
                    while(cursor <= int(item['x_final'])):
                        may = self.tablero[y][cursor].upper()
                        self.tablero[y][cursor] = may
                        cursor += 1           
            
    def mostrarPuntajes(self): #Esta funcion muestra los puntajes del usuario, se usa al final
        print("Puntajes de " + self.nombreUsuario)
        print("Tablero: " + self.nombreTableroAUsar)
        print("Palabras encontradas: " + str(self.puntaje["palabrasEncontradas"]))
        print("Palabras faltantes: " + str(self.puntaje["palabrasNoEncontradas"]))
        print("Puntaje total: " + str(len(self.puntaje["palabrasEncontradas"])))
        
    def chequearSiTableroExiste(self, nombreTablero): #Esta funcion busca en la carpeta si el tablero existe
        archivo = Path(nombreTablero + ".csv")
        return archivo.is_file()

### EJECUCIÓN ###
main = Main()
print(main.main())