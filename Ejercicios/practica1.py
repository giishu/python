#! /usr/bin/python

# 1ra Practica Laboratorio 
# Teoria de Grafos
# Consigna: Implementar los siguientes metodos

import sys

def lee_grafo_stdin(grafo):
    """
    Recibe como argumento un grafo representado como una lista de tipo:
       ['3', 'A', 'B', 'C', 'A B', 'B C', 'C B']
    Devuelve:
        (['A','B','C'],[('A','B'),('B','C'),('C','B')])
    """
    cantidad_vertices = int(grafo[0])
    vertices = grafo[1:1 + cantidad_vertices]
    aristas = []

    for linea in grafo[1 + cantidad_vertices:]:
        origen, destino = linea.split()
        aristas.append((origen, destino))

    return (vertices, aristas)

    pass

def lee_grafo_archivo(file_path):
    '''
    Lee un grafo desde un archivo y devuelve su representacion como lista.
    Ejemplo Entrada: 
        3
        A
        B
        C
        A B
        B C
        C B
    Ejemplo retorno: 
        (['A','B','C'],[('A','B'),('B','C'),('C','B')])
    '''

    with open(file_path, 'r') as file:
        lines = file.readlines()
        grafo = [line.strip() for line in lines if line.strip()]
    
    return lee_grafo_stdin(grafo)    

    pass

def imprime_grafo_lista(grafo):
    '''
    Muestra por pantalla un grafo. El argumento esta en formato de lista.
    '''

    vertices, aristas = grafo
    print("Vertices:", vertices)
    print("Aristas:")
    for origen, destino in aristas:
        print(f"{origen} - {destino}")

    pass

#################### FIN EJERCICIO PRACTICA ####################
def lee_entrada_1():
    '''
    Lee un grafo desde entrada estandar y devuelve su representacion como lista.
    Ejemplo Entrada: 
        3
        A
        B
        C
        A B
        B C
        C B
    Ejemplo retorno: 
        ['3', 'A', 'B', 'C', 'A B', 'B C', 'C B']
    '''
    data_input = []
    
    for line in sys.stdin:
        if line == '\n':
            break
        else:
            # Con strip() eliminamos los '\n' del final de c/line
            data_input.append(line.strip())
            
    return data_input

    
def lee_entrada_2():
    lineas = []
    try:
        while True:
            linea = input().strip()
            if not linea:
                break
            lineas.append(linea)
            print(f'Línea leída: [{linea}]') 
    except EOFError:
        pass
    print(f'Total líneas leídas: {len(lineas)}')
    return lineas

def mostrar_saludo():
    print("Hola mundo")
