import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_analizza(self, e):
        dist = self._view.txt_distanza.value
        if dist is None or dist == "":
            self._view.create_alert("Inserire il distanza")
            return
        self._view.txt_result.controls.append(ft.Text(f"distanza: {dist} miles"))
        self._view.update_page()
