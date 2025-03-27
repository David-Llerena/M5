from laptop import Laptop
# from laptop_gaming import Laptop_Gaming

from laptop_business import Laptop_Business

laptop_pepito  = Laptop("HP", "Intel i5", "8GB")
laptop_maria = Laptop("Dell", "Intel i7", "16GB", 600, 20)

# print(laptop_pepito.__dict__)
# print(laptop_pepito.valor_final())
# print("El valor de descuento es:", laptop_pepito.valor_descuento(10))

# print(Laptop.comparar_costo(laptop_pepito, laptop_maria))
# asus_laptop = Laptop.asus_laptop()

# for numero in range (1,1001):
#     asus_laptop = Laptop.asus_laptop(numero)
#     print(asus_laptop.__dict__)


# laptop_juanito = Laptop_Gaming("HP", "Intel i5", "8GB", "GTX")   
# print(laptop_juanito.realizar_diagnostico_sistema) 


# Crear un objeto de tipo Laptop_Business
laptop_oficina = Laptop_Business("Lenovo", "Intel i7", "16GB", 1200, 10, "1TB SSD", 12)

# Ejecutar el diagnóstico del sistema
diagnostico = laptop_oficina.realizar_diagnostico_sistema()
print("Diagnóstico del sistema:", diagnostico)

# Verificar la conectividad de red
conectividad = laptop_oficina.verificar_conectividad_red()
print("Conectividad de red:", conectividad)