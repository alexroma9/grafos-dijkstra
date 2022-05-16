from grafo import Grafo 
import random 
from math import sqrt

def distancia(NI, NF):
  x1 = NI.attributos['px']
  y1 = NI.attributos['py']
  x2 = NF.attributos['px']
  y2 = NF.attributos['py']
  dista = sqrt((x2-x1)**2 + (y2-y1)**2)
  return dista


def geosim(n,r):
  """
  Grafo Geografíco Simple (Método aleatorio)
  n : número de nodos.
  r : distancia para generar la arista entre dos nodos.
  """
  g = Grafo('GeoSimple')
  for i in range(n):
    nodo = g.addNodo(str(i))
    nodo.attributos['px'] = random.random()
    nodo.attributos['py'] = random.random() 
  conteoAristas = 1
  for i in range(n):
    for j in range(n):
      if i != j:
        nI = g.giveNodo(str(i))
        nF = g.giveNodo(str(j))
        dista = distancia(nI,nF)
        if dista <= r:
          peso = random.randint(1, 50)
          g.addArista('{} -- {}'.format(str(i), str(j)),str(i),str(j),peso)
          conteoAristas += 1  
  return g

print ("Modelo Geográfico simple  ----------")
n_nodo = int(input("Ingrese número de nodos: "))
dist = float(input("Ingrese la distancia máxima para crear un nodo valor entre 0 y 1: "))
nodo_fin = int(input("Indica el segundo nodo o final a encontrar ruta : "))

geosim_ = geosim(n_nodo,dist)
geosim_.savedArchivoDijsktra('{}_n{}'.format('_completo',str(n_nodo)))

n_inicia = list(geosim_.nodos.keys())[0]
n_final = list(geosim_.nodos.keys())[nodo_fin]

grafoDijkstra = Grafo.dijkstra(geosim_,n_inicia,n_final)
grafoDijkstra.savedArchivoDijsktra('{}_n{}'.format('_GeoSimple',str(n_nodo)))

