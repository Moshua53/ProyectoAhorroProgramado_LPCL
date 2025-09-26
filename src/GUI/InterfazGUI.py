import sys
sys.path.append("src")

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup

# --- Grafica ---
from kivy_garden.graph import Graph, MeshLinePlot  

from model import Modulos
from model.Modulos import ErrorValorMeta, ErrorValorMeses, ErrorAbonoExcesivo

KV = """
<RootUI>:
    orientation: "vertical"
    padding: 10
    spacing: 10
 
    Widget:
        size_hint_y: None
        height: 80

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
                text: "Interes mensual"
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
        text: "Evolucion del ahorro"
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

    # --- Aqui va la grafica ---
    BoxLayout:
        id: grafico_box
        size_hint_y: 0.5
""" 

class RootUI(BoxLayout):
    resultado_texto = StringProperty("")
    data_points = ListProperty([])

    def on_kv_post(self, base_widget):
        self._crear_encabezados_tabla()
        self._crear_grafico()

    def limpiar(self):
        self.ids.meta_in.text = ""
        self.ids.meses_in.text = ""
        self.ids.abono_in.text = ""
        self.ids.interes_in.text = ""
        self.resultado_texto = ""
        self._limpiar_tabla()
        self._crear_encabezados_tabla()
        self._reset_grafico()

    def calcular(self):
        try:
            if not self.ids.meta_in.text.strip():
                raise ValueError("La meta es obligatoria y debe ser un número válido.")
            if not self.ids.meses_in.text.strip():
                raise ValueError("Los meses son obligatorios y deben ser un número válido.")

            meta = float(self.ids.meta_in.text)
            meses = int(self.ids.meses_in.text)
            abono = float(self.ids.abono_in.text or 0)
            interes = float(self.ids.interes_in.text or 0)

            ahorro_mensual = Modulos.calcular_ahorro_mensual(meta, meses, abono, interes)
            self.resultado_texto = f"Ahorro mensual: {ahorro_mensual:.2f}"

            self._poblar_tabla(meses, ahorro_mensual, interes)

        except ValueError as ve:
            self.mostrar_error(f"⚠ Error de valor:\n{ve}")
        except ErrorValorMeta as evm:
            self.mostrar_error(str(evm))
        except ErrorValorMeses as evmes:
            self.mostrar_error(str(evmes))
        except ErrorAbonoExcesivo as eae:
            self.mostrar_error(str(eae))
        except Exception as e:
            self.mostrar_error(f"❌ Error inesperado:\n{e}")

    def mostrar_error(self, mensaje: str):
        contenido = GridLayout(cols=1, padding=20, spacing=10)
        contenido.add_widget(Label(text=mensaje))
        cerrar = Button(text="Cerrar", size_hint=(1, 0.3))
        contenido.add_widget(cerrar)

        popup = Popup(title="Error",
                      content=contenido,
                      size_hint=(0.7, 0.4),
                      auto_dismiss=False)
        cerrar.bind(on_press=popup.dismiss)
        popup.open()

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
        self.data_points = []  # reinicia puntos de la gráfica

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

            # guardar para grafica
            self.data_points.append((mes, saldo))

        # actualizar gráfica
        self._actualizar_grafico()

    # --- Metodos para la grafica ---
    def _crear_grafico(self):
        grafico = Graph(
            xlabel="Mes",
            ylabel="Saldo",
            x_ticks_minor=1,
            x_ticks_major=1,
            y_ticks_major=1000,
            y_grid_label=True,
            x_grid_label=True,
            padding=5,
            x_grid=True,
            y_grid=True,
            xmin=0,
            xmax=12,
            ymin=0,
            ymax=10000,
        )
        self.plot = MeshLinePlot(color=[0, 1, 0, 1])
        grafico.add_plot(self.plot)
        self.ids.grafico_box.add_widget(grafico)
        self.grafico = grafico

    def _actualizar_grafico(self):
        if not self.data_points:
            return
        self.plot.points = self.data_points
        # ajustar limites
        self.grafico.xmax = max(m for m, _ in self.data_points) + 1
        self.grafico.ymax = max(s for _, s in self.data_points) * 1.1

    def _reset_grafico(self):
        self.plot.points = []
        self.grafico.xmax = 12
        self.grafico.ymax = 10000


class CalculadoraAhorroApp(App):
    def build(self):
        Builder.load_string(KV)
        return RootUI()


if __name__ == "__main__":
    CalculadoraAhorroApp().run()  