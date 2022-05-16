from grafo import Grafo
from arista import Arista
import random
weight = 'Peso'

def erdosrenyi(n,m, dirigido=False, auto=False):
  """
  Grafo Erdos-Renyi (método aleatorio)
  n : número de nodos
  m : número de aristas 
  """
  #a = Arista
  g = Grafo('Erdos-Renyi')
  for i in range(n):
      g.addNodo(str(i))
  #edges = {}
  for i in range(m):
    u = random.randint(0, n-1)
    v = random.randint(0, n-1)
    e = (u, v)
    if u != v:
      peso = random.randint(1, 50)
      g.addArista('{} -- {}'.format(str(u), str(v)),str(u),str(v),peso)

  return g


print ("Modelo Erdös y Rényi  ----------")
nodo = int(input("Ingrese número de nodos: "))
arista = int(input("Ingrese número de aristas: "))
nodo_fin = int(input("Indica el segundo nodo o final a encontrar ruta : "))

erdosrenyi_ = erdosrenyi(nodo,arista)
erdosrenyi_.savedArchivoDijsktra('{}_n{}'.format('_completo',str(nodo)))

n_inicia = list(erdosrenyi_.nodos.keys())[0]
n_final = list(erdosrenyi_.nodos.keys())[nodo_fin]

grafoDijkstra = Grafo.dijkstra(erdosrenyi_,n_inicia,n_final)
grafoDijkstra.savedArchivoDijsktra('{}_n{}'.format('_Erdos',str(nodo)))

