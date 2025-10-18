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
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.metrics import dp
from kivy.graphics import Color, Rectangle

# --- Grafica ---
try:
    from kivy_garden.graph import Graph, MeshLinePlot
    _GRAPH_AVAILABLE = True
except Exception:  # ImportError u otros problemas de carga
    Graph = None
    MeshLinePlot = None
    _GRAPH_AVAILABLE = False

from model import Modulos
from model.Modulos import ErrorValorMeta, ErrorValorMeses, ErrorAbonoExcesivo

KV = """
<CalculadoraScreen>:
    orientation: "vertical"
    padding: dp(20)
    spacing: dp(15)
    canvas.before:
        Color:
            rgba: 0.1, 0.1, 0.15, 1
        Rectangle:
            pos: self.pos
            size: self.size
 
    # Título principal
    Label:
        text: "Calculadora de Ahorro Programado"
        font_size: "24sp"
        bold: True
        color: [0.7, 0.9, 1, 1]
        size_hint_y: None
        height: dp(50)
        halign: "center"

    # Campos de entrada: textos arriba y inputs debajo
    BoxLayout:
        size_hint_y: None
        height: dp(140)
        spacing: dp(15)
        padding: [dp(10), 0, dp(10), 0]
        orientation: "vertical"

        # Fila de títulos
        BoxLayout:
            size_hint_y: None
            height: dp(30)
            spacing: dp(15)
            Label:
                text: "Meta de Ahorro"
                color: [0.8, 0.8, 0.9, 1]
            Label:
                text: "Meses"
                color: [0.8, 0.8, 0.9, 1]
            Label:
                text: "Abono Extra"
                color: [0.8, 0.8, 0.9, 1]
            Label:
                text: "Interés Mensual"
                color: [0.8, 0.8, 0.9, 1]

        # Fila de inputs (debajo de las palabras)
        BoxLayout:
            size_hint_y: None
            height: dp(50)
            spacing: dp(15)
            TextInput:
                id: meta_in
                hint_text: "Ej: 1200000"
                multiline: False
                font_size: "16sp"
                padding: [dp(10), dp(10), dp(10), dp(10)]
                background_normal: ''
                background_color: [0.3, 0.3, 0.3, 1]
                foreground_color: [1, 1, 1, 1]
                hint_text_color: [0.7, 0.7, 0.7, 1]
                cursor_color: [1, 1, 1, 1]
            TextInput:
                id: meses_in
                hint_text: "Ej: 12"
                multiline: False
                font_size: "16sp"
                padding: [dp(10), dp(10), dp(10), dp(10)]
                background_normal: ''
                background_color: [0.3, 0.3, 0.3, 1]
                foreground_color: [1, 1, 1, 1]
                hint_text_color: [0.7, 0.7, 0.7, 1]
                cursor_color: [1, 1, 1, 1]
            TextInput:
                id: abono_in
                hint_text: "Ej: 0"
                multiline: False
                font_size: "16sp"
                padding: [dp(10), dp(10), dp(10), dp(10)]
                background_normal: ''
                background_color: [0.3, 0.3, 0.3, 1]
                foreground_color: [1, 1, 1, 1]
                hint_text_color: [0.7, 0.7, 0.7, 1]
                cursor_color: [1, 1, 1, 1]
            TextInput:
                id: interes_in
                hint_text: "Ej: 0.01"
                multiline: False
                font_size: "16sp"
                padding: [dp(10), dp(10), dp(10), dp(10)]
                background_normal: ''
                background_color: [0.3, 0.3, 0.3, 1]
                foreground_color: [1, 1, 1, 1]
                hint_text_color: [0.7, 0.7, 0.7, 1]
                cursor_color: [1, 1, 1, 1]

    # Botones con mejor diseño
    BoxLayout:
        size_hint_y: None
        height: dp(60)
        spacing: dp(20)
        padding: [dp(50), dp(10), dp(50), dp(10)]
        Button:
            text: "Calcular"
            font_size: "18sp"
            bold: True
            background_color: [0.2, 0.6, 0.3, 1]
            color: [1, 1, 1, 1]
            on_release: root.calcular()
        Button:
            text: "Limpiar"
            font_size: "18sp"
            bold: True
            background_color: [0.6, 0.2, 0.2, 1]
            color: [1, 1, 1, 1]
            on_release: root.limpiar()

    # Resultado con mejor diseño
    BoxLayout:
        size_hint_y: None
        height: dp(60)
        canvas.before:
            Color:
                rgba: 0.2, 0.3, 0.4, 1
            RoundedRectangle:
                pos: self.pos
                size: self.size
                radius: [dp(10), dp(10), dp(10), dp(10)]
        Label:
            id: resultado_lbl
            text: root.resultado_texto
            font_size: "20sp"
            bold: True
            color: [0.7, 1, 0.7, 1]
            halign: "center"

    # Tabla de resultados
    Label:
        text: "Evolución del Ahorro"
        font_size: "18sp"
        bold: True
        color: [0.8, 0.8, 0.9, 1]
        size_hint_y: None
        height: dp(40)

    ScrollView:
        size_hint_y: 0.45
        do_scroll_x: False
        canvas.before:
            Color:
                rgba: 0.2, 0.2, 0.25, 1
            RoundedRectangle:
                pos: self.pos
                size: self.size
                radius: [dp(10), dp(10), dp(10), dp(10)]
        GridLayout:
            id: tabla
            cols: 4
            size_hint_y: None
            row_default_height: dp(35)
            height: self.minimum_height
            spacing: [dp(2), dp(2)]
            padding: [dp(5), dp(5), dp(5), dp(5)]

    # Gráfica
    BoxLayout:
        id: grafico_box
        size_hint_y: 0.35
        canvas.before:
            Color:
                rgba: 0.2, 0.2, 0.25, 1
            RoundedRectangle:
                pos: self.pos
                size: self.size
                radius: [dp(10), dp(10), dp(10), dp(10)]

<RootUI>:
    ScreenManager:
        id: screen_manager
        CalculadoraScreen:
            name: "calculadora"
""" 

class MensajePopup(Popup):
    def __init__(self, titulo, mensaje, tipo="info", **kwargs):
        super().__init__(**kwargs)
        self.title = titulo
        self.title_color = [0.9, 0.9, 0.95, 1]
        self.size_hint = (0.7, 0.5)
        self.auto_dismiss = False
        self.background_color = [0.15, 0.15, 0.2, 1]
        
        # Crear contenido del popup
        content = BoxLayout(orientation='vertical', padding=dp(20), spacing=dp(15))
        content.canvas.before.clear()
        
        # Icono y mensaje
        icono = "❌" if tipo == "error" else "✅" if tipo == "success" else "ℹ️"
        mensaje_label = Label(
            text=f"{icono}\n{mensaje}",
            text_size=(None, None),
            halign='center',
            valign='middle',
            font_size='16sp',
            color=[0.9, 0.9, 0.95, 1]
        )
        content.add_widget(mensaje_label)
        
        # Botón OK
        btn_ok = Button(
            text="OK",
            size_hint_y=None,
            height=dp(50),
            font_size='18sp',
            bold=True,
            background_color=[0.2, 0.6, 0.8, 1],
            color=[1, 1, 1, 1]
        )
        btn_ok.bind(on_release=self.dismiss)
        content.add_widget(btn_ok)
        
        self.content = content

class CalculadoraScreen(Screen):
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
        self.mostrar_mensaje("Información", "Campos limpiados correctamente", "success")

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
            self.resultado_texto = f"💰 Ahorro mensual requerido: ${ahorro_mensual:,.2f}"

            self._poblar_tabla(meses, ahorro_mensual, interes)
            self.mostrar_mensaje("¡Cálculo Exitoso!", 
                               f"Se ha calculado tu plan de ahorro.\n\n"
                               f"Meta: ${meta:,.2f}\n"
                               f"Período: {meses} meses\n"
                               f"Ahorro mensual: ${ahorro_mensual:,.2f}", 
                               "success")

        except ValueError as ve:
            self.mostrar_mensaje("Error de Validación", str(ve), "error")
        except ErrorValorMeta as evm:
            self.mostrar_mensaje("Error en Meta", str(evm), "error")
        except ErrorValorMeses as evmes:
            self.mostrar_mensaje("Error en Meses", str(evmes), "error")
        except ErrorAbonoExcesivo as eae:
            self.mostrar_mensaje("Error en Abono", str(eae), "error")
        except Exception as e:
            self.mostrar_mensaje("Error Inesperado", f"Ha ocurrido un error inesperado:\n{e}", "error")

    def mostrar_mensaje(self, titulo: str, mensaje: str, tipo: str = "info"):
        popup = MensajePopup(titulo, mensaje, tipo)
        popup.open()

    def _crear_encabezados_tabla(self):
        tabla = self.ids.tabla
        encabezados = ["📅 Mes", "💰 Depósito", "📈 Interés", "💎 Saldo Final"]
        for i, texto in enumerate(encabezados):
            label = Label(
                text=texto, 
                bold=True, 
                font_size='14sp',
                color=[0.6, 0.8, 1, 1]
            )
            tabla.add_widget(label)

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

            # Crear fila con mejor formato
            fila = [
                f"{mes}",
                f"${ahorro_mensual:,.2f}",
                f"${interes_ganado:,.2f}",
                f"${saldo:,.2f}",
            ]
            
            for i, celda in enumerate(fila):
                # Colores alternados para las filas (fondo por celda)
                bg_rgba = [0.3, 0.3, 0.35, 1] if mes % 2 == 0 else [0.25, 0.25, 0.3, 1]

                cell_container = BoxLayout(orientation='vertical', size_hint_y=None, height=dp(35), padding=[dp(6), 0, dp(6), 0])
                with cell_container.canvas.before:
                    Color(rgba=bg_rgba)
                    rect = Rectangle(pos=cell_container.pos, size=cell_container.size)
                def _sync_rect_pos(instance, value):
                    rect.pos = value
                def _sync_rect_size(instance, value):
                    rect.size = value
                cell_container.bind(pos=_sync_rect_pos, size=_sync_rect_size)

                label = Label(
                    text=celda,
                    font_size='12sp',
                    color=[0.92, 0.92, 0.98, 1],
                    halign='left',
                    valign='middle'
                )
                label.bind(size=lambda inst, val: setattr(inst, 'text_size', val))
                cell_container.add_widget(label)
                self.ids.tabla.add_widget(cell_container)

            # guardar para grafica
            self.data_points.append((mes, saldo))

        # actualizar gráfica
        self._actualizar_grafico()

    # --- Metodos para la grafica ---
    def _crear_grafico(self):
        # Si la librería de gráficas no está disponible, mostrar aviso y no crear gráfica
        if not _GRAPH_AVAILABLE:
            aviso = Label(
                text="La librería de gráficas no está instalada.\nInstala 'kivy_garden.graph' para ver la gráfica.",
                color=[0.9, 0.9, 0.95, 1],
                font_size='14sp',
                halign='center',
                valign='middle'
            )
            self.ids.grafico_box.add_widget(aviso)
            self.grafico = None
            self.plot = None
            return

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
        if not getattr(self, 'plot', None) or not getattr(self, 'grafico', None):
            return
        self.plot.points = self.data_points
        # ajustar limites
        try:
            self.grafico.xmax = max(m for m, _ in self.data_points) + 1
            self.grafico.ymax = max(s for _, s in self.data_points) * 1.1
        except Exception:
            # Si por cualquier razón la gráfica no acepta los valores, lo ignoramos
            pass

    def _reset_grafico(self):
        if getattr(self, 'plot', None):
            self.plot.points = []
        if getattr(self, 'grafico', None):
            try:
                self.grafico.xmax = 12
                self.grafico.ymax = 10000
            except Exception:
                pass


class RootUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # El ScreenManager se crea automáticamente desde el KV


class CalculadoraAhorroApp(App):
    def build(self):
        Builder.load_string(KV)
        return RootUI()


if __name__ == "__main__":
    from kivy.config import Config
    Config.set('graphics', 'width', '1000')
    Config.set('graphics', 'height', '700')
    Config.set('graphics', 'resizable', '1')
    Config.set('graphics', 'borderless', '0')
    Config.set('graphics', 'window_state', 'normal')
    
    app = CalculadoraAhorroApp()
    app.run()  