import pandas as pd
import numpy as np

# Archivo: test.py
# Resolución de los 15 ejercicios específicos de análisis de ventas

# Crear el dataframe con los datos proporcionados
data = {
    'Producto': [f'Producto {i}' for i in range(1, 21)],
    'Cantidad_Vendida': [30, 20, 50, 15, 10, 25, 40, 35, 45, 50, 60, 30, 25, 40, 55, 35, 45, 50, 60, 30],
    'Precio_Unitario': [50, 70, 20, 100, 150, 200, 30, 120, 60, 90, 110, 80, 50, 150, 60, 70, 100, 120, 80, 150],
    'Descuento_Porcentaje': [10, 5, 15, 20, 25, 10, 0, 5, 20, 30, 15, 10, 5, 0, 10, 10, 20, 15, 10, 25],
    'Costo_Produccion': [20, 30, 10, 40, 60, 80, 15, 50, 25, 35, 45, 30, 20, 60, 25, 35, 45, 50, 40, 55]
}

# Crear DataFrame
df = pd.DataFrame(data)

print("-" * 60)
print("RESOLUCIÓN DE EJERCICIOS DE ANÁLISIS DE VENTAS")
print("-" * 60)

# Ejercicio 1: Seleccionar columnas específicas
print("\nEjercicio 1: Selección de columnas específicas")
columnas_seleccionadas = df[['Producto', 'Cantidad_Vendida', 'Precio_Unitario', 'Descuento_Porcentaje', 'Costo_Produccion']]
print(columnas_seleccionadas.head())  # Mostramos solo las 5 primeras filas

# Ejercicio 2: Cálculo del Ingreso Total por Producto
print("\nEjercicio 2: Cálculo del Ingreso Total por Producto")
df['Precio_con_Descuento'] = df['Precio_Unitario'] * (1 - df['Descuento_Porcentaje']/100)
df['Ingreso_Total'] = df['Cantidad_Vendida'] * df['Precio_con_Descuento']
print(df[['Producto', 'Cantidad_Vendida', 'Precio_Unitario', 'Descuento_Porcentaje', 'Precio_con_Descuento', 'Ingreso_Total']].head())

# Ejercicio 3: Cálculo del Ingreso Total Global
print("\nEjercicio 3: Cálculo del Ingreso Total Global")
ingreso_total_global = df['Ingreso_Total'].sum()
print(f"Ingreso Total Global: ${ingreso_total_global:.2f}")

# Ejercicio 4: Cálculo del Costo Total de Producción
print("\nEjercicio 4: Cálculo del Costo Total de Producción por Producto")
df['Costo_Total_Produccion'] = df['Cantidad_Vendida'] * df['Costo_Produccion']
print(df[['Producto', 'Cantidad_Vendida', 'Costo_Produccion', 'Costo_Total_Produccion']].head())

# Ejercicio 5: Cálculo de la Ganancia Bruta por Producto
print("\nEjercicio 5: Cálculo de la Ganancia Bruta por Producto")
df['Ganancia_Bruta'] = df['Ingreso_Total'] - df['Costo_Total_Produccion']
print(df[['Producto', 'Ingreso_Total', 'Costo_Total_Produccion', 'Ganancia_Bruta']].head())

# Ejercicio 6: Cálculo de la Ganancia Bruta Total
print("\nEjercicio 6: Cálculo de la Ganancia Bruta Total")
ganancia_bruta_total = df['Ganancia_Bruta'].sum()
print(f"Ganancia Bruta Total: ${ganancia_bruta_total:.2f}")

# Ejercicio 7: Cálculo del Ingreso Promedio por Producto
print("\nEjercicio 7: Cálculo del Ingreso Promedio por Producto")
ingreso_promedio = ingreso_total_global / len(df)
print(f"Ingreso Promedio por Producto: ${ingreso_promedio:.2f}")

# Ejercicio 8: Cálculo del Precio Promedio por Producto
print("\nEjercicio 8: Cálculo del Precio Promedio por Producto")
precio_promedio = df['Precio_Unitario'].mean()
print(f"Precio Promedio por Producto: ${precio_promedio:.2f}")

# Ejercicio 9: Identificar el Producto Más Rentable (mayor ingreso)
print("\nEjercicio 9: Identificar el Producto con Mayor Ingreso")
producto_mayor_ingreso = df.loc[df['Ingreso_Total'].idxmax()]
print(f"Producto con Mayor Ingreso: {producto_mayor_ingreso['Producto']}")
print(f"Ingreso Total: ${producto_mayor_ingreso['Ingreso_Total']:.2f}")

# Ejercicio 10: Identificar el Producto con Mayor Ganancia Bruta
print("\nEjercicio 10: Identificar el Producto con Mayor Ganancia Bruta")
producto_mayor_ganancia = df.loc[df['Ganancia_Bruta'].idxmax()]
print(f"Producto con Mayor Ganancia Bruta: {producto_mayor_ganancia['Producto']}")
print(f"Ganancia Bruta: ${producto_mayor_ganancia['Ganancia_Bruta']:.2f}")

# Ejercicio 11: Suma de Cantidades Vendidas
print("\nEjercicio 11: Suma de Cantidades Vendidas")
total_cantidades = df['Cantidad_Vendida'].sum()
print(f"Total de Unidades Vendidas: {total_cantidades}")

# Ejercicio 12: Promedio de Descuento por Producto
print("\nEjercicio 12: Promedio de Descuento por Producto")
descuento_promedio = df['Descuento_Porcentaje'].mean()
print(f"Descuento Promedio: {descuento_promedio:.2f}%")

# Ejercicio 13: Suma de Costos de Producción
print("\nEjercicio 13: Suma de Costos de Producción Total")
costos_produccion_total = df['Costo_Total_Produccion'].sum()
print(f"Costo Total de Producción: ${costos_produccion_total:.2f}")

# Ejercicio 14: Porcentaje de Ingreso Total sobre el Costo Total de Producción
print("\nEjercicio 14: Porcentaje de Ingreso Total sobre el Costo Total de Producción")
porcentaje_ingreso_sobre_costo = (ingreso_total_global / costos_produccion_total) * 100
print(f"Porcentaje de Ingreso Total sobre Costo Total: {porcentaje_ingreso_sobre_costo:.2f}%")

# Ejercicio 15: Cálculo de la Rentabilidad de la Tienda
print("\nEjercicio 15: Cálculo de la Rentabilidad de la Tienda")
rentabilidad_tienda = (ganancia_bruta_total / ingreso_total_global) * 100
print(f"Rentabilidad de la Tienda: {rentabilidad_tienda:.2f}%")

