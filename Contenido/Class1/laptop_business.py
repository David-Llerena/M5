from laptop import Laptop
import random

class Laptop_Business(Laptop):
    def __init__(self, marca, procesador, ram, costo, descuento, almacenamiento, duracion_bateria):
        # Llamar al constructor de la clase base (Laptop)
        super().__init__(marca, procesador, ram, costo , descuento)
        # Atributos específicos de Laptop_Business
        self.almacenamiento = almacenamiento
        self.duracion_bateria = duracion_bateria

    def __str__(self):
        return (f"Laptop Business:\n"
                f"Marca: {self.marca}\n"
                f"Procesador: {self.procesador}\n"
                f"Memoria: {self.memoria}\n"
                f"Almacenamiento: {self.almacenamiento}\n"
                f"Precio: {self.costo}\n"
                f"Duración Batería: {self.duracion_bateria}\n")

    def realizar_diagnostico_sistema(self):
        # Obtener el diagnóstico básico de la clase base
        diagnostico_basico = super().realizar_diagnostico_sistema()
        # Añadir diagnósticos adicionales
        diagnostico_adicional = {
            "almacenamiento": f"{self.almacenamiento} disponibles",
            "duracion_bateria": f"{self.duracion_bateria} horas de batería"
        }
        # Combinar ambos diagnósticos
        diagnostico_completo = {**diagnostico_basico, **diagnostico_adicional}
        return diagnostico_completo

    def verificar_conectividad_red(self):
        # Simular comprobaciones de conectividad de red
        conectividad = {
            "wifi_disponible": random.choice([True, False]),
            "acceso_servidores_empresariales": random.choice([True, False]),
            "latencia_red": random.randint(10, 100)  # Latencia simulada en ms
        }
        return conectividad
    