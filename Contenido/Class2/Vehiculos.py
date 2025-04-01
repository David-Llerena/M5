class Vehiculo:
    def __init__(self, marca, modelo, anio):
        """
        Constructor de la clase base Vehiculo
        
        Args:
            marca (str): Marca del vehículo
            modelo (str): Modelo del vehículo
            anio (int): Año de fabricación
        """
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
    
    def descripcion(self):
        """
        Método de instancia que muestra la información del vehículo
        
        Returns:
            str: Cadena con la información del vehículo
        """
        return f"Vehículo {self.marca} {self.modelo}, año {self.anio}"


class Auto(Vehiculo):
    def __init__(self, marca, modelo, anio, num_puertas):
        """
        Constructor de la subclase Auto
        
        Args:
            marca (str): Marca del vehículo
            modelo (str): Modelo del vehículo
            anio (int): Año de fabricación
            num_puertas (int): Número de puertas del auto
        """
        # Llamar al constructor de la clase padre
        super().__init__(marca, modelo, anio)
        self.num_puertas = num_puertas
    
    def descripcion(self):
        """
        Método sobrescrito que muestra la información del auto
        
        Returns:
            str: Cadena con la información del auto incluyendo número de puertas
        """
        return f"Auto {self.marca} {self.modelo}, año {self.anio}, {self.num_puertas} puertas"


class Moto(Vehiculo):
    def __init__(self, marca, modelo, anio, tipo):
        """
        Constructor de la subclase Moto
        
        Args:
            marca (str): Marca del vehículo
            modelo (str): Modelo del vehículo
            anio (int): Año de fabricación
            tipo (str): Tipo de moto (deportiva, scooter, etc.)
        """
        # Llamar al constructor de la clase padre
        super().__init__(marca, modelo, anio)
        self.tipo = tipo
    
    def descripcion(self):
        """
        Método sobrescrito que muestra la información de la moto
        
        Returns:
            str: Cadena con la información de la moto incluyendo el tipo
        """
        return f"Moto {self.marca} {self.modelo}, año {self.anio}, tipo {self.tipo}"