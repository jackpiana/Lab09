import networkx as nx

from database.DAO import dao


class Model:
    def __init__(self):
        self._areoporti = dao.get_airports()
        self._grafo = nx.Graph()

    def buildGraph(self):
        # Aggiungiamo i nodi
        self._grafo.add_nodes_from(self._areoporti)

if __name__ == "__main__":
    m = Model()
    for areoporto in m._areoporti:
        print(areoporto)
