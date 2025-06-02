def cuenta_grado(grafo_lista):
    '''
    Muestra por pantalla los grados de los vertices de un grafo. 
    El argumento esta en formato de lista.
    
    Ejemplo Entrada: 
        (['A','B','C'],[('A','B'),('B','C'),('C','B')])
    Ejemplo retorno: 
        {'A': 1, 'B': 3, 'C': 2}
    '''

    vertices, aristas = grafo_lista
    grados = {v: 0 for v in vertices}  

    for origen, destino in aristas:
        grados[origen] += 1 
        grados[destino] += 1 

    print(grados)
    return grados

    pass

def vertice_aislado(grafo_lista):
    '''
    Dado un grafo en representacion de lista, obtiene una lista de los vértices aislado.
    Ejemplo Entrada: 
        (['A','B','C','D','E'],[('A','B'),('B','C'),('C','B')])
    Ejemplo formato salida: 
        ['D','E']
    '''
    grado = cuenta_grado(grafo_lista)
    v_aisl = []

    for v in grado:
        if grado[v] == 0:
            v_aisl.append(v)
            
    return v_aisl

    pass

def componentes_conexas(grafo_lista):
    '''
    Dado un grafo en representacion de lista, obtiene sus componentes conexas.
    Ejemplo Entrada: 
        (['A','B','C','D','E'],[('A','B'),('B','C'),('C','B'),('D','E')])
    Ejemplo formato salida: 
        [['A, 'B','C'], ['D','E']]
    '''

    vertices, aristas = grafo_lista
    visitados = set()
    conexiones = {v: set() for v in vertices}
    componentes = []

    for origen, destino in aristas:
        conexiones[origen].add(destino)
        conexiones[destino].add(origen)
    
    for v in vertices:
        for v in not visitados:
            pila = [v]
            componente = []
            while pila:
                actual = pila.pop()
                if actual not in visitados:
                    visitados.add(actual)
                    componente.append(actual)
                    pila.extend(conexiones[actual] - visitados)
    
            componentes.append(componente)
    
    return componentes

    pass

def es_conexo(grafo_lista):
    '''
    Dado un grafo en representacion de lista, y utilizando la función "componentes_conexas"
    devuelve True/False si el grafo es o no conexo.
    '''

    componentes = componentes_conexas(grafo_lista)
    return len(componentes) == 1

    pass

def es_completo(grafo_lista):
    '''
    Dado un grafo en representacion de lista, devuelve True/False si el grafo es o no completo.
    Ejemplo Entrada:
    	['3', 'A', 'B', 'C', 'A B', 'B A', 'A C', 'C A', 'B C', 'C B']
    Ejemplo formato salida:
    	True
    '''

    vertices, aristas = grafo_lista
    n = len(vertices)

    es_dirigido = all((b,a) in aristas for (a,b) in aristas)

    if es_dirigido:
        if(len(aristas) != ((n*(n-1))/2)):
            return False


    pass
    	
def aristas_de(grafo, vertice):
    '''
    Dado un grafo en representacion de lista, devuelva todas las aristas salientes desde un vértice dado
    Ejemplo Entrada:
    	grafo = ['3', 'A', 'B', 'C', 'A B', 'A C', 'B C']
	aristas_de(grafo, 'A')
    Ejemplo formato salida:
    	[('A', 'B'), ('A', 'C')]
    '''

    n = int(grafo[0])
    aristas_lista = grafo[n+1:]
    aristas = []

    for arista in aristas_lista:
        origen, destino = arista.split()
        if origen == vertice:
            aristas.append((origen, destino))

    return aristas

    pass

def grafo_inducido(grafo, subconjunto_vertices):
    '''
    Dado un grafo en representacion de lista, y un subconjunto de vertices,
    devuelva el subgrafo inducido
    Ejemplo Entrada:
    	grafo = ['4', 'A', 'B', 'C', 'D', 'A B', 'A C', 'B D']
	subconjunto_vertices = ['A', 'B', 'C']
    Ejemplo formato salida:
    	(['A', 'B', 'C'], [('A', 'B'), ('A', 'C')])
    '''

    n = int(grafo[0])
    aristas_lista = grafo[n+1:]
    aristas_inducidas = []

    for arista in aristas_lista:
        origen, destino = arista.split()
        if origen in subconjunto_vertices and destino in subconjunto_vertices:
            aristas_inducidas.append((origen, destino))

    return (subconjunto_vertices, aristas_inducidas)

    pass

def grafo_complementario(grafo):
    '''
    Dado un grafo en representacion de lista, devuelve el grafo complementario en forma de lista
    Ejemplo Entrada:
    	['3', 'A', 'B', 'C', 'A B', 'B C']
    Ejemplo formato salida:
    	(['A', 'B', 'C'], [('A', 'C'), ('B', 'A'), ('C', 'A'), ('C', 'B')])
    '''

    n = int(grafo[0])
    aristas_lista = grafo[n+1:]
    vertices_lista = grafo[1:n+1]

    aristas_existentes = set()
    for arista in aristas_lista:
        origen, destino = arista.split()
        aristas_existentes.add((origen, destino))

    aristas_complementarias = []

    for origen in vertices_lista:
        for destino in vertices_lista:
            if origen != destino and (origen, destino) not in aristas_existentes:
                aristas_complementarias.append((origen, destino))

    return (vertices_lista, aristas_complementarias)

    pass