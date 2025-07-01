def print_comb(invertido=False):
    """Esta función imprime todos los números de tres cifras sin repetir los números
    en las centenas, decenas y unidades... 
    adicionalmente no repite numeros que ya se hayan hecho en otra secuencia de números de forma asecendente y descendente"""
    combinaciones = [] # se crea lista de combinaciones en blanco, para guardar los valores
    for c in range(10): # itera de 0 a 9
        for d in range(c + 1, 10): # toma el valor de las centenas y le agrega uno para no repetir el número e itera desde ese valor hasta 9
            for u in range(d + 1, 10): # toma el valor de las decenas y le agrega uno para no repetir el número e itera desde ese valor hasta 9
                combinaciones.append(f"{c}{d}{u}") # agrega el valor de cada digito en la lista como string

    if invertido == False: # la peticion no es vivertida
        print(", ".join(combinaciones)) # imprime cada valor de la lista "combinaciones" adiriendole una como y espacio al final
    else: # de lo contrario
        combinaciones_inv =[] # se crea lista de combinaciones en blanco, para guardar los valores de forma invertida
        space = len(combinaciones) # contamos la cantidad de espacios en la lista
        for inv in range(space - 1, -1, -1): # iteramos de forma invertida tomando el ultimo valor y diregiendo hasta la primer espacio de la lista, restandole uno en uno 
            combinaciones_inv.append(combinaciones[inv]) # agregamos a la lista de combinaciones invertidas cada iteración
        print(", ".join(combinaciones_inv)) # imprime cada valor de la lista "combinaciones" adiriendole una como y espacio al final
              

def main():
    
    while True: # ciclo perpetuo
        invertido = input("¿Quieres ver las combinaciones en orden invertido? (s/n): ").upper().strip() # peticion de orden a imprimir
    
        if invertido == "S": # si es invertido
            invertido = False # será false
            return print_comb(invertido) # retornará la funcion a imprimir con el booleano determinado
        elif invertido == "N": # si es normal
            invertido = True # será true
            return print_comb(invertido) # retornará la funcion a imprimir con el booleano determinado
        else: # si no hay considencias 
            print("el valor debe ser <s/n>") # imprime que erl valor no es correcto 
        continue # vuelve al ciclo perpetuo

        

if __name__ == "__main__":
    main()
