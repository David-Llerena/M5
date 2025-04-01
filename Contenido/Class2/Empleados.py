from abc import ABC, abstractmethod

class Empleado(ABC):
    """
    Clase abstracta que representa a un empleado genérico.
    """
    
    def __init__(self, nombre, salario_base):
        """
        Constructor de la clase Empleado
        
        Args:
            nombre (str): Nombre del empleado
            salario_base (float): Salario mensual base
        """
        self.nombre = nombre
        self.salario_base = salario_base
    
    @abstractmethod
    def calcular_salario(self):
        """
        Método abstracto que debe ser implementado en las subclases.
        Calcula el salario final del empleado.
        
        Returns:
            float: Salario final con bonos aplicados
        """
        pass
    
    def __str__(self):
        """
        Representación en string del empleado
        
        Returns:
            str: Información del empleado
        """
        return f"Empleado: {self.nombre}, Salario Base: ${self.salario_base:.2f}"


class EmpleadoTiempoCompleto(Empleado):
    """
    Subclase que representa a un empleado de tiempo completo.
    """
    
    def __init__(self, nombre, salario_base):
        """
        Constructor de la clase EmpleadoTiempoCompleto
        
        Args:
            nombre (str): Nombre del empleado
            salario_base (float): Salario mensual base
        """
        super().__init__(nombre, salario_base)
    
    def calcular_salario(self):
        """
        Implementación del método para calcular el salario de un empleado
        de tiempo completo, aplicando un bono del 20%.
        
        Returns:
            float: Salario con bono del 20%
        """
        bono = self.salario_base * 0.20
        return self.salario_base + bono
    
    def __str__(self):
        """
        Representación en string del empleado de tiempo completo
        
        Returns:
            str: Información del empleado de tiempo completo
        """
        return f"Empleado Tiempo Completo: {self.nombre}, Salario Base: ${self.salario_base:.2f}, Salario Final: ${self.calcular_salario():.2f}"


class EmpleadoMedioTiempo(Empleado):
    """
    Subclase que representa a un empleado de medio tiempo.
    """
    
    def __init__(self, nombre, salario_base):
        """
        Constructor de la clase EmpleadoMedioTiempo
        
        Args:
            nombre (str): Nombre del empleado
            salario_base (float): Salario mensual base
        """
        super().__init__(nombre, salario_base)
    
    def calcular_salario(self):
        """
        Implementación del método para calcular el salario de un empleado
        de medio tiempo, aplicando un bono del 10%.
        
        Returns:
            float: Salario con bono del 10%
        """
        bono = self.salario_base * 0.10
        return self.salario_base + bono
    
    def __str__(self):
        """
        Representación en string del empleado de medio tiempo
        
        Returns:
            str: Información del empleado de medio tiempo
        """
        return f"Empleado Medio Tiempo: {self.nombre}, Salario Base: ${self.salario_base:.2f}, Salario Final: ${self.calcular_salario():.2f}"

