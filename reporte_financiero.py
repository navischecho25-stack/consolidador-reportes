import os
import csv

def generar_datos_prueba():
    """Crea archivos CSV de prueba simulando sucursales de un negocio."""
    print("🛠️ Generando archivos de datos de prueba...")
    
    sucursal_norte = [
        ["Fecha", "Concepto", "Tipo", "Valor"],
        ["2026-10-01", "Venta de mercancía", "Ingreso", 1500000],
        ["2026-10-02", "Pago de servicios", "Egreso", 300000],
        ["2026-10-03", "Venta de mercancía", "Ingreso", 2200000]
    ]
    
    sucursal_sur = [
        ["Fecha", "Concepto", "Tipo", "Valor"],
        ["2026-10-01", "Venta de mercancía", "Ingreso", 900000],
        ["2026-10-02", "Mantenimiento equipos", "Egreso", 200000],
        ["2026-10-04", "Venta de mercancía", "Ingreso", 1800000]
    ]
    
    with open("ventas_norte.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(sucursal_norte)
        
    with open("ventas_sur.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(sucursal_sur)
        
    print("✅ Archivos 'ventas_norte.csv' y 'ventas_sur.csv' creados con éxito.")

def consolidar_reportes():
    # Asegurarnos de tener datos para procesar
    if not os.path.exists("ventas_norte.csv") or not os.path.exists("ventas_sur.csv"):
        generar_datos_prueba()
        
    print("\n📊 Iniciando consolidación y análisis de reportes...")
    
    archivos_csv = [f for f in os.listdir(".") if f.endswith(".csv") and f != "reporte_consolidado_final.csv"]
    
    todas_las_transacciones = []
    
    for archivo in archivos_csv:
        print(f"📂 Leyendo datos de: {archivo}")
        with open(archivo, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            encabezados = next(reader) # Leer la cabecera
            for fila in reader:
                todas_las_transacciones.append(fila)
                
    # Procesar y calcular métricas financieras básicas
    total_ingresos = 0
    total_egresos = 0
    
    for fila in todas_las_transacciones:
        tipo = fila[2]
        valor = float(fila[3])
        if tipo == "Ingreso":
            total_ingresos += valor
        elif tipo == "Egreso":
            total_egresos += valor
            
    utilidad_neta = total_ingresos - total_egresos
    
    # Escribir el reporte consolidado final
    nombre_reporte = "reporte_consolidado_final.csv"
    with open(nombre_reporte, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Fecha", "Concepto", "Tipo", "Valor"])
        writer.writerows(todas_las_transacciones)
        
    print("\n" + "="*40)
    print("📈 RESUMEN FINANCIERO GERENCIAL")
    print("="*40)
    print(f"💰 Total Ingresos: $ {total_ingresos:,.2f}")
    print(f"💸 Total Egresos:  $ {total_egresos:,.2f}")
    print(f"⚖️ Utilidad Neta:  $ {utilidad_neta:,.2f}")
    print("="*40)
    print(f"✅ Reporte consolidado guardado exitosamente en: {nombre_reporte}")

if __name__ == "__main__":
    consolidar_reportes()