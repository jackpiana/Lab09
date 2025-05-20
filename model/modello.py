from time import time

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


from database.DAO import dao

class Model:
    def __init__(self):
        self._areoporti = dao.get_airports()
        self._grafo = nx.Graph()

#lento in culo
    def mine_add_edges(self, mediaMinima):
        checked = []
        for u in self._areoporti:
            for v in self._areoporti:
                if (u, v) not in checked:
                    flights = dao.get_flights(u, v)
                    checked.append((v, u))
                    distances = []
                    distanza_media = -1
                    for flight in flights:
                        distances.append(flight.DISTANCE)
                        distanza_media = np.mean(distances)
                    if distanza_media > mediaMinima:
                        self._grafo.add_edge(u, v, weight = distanza_media)
                        print(f"{u}, {v}, weight = {distanza_media}")

    # lento in culo
    def add_edges_v2(self, mediaMinima):
        checked = set()
        for u in self._areoporti:
            for v in self._areoporti:
                if u == v:
                    continue
                if (v, u) in checked:
                    continue
                distanza_media = dao.get_avg_distance(u, v)
                if distanza_media > mediaMinima:
                    checked.add((v, u))
                    self._grafo.add_edge(u, v, weight=distanza_media)
                    print(f"{u}, {v}, weight = {distanza_media}")

    #godo
    def add_edges(self, mediaMinima):
        potential_edges = dao.get_edges()
        for edge in potential_edges:
            media = int(float(edge[3])/int(edge[2]))
            if int(media) > int(mediaMinima):
                u = self._areoporti[edge[0]]
                v = self._areoporti[edge[1]]
                self._grafo.add_node(u)
                self._grafo.add_node(v)
                self._grafo.add_edge(u, v, weight=media)
                print(f"added edge:\n"
                      f"{u.CITY} {u.IATA_CODE}\n"
                      f"{v.CITY} {v.IATA_CODE} \n"
                      f"weight = {media}"
                      f"\n")


    def buildGraph(self, mediaMinima):
        self.add_edges(mediaMinima)


if __name__ == "__main__":
    m = Model()
    start = time()
    m.buildGraph("4000")
    end = time()
    print(f"Tempo: {end - start}")
