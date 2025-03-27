from laptop import Laptop

class Laptop_Gaming(Laptop):
    def _init_(self, marca, procesador, memoria, tarj_graf,costo = 500, impuesto = 10):
        super()._init_(marca, procesador, memoria, costo, impuesto)
        self.tarj_graf = tarj_graf
    def realizar_diagnostico_sistema(self):
        resultado_diagnostico = super().realizar_diagnostico_sistema()
        resultado_juego = self.realizar_diagnostico_juegos()
        resultado_diagnostico["Resultados Juegos"] = resultado_juego
        print(resultado_diagnostico)
        return resultado_diagnostico
    def realizar_diagnostico_juegos(self):
       juegos = ["Fornite","COD", "GTA"]
       resultado = {}
       for juego in juegos:
            fps_base = 30
            if "RTX" in self.tarj_graf:
                fps = fps_base * 3
            elif "GTX" in self.tarj_graf:
                fps = fps_base * 2
            else:
                fps = fps_base 
            resultado[juego] = f"{fps} FPS"
       return resultado
     
    pass