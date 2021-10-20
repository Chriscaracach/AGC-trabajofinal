def pedir_dato(texto, textoError, fn):
    print(texto)
    dato = input()
    if(fn(dato)):
        return dato
    else:
        print(textoError)
        print(pedir_dato(texto, textoError, fn))



