import sys
import os

# Agregar el directorio src al path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

# Importar y ejecutar la aplicación
from GUI.InterfazGUI import CalculadoraAhorroApp

if __name__ == '__main__':
    CalculadoraAhorroApp().run()