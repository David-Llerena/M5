from Biblioteca import Libro

# Crear instancias de libros
libro1 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 863)
libro2 = Libro("El Principito", "Antoine de Saint-Exupéry", 96)
libro3 = Libro("Cien años de soledad", "Gabriel García Márquez", 471)

# Mostrar información de los libros
print(libro1.mostrar_info())
print(libro2.mostrar_info())
print(libro3.mostrar_info())

# Verificar si los libros son grandes
print(f"¿Don Quijote es un libro grande? {Libro.es_grande(libro1.paginas)}")
print(f"¿El Principito es un libro grande? {Libro.es_grande(libro2.paginas)}")

# Mostrar el total de libros creados
print(f"Total de libros creados: {Libro.total_libros()}")