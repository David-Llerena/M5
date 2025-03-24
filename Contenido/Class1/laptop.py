
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
    
    @staticmethod
    def comparar_costo(laptop1, laptop2):
        if laptop1.costo == laptop2.costo:
            return "Ambas laptops tienen el mismo costo"
        else: 
            return "Las laptops tienen diferentes costos"  
    @classmethod
    def asus_laptop(cls, costo):
       marca = "Asus"
       procesador = "Intel i7"
       memoria = "16GB"
       return cls(marca, procesador, memoria,costo)
