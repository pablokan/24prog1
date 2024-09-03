class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def vender(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            return cantidad * self.precio
        else:
            print(f"No hay suficiente stock de {self.nombre}.")
            return 0

class Remera(Producto):
    def __init__(self, color, stock):
        super().__init__(f"Remera {color}", 15000, stock)
        self.color = color

class Camisa(Producto):
    def __init__(self, stock):
        super().__init__("Camisa", 30000, stock)

    def vender(self, cantidad):
        total = super().vender(cantidad)
        if self.stock < 20:
            print("COMPRAR CAMISAS URGENTE!")
            self.stock += 100  # Simula la compra automática de más camisas
        return total

class Tienda:
    def __init__(self):
        self.remerasVerdes = Remera("verde", 100)
        self.remerasNegras = Remera("negra", 100)
        self.camisas = Camisa(100)
        self.facturacion = 0

    def vender_remeras(self, color, cantidad):
        if color == "verde":
            self.facturacion += self.remerasVerdes.vender(cantidad)
        elif color == "negra":
            self.facturacion += self.remerasNegras.vender(cantidad)
        self.comparar_remeras()

    def vender_camisas(self, cantidad):
        self.facturacion += self.camisas.vender(cantidad)

    def comparar_remeras(self):
        if self.remerasVerdes.stock > self.remerasNegras.stock:
            print("Me quedan más remeras verdes.")
        elif self.remerasNegras.stock > self.remerasVerdes.stock:
            print("Me quedan más remeras negras.")
        else:
            print("Tengo la misma cantidad de remeras verdes y negras.")

    def mostrar_estado(self):
        print(f"Remeras: Verdes={self.remerasVerdes.stock}. Negras={self.remerasNegras.stock} / "
              f"Camisas={self.camisas.stock} / Facturación: ${self.facturacion}")

# Ejecución de las ventas
tienda = Tienda()

# 10 remeras verdes y 40 camisas
tienda.vender_remeras("verde", 10)
tienda.vender_camisas(40)
tienda.mostrar_estado()

# 50 camisas
tienda.vender_camisas(50)
tienda.mostrar_estado()

# 30 remeras negras
tienda.vender_remeras("negra", 30)
tienda.mostrar_estado()
