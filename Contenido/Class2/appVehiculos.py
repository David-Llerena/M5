from Vehiculos import Vehiculo
from Vehiculos import Auto
from Vehiculos import Moto  
# Clase de Prueba
def main():
    print("PRUEBA DE CLASES DE VEHÍCULOS")
    print("=============================\n")
    
    # Crear un objeto de cada tipo (Auto y Moto)
    print("1. Creando objetos de cada tipo:")
    auto = Auto("Toyota", "Corolla", 2023, 4)
    moto = Moto("Yamaha", "YZF", 2022, "deportiva")
    
    # Mostrar la descripción de ambos vehículos
    print("\n2. Mostrando descripción de cada vehículo:")
    print(f"- {auto.descripcion()}")
    print(f"- {moto.descripcion()}")
    
    # Crear una lista con autos y motos para demostrar polimorfismo
    print("\n3. Demostrando polimorfismo con una lista mixta:")
    vehiculos = [
        Auto("Ford", "Mustang", 2023, 2),
        Moto("Honda", "CB500", 2021, "naked"),
        Auto("Volkswagen", "Golf", 2022, 5),
        Moto("Ducati", "Monster", 2023, "deportiva"),
        Auto("Tesla", "Model 3", 2023, 4)
    ]
    
    # Recorrer la lista y llamar al método descripcion() para mostrar polimorfismo
    print("Lista de vehículos diversos:")
    for i, vehiculo in enumerate(vehiculos, 1):
        print(f"  {i}. {vehiculo.descripcion()}")
    
    print("\nNota: El polimorfismo permite llamar al mismo método 'descripcion()' ")
    print("      en objetos de diferentes clases, obteniendo el comportamiento ")
    print("      específico de cada subclase.")

# Ejecutar la prueba
if __name__ == "__main__":
    main()