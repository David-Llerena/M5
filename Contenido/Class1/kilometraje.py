from datetime import datetime
class Auto:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.kilometraje = 0

    def mostrar_información(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")

    def actualizar_kilometraje(self, kilometraje):
        if kilometraje >= self.kilometraje:
            self.kilometraje = kilometraje
        else:
            print("No se puede reducir el kilometraje.")

    def realizar_viaje(self, kilometros):
        if kilometros > 0:
            self.kilometraje += kilometros
        else:
            print("La cantidad de kilómetros debe ser positiva.")

    def estado_auto(self):
        if self.kilometraje < 20000:
            print("Estoy como nuevo")
        elif 20000 <= self.kilometraje <= 100000:
            print("Ya estoy usado")
        else:
            print("¡Ya déjame descansar por favor!")

    # reto 7
    @classmethod
    def crear_auto_toyota_nuevo(cls):
        """
        Método de clase para crear un nuevo Toyota del año actual
        """
        año_actual = datetime.now().year
        return cls("Toyota", "Modelo Genérico", año_actual)

    @staticmethod
    def comparar_kilometraje(auto1, auto2):
        """
        Método estático para comparar el kilometraje de dos autos
        """
        if auto1.kilometraje == auto2.kilometraje:
            print("Los autos tienen el mismo kilometraje")
            return True
        else:
            print("Los autos tienen diferente kilometraje")
            return False

    @staticmethod
    def calcular_impuesto_por_kilometraje(auto):
        """
        Método estático adicional para calcular un impuesto hipotético 
        basado en el kilometraje
        """
        if auto.kilometraje < 20000:
            return 0  # Exento
        elif 20000 <= auto.kilometraje <= 50000:
            return auto.kilometraje * 0.01  # 1% de impuesto
        else:
            return auto.kilometraje * 0.02  # 2% de impuesto

    @classmethod
    def crear_flota_autos(cls, cantidad):
        """
        Método de clase para crear una flota de autos Toyota nuevos
        """
        return [cls.crear_auto_toyota_nuevo() for _ in range(cantidad)]
        

# Ejemplo de uso
mi_auto = Auto("Toyota", "Corolla", 2020)
mi_auto.mostrar_información()
print(f"\nKilometraje inicial: {mi_auto.kilometraje} km")

mi_auto.actualizar_kilometraje(15000)
print(f"Kilometraje después de actualizar: {mi_auto.kilometraje} km")

mi_auto.realizar_viaje(10000)
print(f"Kilometraje después del viaje: {mi_auto.kilometraje} km")

mi_auto.estado_auto()