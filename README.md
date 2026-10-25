# 📊 Consolidador Automático de Reportes Financieros (`reporte_financiero.py`)

## 🎯 Descripción del Proyecto
Este script de automatización en Python (BPA - Business Process Automation) resuelve una tarea administrativa clave: consolidar múltiples reportes de ventas y gastos provenientes de diferentes sucursales (archivos CSV), procesarlos de forma masiva y calcular métricas gerenciales (ingresos, egresos y utilidad neta) para la toma de decisiones.

## 🛠️ Tecnologías Utilizadas
* **Lenguaje:** Python 3.14
* **Módulos Nativos:** `os` (gestión de directorios) y `csv` (lectura y escritura de datos tabulares).

## 🚀 Características
* **Generación de Datos de Prueba:** Incluye una función autónoma que crea archivos CSV simulados (`ventas_norte.csv`, `ventas_sur.csv`) si la carpeta está vacía, permitiendo validar la ejecución al instante.
* **Consolidación Masiva:** Agrupa dinámicamente todos los archivos de transacciones disponibles en el directorio de trabajo.
* **Análisis Financiero:** Calcula en tiempo real el total de ingresos, total de egresos y la utilidad neta, generando un reporte final consolidado (`reporte_consolidado_final.csv`).

## 💻 Instrucciones de Uso
1. Coloca tus archivos CSV con formato de transacciones en la carpeta del proyecto.
2. Ejecuta el script:
   ```bash
   python reporte_financiero.py