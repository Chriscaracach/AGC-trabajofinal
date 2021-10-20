import csv

def escribir_juego(matriz, diccionario, nombre):
    #nombre del archivo
    nombre_del_archivo = nombre + ".csv"

    archivo = open(nombre_del_archivo, 'w')
    with archivo:
        writer = csv.writer(archivo)
        for lista in matriz:
            writer.writerow(lista)
        
    
    #Hasta acá llegué
    nombre_del_archivo_solucion = nombre + "_solucion.csv"

    solucion = open(nombre_del_archivo_solucion, 'w')
    with solucion:
        titulos = ["palabra", "x_inicial", "x_final", "y_inicial", "y_final"]
        writer = csv.DictWriter(solucion, titulos)
        writer.writeheader()
        dictValues = diccionario.values()
        dictKeys = diccionario.keys()
        for item in dictValues:
            writer.writerow(item)





listaListas = [["a", "b", "c"],["d","e","f"],["g","h","i"]]
diccionarioPalabras = {"casa": {"x_inicial": 0, "x_final": 3, "y_inicial": 0, "y_final": 0}, "perro": {"x_inicial": 1, "x_final": 5, "y_inicial": 1, "y_final": 1}}
nombreArchivo = "nombreArchivoPrueba"



print(escribir_juego(listaListas, diccionarioPalabras, nombreArchivo))