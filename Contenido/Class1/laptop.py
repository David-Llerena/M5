
class Laptop:
    def __init__(self, marca, procesador, memoria, costo = 500, impuesto = 10):
        self.marca = marca
        self.procesador = procesador   
        self.memoria = memoria
        self.costo = costo
        self.impuesto = impuesto

    def valor_final(self):
        return self.costo + self.impuesto
    
    def valor_descuento(self, descuento):
        return (self.costo *descuento)/100
    
laptop_pepito  = Laptop("HP", "Intel i5", "8GB")

print(laptop_pepito.__dict__)
print(laptop_pepito.valor_final())
print("El valor de descuento es:", laptop_pepito.valor_descuento(10))
