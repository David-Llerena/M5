from laptop import Laptop

laptop_pepito  = Laptop("HP", "Intel i5", "8GB")
laptop_maria = Laptop("Dell", "Intel i7", "16GB", 600, 20)

# print(laptop_pepito.__dict__)
# print(laptop_pepito.valor_final())
# print("El valor de descuento es:", laptop_pepito.valor_descuento(10))

# print(Laptop.comparar_costo(laptop_pepito, laptop_maria))
# asus_laptop = Laptop.asus_laptop()

for numero in range (1,1001):
    asus_laptop = Laptop.asus_laptop(numero)
    print(asus_laptop.__dict__)


