import sys
sys.path.append("src")

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

from model import Modulos


KV = """
<RootUI>:
    orientation: "vertical"
    padding: 10
    spacing: 10

    # Espaciador superior para bajar las cajas de entrada
    Widget:
        size_hint_y: None
        height: 120

    BoxLayout:
        size_hint_y: None
        height: self.minimum_height
        spacing: 10

        BoxLayout:
            orientation: "vertical"
            size_hint_x: 0.25
            Label:
                text: "Meta"
                size_hint_y: None
                height: 28
            TextInput:
                id: meta_in
                hint_text: "Ej: 1200000"
                input_filter: "float"
                multiline: False
                size_hint_y: None
                height: 48
                font_size: "18sp"
                padding_y: [10, 10]

        BoxLayout:
            orientation: "vertical"
            size_hint_x: 0.25
            Label:
                text: "Meses"
                size_hint_y: None
                height: 28
            TextInput:
                id: meses_in
                hint_text: "Ej: 12"
                input_filter: "int"
                multiline: False
                size_hint_y: None
                height: 48
                font_size: "18sp"
                padding_y: [10, 10]

        BoxLayout:
            orientation: "vertical"
            size_hint_x: 0.25
            Label:
                text: "Abono extra"
                size_hint_y: None
                height: 28
            TextInput:
                id: abono_in
                hint_text: "Ej: 0"
                input_filter: "float"
                multiline: False
                size_hint_y: None
                height: 48
                font_size: "18sp"
                padding_y: [10, 10]

        BoxLayout:
            orientation: "vertical"
            size_hint_x: 0.25
            Label:
                text: "Interés mensual"
                size_hint_y: None
                height: 28
            TextInput:
                id: interes_in
                hint_text: "Ej: 0.01"
                input_filter: "float"
                multiline: False
                size_hint_y: None
                height: 48
                font_size: "18sp"
                padding_y: [10, 10]

    BoxLayout:
        size_hint_y: None
        height: 40
        spacing: 10
        Button:
            text: "Calcular"
            on_release: root.calcular()
        Button:
            text: "Limpiar"
            on_release: root.limpiar()

    Label:
        id: resultado_lbl
        text: root.resultado_texto
        size_hint_y: None
        height: 30

    Label:
        text: "Evolución del ahorro"
        size_hint_y: None
        height: 24

    ScrollView:
        do_scroll_x: False
        GridLayout:
            id: tabla
            cols: 4
            size_hint_y: None
            row_default_height: 28
            height: self.minimum_height
"""


class RootUI(BoxLayout):
    resultado_texto = StringProperty("")

    def on_kv_post(self, base_widget):
        self._crear_encabezados_tabla()

    def limpiar(self):
        self.ids.meta_in.text = ""
        self.ids.meses_in.text = ""
        self.ids.abono_in.text = ""
        self.ids.interes_in.text = ""
        self.resultado_texto = ""
        self._limpiar_tabla()
        self._crear_encabezados_tabla()

    def calcular(self):
        try:
            meta = float(self.ids.meta_in.text or 0)
            meses = int(self.ids.meses_in.text or 0)
            abono = float(self.ids.abono_in.text or 0)
            interes = float(self.ids.interes_in.text or 0)

            ahorro_mensual = Modulos.calcular_ahorro_mensual(meta, meses, abono, interes)
            self.resultado_texto = f"Ahorro mensual: {ahorro_mensual:.2f}"

            self._poblar_tabla(meses, ahorro_mensual, interes)

        except ValueError:
            self.resultado_texto = "Error: Verifique los datos numéricos."
        except Exception as e:
            self.resultado_texto = f"Error: {e}"

    def _crear_encabezados_tabla(self):
        tabla = self.ids.tabla
        encabezados = ["Mes", "Depósito", "Interés", "Saldo final"]
        for texto in encabezados:
            tabla.add_widget(Label(text=texto, bold=True))

    def _limpiar_tabla(self):
        tabla = self.ids.tabla
        tabla.clear_widgets()

    def _poblar_tabla(self, meses: int, ahorro_mensual: float, interes_mensual: float):
        self._limpiar_tabla()
        self._crear_encabezados_tabla()

        saldo = 0.0
        for mes in range(1, meses + 1):
            saldo += ahorro_mensual
            interes_ganado = saldo * interes_mensual
            saldo += interes_ganado

            fila = [
                str(mes),
                f"{ahorro_mensual:.2f}",
                f"{interes_ganado:.2f}",
                f"{saldo:.2f}",
            ]
            for celda in fila:
                self.ids.tabla.add_widget(Label(text=celda))


class CalculadoraAhorroApp(App):
    def build(self):
        Builder.load_string(KV)
        return RootUI()


if __name__ == "__main__":
    CalculadoraAhorroApp().run()


