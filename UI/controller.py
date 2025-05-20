import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_analizza(self, e):
        dist = self._view.txt_distanza.value
        try:
            int(dist)
            print(f"distanza media minima selezionata: {dist} miles\n")
            self._model.buildGraph(dist)
            self._view.txt_result.controls.append(ft.Text(f"Grafo creato!"))
            self._view.txt_result.controls.append(ft.Text(f"Distanza media minima selezionata: {dist} miles"))
            self._view.txt_result.controls.append(ft.Text(f"Numero di vertici: {len(self._model._grafo.nodes)}"))
            self._view.txt_result.controls.append(ft.Text(f"Numero di archi: {len(self._model._grafo.edges)}"))
            for e in self._model._grafo.edges(data = True):
                a = e[0]
                b = e[1]
                distanza = e[2]["weight"]
                self._view.txt_result.controls.append(ft.Text(f"{a.CITY} {a.AIRPORT} - {b.CITY} {b.AIRPORT} --- distanza: {distanza}"))
            self._view._page.update()




        except ValueError:
            self._view.create_alert("inserire un numero intero!")
        self._view.update_page()
