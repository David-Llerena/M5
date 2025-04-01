class Libro:
    # Variable de clase para contar libros
    contador_libros = 0
    
    def __init__(self, titulo, autor, paginas):
        """
        Constructor de la clase Libro
        
        Args:
            titulo (str): El título del libro
            autor (str): El nombre del autor
            paginas (int): El número de páginas del libro
        """
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        
        # Incrementar contador de libros
        Libro.contador_libros += 1
    
    def mostrar_info(self):
        """
        Método de instancia que muestra la información del libro
        
        Returns:
            str: Cadena con la información del libro
        """
        return f"Título: {self.titulo}, Autor: {self.autor}, Páginas: {self.paginas}"
    
    @staticmethod
    def es_grande(paginas):
        """
        Método estático que determina si un libro es grande
        
        Args:
            paginas (int): Número de páginas a evaluar
            
        Returns:
            bool: True si tiene más de 300 páginas, False en caso contrario
        """
        return paginas > 300
    
    @classmethod
    def total_libros(cls):
        """
        Método de clase que retorna la cantidad de libros creados
        
        Returns:
            int: Cantidad de libros creados
        """
        return cls.contador_libros
    
    
