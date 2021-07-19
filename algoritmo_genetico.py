import random
import math


def optimizar(dominio, tam_pobl, porc_elite, prob_mut, reps,testeo):
    """Algoritmo genético para optimización estocástica.

    Entradas:
    dominio (DominioAG)
        Un objeto que modela el dominio del problema que se quiere aproximar.
    
    tam_pobl (int)
        Tamaño de la población.
    
    porc_elite (float)
        Porcentaje de la población que se tomará como elite.
    
    prob_mut (float)
        Probabilidad de mutación, debe estar en el rango [0, 1]
    
    reps (int)
        Número de iteraciones a ejecutar.

    Salidas:
        (estructura de datos) Estructura de datos según el dominio, que representa una
        aproximación a la mejor solución al problema.
    """

    poblacion = dominio.generar_n(tam_pobl)
    costo = dominio.fcosto(poblacion[0])

    if testeo:
        datos = {"Fitness(costo ruta)":[costo],"Iteraciones":[0]}
        iteracion = 1
    

    for iterador_genetico in range(0, reps):
        nueva_poblacion = seleccion_poblacion(dominio, poblacion, math.ceil(tam_pobl * porc_elite))



        del poblacion[:]

        for iterator in range(0, tam_pobl):
            indice_padre_1 = random.randint(0, len(nueva_poblacion)-1)
            indice_padre_2 = random.randint(0, len(nueva_poblacion)-1)
            valor_mutacion = random.uniform(0, 1)
            hijo = dominio.cruzar(nueva_poblacion[indice_padre_1], nueva_poblacion[indice_padre_2])
            if valor_mutacion < prob_mut:
                hijo = dominio.mutar(hijo)
                poblacion.append(hijo)
            else:
                poblacion.append(hijo)     
        if testeo:
            ordena_poblacion(dominio,poblacion)#Implementacion de quicksort para ordenar de menor a mayor en costo
            costo = dominio.fcosto(poblacion[0])   
            datos["Fitness(costo ruta)"].append(costo)
            datos["Iteraciones"].append(iteracion)
            iteracion +=1
            
    if testeo:
        return poblacion[0],datos

    ordena_poblacion(dominio,poblacion)                     
    return poblacion[0]


def seleccion_poblacion(dominio, poblacion, tamaño_elite):
    nueva_poblacion = []

    for iterador in range(0, tamaño_elite):
        indice_posible_padre_1 = random.randint(0, len(poblacion)-1)
        indice_posible_padre_2 = random.randint(0, len(poblacion)-1)
        posible_padre_1 = dominio.fcosto(poblacion[indice_posible_padre_1])
        posible_padre_2 = dominio.fcosto(poblacion[indice_posible_padre_2])
        if (posible_padre_1 <= posible_padre_2):
            nueva_poblacion.append(poblacion[indice_posible_padre_1])
        else:
            nueva_poblacion.append(poblacion[indice_posible_padre_2])

    return nueva_poblacion


def ordena_poblacion(dominio,poblacion):
    quicksortOP(dominio,0,len(poblacion)-1,poblacion)


def exchange(i,j,arr):
    temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;

def quicksortOP(dominio,low,high,arr):
    i , j = low , high
    pivot = dominio.fcosto(arr[(int)(low + (high-low)/2)])
    while (i <= j):
        while (dominio.fcosto(arr[i]) < pivot):
            i+=1
        while (dominio.fcosto(arr[j]) > pivot):
            j-=1;

        if (i <= j):
            exchange(i, j, arr)
            i+=1
            j-=1
    if (low < j): #recursion
        quicksortOP(dominio,low, j,arr)
    if (i < high):
        quicksortOP(dominio,i, high,arr)

