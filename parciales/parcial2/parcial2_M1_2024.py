class Prenda:
    def __init__(self, stock, precio):
        self.stock = stock
        self.precio = precio

    def vender(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            return cantidad * self.precio
        else:
            return 0

class Remera(Prenda):
    def __init__(self, stock, precio, color):
        super().__init__(stock, precio)
        self.color = color

class Tienda:
    def __init__(self):
        self.remeraVerde = Remera(100, 15000, "verde")
        self.remeraNegra = Remera(100, 15000, "negra")
        self.camisa = Prenda(100, 30000)
        self.facturacion = 0

    def alertaCamisas(self):
        if self.camisa.stock < 20:
            print("COMPRAR CAMISAS URGENTE!")
            self.camisa.stock += 100

    def compararRemeras(self):
        if self.remeraVerde.stock > self.remeraNegra.stock:
            return "Me quedan más remeras verdes."
        elif self.remeraNegra.stock > self.remeraVerde.stock:
            return "Me quedan más remeras negras."
        else:
            return "Tengo la misma cantidad de remeras verdes y negras."

    def realizarVenta(self, cantidadRemerasVerdes, cantidadRemerasNegras, cantidadCamisas):
        self.facturacion = self.remeraVerde.vender(cantidadRemerasVerdes)
        self.facturacion += self.remeraNegra.vender(cantidadRemerasNegras)
        self.facturacion += self.camisa.vender(cantidadCamisas)
        
        print(f"Remeras: Verdes={self.remeraVerde.stock}. Negras={self.remeraNegra.stock} / Camisas={self.camisa.stock} / Facturación: ${self.facturacion}")
        print(self.compararRemeras())
        self.alertaCamisas()
        print()

tienda = Tienda()

tienda.realizarVenta(10, 0, 40)
tienda.realizarVenta(0, 0, 50)
tienda.realizarVenta(0, 30, 0)
