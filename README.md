# Proyectos de Aula LPCL

**Integrantes:** Esteban Arias y Juanita Legarda

---

## Calculadora de Ahorro Programado

Se requiere una aplicación que permita conocer el valor que debe ahorrar mensualmente una persona que suscriba un ahorro programado al final del periodo de tiempo pactado, para alcanzar una meta de ahorro.  
La aplicación permite además realizar abonos extras en el tiempo y cantidad que el ahorrador desee.

---

## Solución del problema

### 1. Perfil del entrevistado

- **Nombre:** Adriana Gonzalez Mejia  
- **Edad:** 43 años  
- **Ocupación:** Analista de crédito  
- **Experiencia:** Lleva años ahorrando mensualmente para metas como vacaciones, estudio o gustos personales. No es financiera, pero sí muy organizada con sus metas.  
- **Link de la entrevista:** [Ver entrevista](https://drive.google.com/file/d/1dJfGLr8ntzFC1T09SV6Yael1X12K_EQU/view?usp=sharing)

---

### 2. Identificación de variables y fórmulas

#### Variables de entrada:
- meta: float  
- meses: int  
- abono_extra: float  
- interes_mensual: float  

#### Variables de salida:
- ahorro_mensual: float  
- total_depositado: float  
- saldo_final: float  
- ganancia_intereses: float  

---

## 3. Fórmulas utilizadas

### Cálculo sin interés (interes_mensual = 0)

```python
ahorro_mensual = (meta - abono_extra) / meses
```

### Cálculo con interés mensual compuesto (interes_mensual > 0)

- Fórmula usada en el código Python:
```python
factor = ((1 + interes_mensual) ** meses - 1) / interes_mensual
ahorro_mensual = (meta - abono_extra * (1 + interes_mensual) ** meses) / factor
```

### Cálculo con interés mensual compuesto (interes_mensual > 0)

- Fórmula equivalente en Excel:
```python
=PAGO(InteresMensual, Meses, 0, -(Meta - AbonoExtra * (1 + InteresMensual)^Meses))
```

---

## 4. Casos de prueba en hoja de cálculo

Se desarrolló una hoja de cálculo con 11 casos de prueba, organizados en tres secciones:
- Casos normales (sin interés, sin abonos extra)
- Casos extraordinarios (con abonos extra y/o interés)
- Casos de error (meta negativa, tiempo igual a cero, meta superada)

Esta hoja permitió validar tanto el comportamiento del cálculo como el lanzamiento de excepciones correctamente definidas en el código.

**Enlace al documento:** [Ver hoja de cálculo](https://docs.google.com/spreadsheets/d/1LvZmssoXyPGCphXX650ifGW0w8BjKPEnsEZLR5gztD4/edit?usp=sharing)

---

## 5. Ejecucion de programa ( vista en consola )

Para correr la aplicacion en consola:
```bash
py src/view/interfaz.py
```

Ejecucion de las pruebas:
```bash
py test/test_ahorro.py
```
