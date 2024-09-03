class Remera:
    def __init__(self, venderCantV, venderCantN) -> None:
        self.precio = 15000
        self.stockV = 100
        self.stockN = 100
        self.venderCantV = venderCantV
        self.venderCantN = venderCantN

        if self.stockN > self.stockV:
            print("Me quedan mas remeras negras")
        else:
            print("Me quedan mas remeras verdes")

    def actualizarStock(self):
        self.stockV -= self.venderCantV
        self.stockN -= self.venderCantN
    

class Camisa:
    def __init__(self, cant) -> None:
        self.precio = 30000
        self.stock = 100
        self.cant = cant

        if self.stock < 20:
            print("Quedan menos de 20 unidades.")
            self.stock += 20
    
    def actualizarStock(self):
        self.stock -= self.cant

class Tienda:
    def __init__(self, remerasV, remerasN, camisas) -> None:
        self.remerasV = remerasV
        self.remerasN = remerasN
        self.camisas = camisas
        
        ventaRemeras = Remera(remerasV, remerasN)
        ventaRemeras.actualizarStock()
        
        facturacionRemeras = ventaRemeras.precio * (remerasV + remerasN)

        ventaCamisas = Camisa(camisas)
        ventaCamisas.actualizarStock()
        facturacionCamisas = ventaCamisas.precio * camisas

        facturacionTotal = facturacionRemeras + facturacionCamisas

        print(f"Remeras: Verdes={ventaRemeras.stockV}. Negras: {ventaRemeras.stockN}. Camisas: {ventaCamisas.stock}. Facturacion: {facturacionTotal}")


venta = Tienda(10, 0, 40)
print(" ")
venta = Tienda(0, 0, 50)
print(" ")
venta = Tienda(0, 30 , 0)

# No supe lograr mantener el stock anterior luego de cada ejecucion, por lo que siempre resta desde el stock inicial