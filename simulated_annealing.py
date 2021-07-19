from random import random as rd
from math import e
def optimizar(dominio, temp = 10e3, tasa_enfriamiento = 0.95,testeo=False):

    """Algoritmo de optimización estocástica simulated annealing.

    Entradas:
    dominio (Dominio)
        Un objeto que modela el dominio del problema que se quiere aproximar.

    temp (float/int)
        Temperatura inicial del algoritmo, se recomienda un número alto

    tasa_enfriamiento (float)
        Porcentaje de enfriamiento de la temperatura durante cada iteración, el valor
        por defecto es 0.95, lo que indica una tasa de enfriamiento del 5%.

    testeo (Boolean)
        Si el algoritmo se utiliza para testeo y que retorne valores adicionales
        para analizar datos se debe setear en True (por defecto es False)

    Salidas:
        (estructura de datos) Estructura de datos según el dominio, que representa una
        aproximación a la mejor solución al problema.
    """
    sol = dominio.generar()
    costo = dominio.fcosto(sol)
    if testeo:
        sol_inicial = sol.copy()
        datos = {"Solucion inicial":sol_inicial,"Fitness(costo ruta)":[costo],"Iteraciones":[0]}
        iteracion = 1
    
    while temp > 0.01:
        vec_sol = dominio.vecino(sol)
        
        vec_costo = dominio.fcosto(vec_sol)
        
        exp = -abs(vec_costo-costo)/temp

        prob = pow(e,exp)
        prob_azar = rd() 
        if vec_costo < costo or prob >= prob_azar:
            sol = vec_sol
            costo = vec_costo
        temp *= tasa_enfriamiento

        if testeo:
            datos["Fitness(costo ruta)"].append(costo)
            datos["Iteraciones"].append(iteracion)
            iteracion +=1
    if testeo:
        return sol,datos
    return sol

