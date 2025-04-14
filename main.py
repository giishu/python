from Ejercicios.practica1 import *
from Ejercicios.practica2 import *

def main():
    entrada = ['3', 'A', 'B', 'C', 'A B', 'B C', 'C B']
    grafo = lee_grafo_stdin(entrada)
    resultado = cuenta_grado(grafo)
    print(grafo)
    print(resultado)

    
if __name__ == '__main__':
    main()
