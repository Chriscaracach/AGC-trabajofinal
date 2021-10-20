def pedir_datos_tablero():
    #cantidad de columnas y filas
    numeroValido = False
    while(numeroValido == False):
        try:
            N = int(input("Ingrese un número para la cantidad de filas y columnas: "))
        except ValueError:
            print("La opción que ingreso no es un numero")
        else:
            print("El numero es válido")
            numeroValido = True
        
    #lista de palabras
    lista = []
    palabras_posibles = int(N/3)
    print("Ahora ingresá las palabras- Podés ingresar hasta " + str(palabras_posibles) + " palabras.")
    print("Y recordá que la longitud de la palabra tiene que ser menor a " + str(N) + ".")
    print("Para finalizar la carga escribí fin")
    palabra = ""
    while(len(lista) < palabras_posibles and palabra != "fin"):
        palabra = input("Palabra: ")
        if(palabra.isalpha() and palabra not in lista):
            lista.append(palabra)
            print("Palabra guardada")
        else:
            print("La palabra que ingresaste ya existe en la lista o contiene caracteres no válidos, ingrese de nuevo")
            
    #nombre del archivo
    print("Ahora ingresá el nombre del archivo. Tiene que tener un máximo de 30 caracteres")
    nombreValido = False
    while (nombreValido == False):
        nombre = input("Nombre: ")
        if(nombre.isalnum() and len(nombre) <= 30):
                nombreValido = True
        else:
            print("El nombre que ingresaste contiene caracteres no válidos. Por favor intentalo nuevamente")
    return (N, lista, nombre)


print(pedir_datos_tablero())

