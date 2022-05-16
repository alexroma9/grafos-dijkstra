from grafo import Grafo
import random


def malla(m, n, dirigido=False):
  """
  Grafo Malla (Método aleatorio)
  m : número de filas
  n : número de columnas
  """
  g = Grafo('Malla')
  Aristas = 1
  Nodos = 1
  for fila in range(m):
    for columna in range(n):  
      if columna < (n-1):
        peso = random.randint(1, 50)
        g.addArista('{} -- {}'.format(fila * n + columna, fila * n + columna + 1), str(fila * n + columna), str(fila * n + columna + 1),peso)
        #g.addArista('{} -- {}'.format(str(fila), str(columna)),str(fila),str(columna),peso)
#        g.addArista(Aristas, str(Nodos), str(Nodos + 1))    
        Aristas += 1
      if fila < (m-1):
        peso2 = random.randint(1, 50)
        #g.addArista('{} -- {}'.format(str(fila), str(columna)),str(fila),str(columna),peso)
        g.addArista('{} -- {}'.format(fila * n + columna, (fila+1)* n + columna), str(fila * n + columna), str((fila+1)* n + columna),peso2)
#        g.addArista(Aristas, str(Nodos), str(Nodos + 2))
        Aristas += 1      
      Nodos += 1
  return g

print ("Modelo Malla  ----------")
columnas = int(input("Ingrese número de columnas: "))
filas = int(input("Ingrese número de filas: "))
nodo_fin = int(input("Indica el segundo nodo o final a encontrar ruta : "))

malla_ = malla(columnas,filas)
malla_.savedArchivoDijsktra('{}_n{}'.format('_completo',str(columnas*filas)))

n_inicia = list(malla_.nodos.keys())[0]
n_final = list(malla_.nodos.keys())[nodo_fin]

grafoDijkstra = Grafo.dijkstra(malla_,n_inicia,n_final)
grafoDijkstra.savedArchivoDijsktra('{}_n{}'.format('_Malla',str(columnas*filas)))


