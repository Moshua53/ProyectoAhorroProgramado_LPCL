# Proyectos de Aula LPCL

**Integrantes:** Moises Herrera y Mateo Molina

---

## Condiciones Generales

- Equipos de 2 estudiantes. Solo en caso de que los matriculados en el curso sean impares, se permite un equipo de 3.
- Cada equipo debe contactar a un experto que les ayude a entender el problema y redactar los casos de prueba. La entrevista con el experto debe ser grabada en video o audio.
- De la entrevista con el experto, el equipo debe identificar las variables de entrada y salida, así como las fórmulas que deben utilizar para realizar los cálculos.
- Usando las variables y las fórmulas suministradas por el experto, deberán construir un libro de Excel con al menos 10 casos de prueba del problema.
- El equipo debe tener un repositorio en GitHub donde hacen la entrega. En la plataforma UVirtual deben suministrar la URL del proyecto.

---

## Entregas

- Pruebas unitarias construidas  
- Interfaz de usuario tipo consola  
- Interfaz de usuario gráfica  
- Base de Datos  
- Interfaz de usuario web  

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

- Meta final de ahorro (`meta`)
- Duración del ahorro en meses (`meses`)
- Abonos extra (mes, valor) (`abonos`)

#### Variables de salida:

- Valor mensual a ahorrar  
- Total ahorrado a la fecha  
- Saldo restante por ahorrar  

---

### 3. Fórmulas del cálculo de ahorro

```plaintext
ahorro_mensual = meta / meses

abonos_extra = abono_1 + abono_2 + abono_3 + ... + abono_n

total_ahorrado = (ahorro_mensual * meses_cumplidos) + abonos_extra

saldo = meta - total_ahorrado

nuevo_ahorro_mensual = saldo / (meses - meses_cumplidos)

```

---

## 4. Casos de prueba en hoja de cálculo

Se construyó un archivo en Google Sheets que contiene al menos 10 casos de prueba aplicando las fórmulas y variables identificadas.  
Este archivo permite visualizar diferentes escenarios de ahorro programado, incluyendo abonos extra, seguimiento del total ahorrado y ajuste del valor mensual en caso de cambios.

**Enlace al documento:** [Ver hoja de cálculo](https://docs.google.com/spreadsheets/d/1LvZmssoXyPGCphXX650ifGW0w8BjKPEnsEZLR5gztD4/edit?usp=sharing)

