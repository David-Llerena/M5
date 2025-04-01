from Empleados import EmpleadoTiempoCompleto
from Empleados import EmpleadoMedioTiempo
def main():
    print("SISTEMA DE GESTIÓN DE EMPLEADOS")
    print("===============================\n")
    
    # Crear un empleado de tiempo completo y uno de medio tiempo
    print("1. Creando empleados:")
    empleado_tc = EmpleadoTiempoCompleto("María López", 2500)
    empleado_mt = EmpleadoMedioTiempo("Juan Pérez", 1500)
    
    # Mostrar el salario final de cada empleado
    print("\n2. Salarios finales individuales:")
    print(f"- {empleado_tc}")
    print(f"  Salario Final: ${empleado_tc.calcular_salario():.2f} (incluye bono del 20%)")
    
    print(f"- {empleado_mt}")
    print(f"  Salario Final: ${empleado_mt.calcular_salario():.2f} (incluye bono del 10%)")
    
    # Usar una lista de empleados para demostrar el polimorfismo
    print("\n3. Demostración de polimorfismo con lista de empleados:")
    empleados = [
        EmpleadoTiempoCompleto("Carlos Rodríguez", 3000),
        EmpleadoMedioTiempo("Ana González", 1800),
        EmpleadoTiempoCompleto("Luis Martínez", 2800),
        EmpleadoMedioTiempo("Laura Sánchez", 1600),
        empleado_tc,
        empleado_mt
    ]
    
    print("Lista de todos los empleados con sus salarios finales:")
    for i, emp in enumerate(empleados, 1):
        # Usamos polimorfismo: el mismo método calcular_salario() 
        # se comporta de forma diferente según la clase del objeto
        salario_final = emp.calcular_salario()
        print(f"  {i}. {emp.nombre} - Salario Base: ${emp.salario_base:.2f}, Salario Final: ${salario_final:.2f}")
    
    # Calcular y mostrar estadísticas de salarios
    print("\n4. Estadísticas de salarios:")
    total_salarios = sum(emp.calcular_salario() for emp in empleados)
    promedio_salarios = total_salarios / len(empleados)
    max_salario = max(empleados, key=lambda x: x.calcular_salario())
    min_salario = min(empleados, key=lambda x: x.calcular_salario())
    
    print(f"- Total de salarios: ${total_salarios:.2f}")
    print(f"- Promedio de salarios: ${promedio_salarios:.2f}")
    print(f"- Salario más alto: ${max_salario.calcular_salario():.2f} ({max_salario.nombre})")
    print(f"- Salario más bajo: ${min_salario.calcular_salario():.2f} ({min_salario.nombre})")
    
    print("\nNota: El polimorfismo nos permite llamar al mismo método 'calcular_salario()' ")
    print("      para diferentes tipos de empleados, obteniendo el resultado correcto ")
    print("      según la implementación específica de cada subclase.")


# Ejecutar el programa principal
if __name__ == "__main__":
    main()