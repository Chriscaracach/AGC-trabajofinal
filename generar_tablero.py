import random

def generar_tablero(n, listaPalabras):
    contador = 0 #Sirve para el while linea 7
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
            "y_inicialfinal" : y #en la ubicación horizontal y es solo un número
        }
        return ubicacion

    def generarUbicacionAleatoriaVertical(y_inicial, x, pal):
        ubicacion = {
            "y_inicial": y_inicial, #idem funcion anterior
            "y_final": int(y_inicial) + len(pal)-1,
            "x_inicialfinal" : x
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
                if(insertarPalabraHorizontal(palabra, int(ubicacion["x_inicial"]), int(ubicacion["y_inicialfinal"])) == False):
                    generarTableroEnBlanco() #si la funcion devuelve False, blanqueo el Tablero
                    #No se si ésto está funcionando
                else:
                    cargaExitosa = True

        else: #vertical
            # print("vertical")
            cargaExitosa = False
            while(cargaExitosa == False):
                #Genero ubicación aleatoria
                ubicacion = generarUbicacionAleatoriaVertical(random.choice(microContadorRandom), random.choice(contadorRandom), palabra)
                #inserto palabra
                if(insertarPalabraVertical(palabra, int(ubicacion["y_inicial"]), int(ubicacion["x_inicialfinal"])) == False):
                    generarTableroEnBlanco()
                else:
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

    #imprimo el tablero para verlo
    for lista in tablero:
        print(*lista, sep="|")

    return tablero
