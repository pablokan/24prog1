"""Tengo un negocio de ropa y quiero hacer un seguimiento de las ventas de remeras y camisas.

Hay dos tipos de remeras, verdes y negras. Todas valen $15000. 

Las camisas son todas iguales, con un precio unitario de $30000.

Cuando comencé con la tienda, arranqué con un stock inicial de 100 remeras de cada color y también 100 camisas.

Con respecto al stock: 
camisas: me preocupa quedarme sin camisas para vender por lo que implementé que se lance un aviso cuando me queden menos de 20 unidades. Dicho aviso se debe disparar al realizar una venta. Y automáticamente le sumo 100 al stock de camisas (simulo una compra solamente, no hace falta un método)
remeras: siempre quiero saber de qué color tengo la mayor cantidad para decidir si las pongo en oferta.

Quiero realizar las siguientes ventas:

10 remeras verdes y 40 camisas
50 camisas
30 remeras negras

Salida esperada (luego de cada venta):

Remeras: Verdes=90. Negras=100 / Camisas=60 / Facturación: $1.350.000
Me quedan más remeras negras.
Remeras: Verdes=90. Negras=100 / Camisas=10 / Facturación: $1.500.000
Me quedan más remeras negras.
COMPRAR CAMISAS URGENTE!
Remeras: Verdes=90. Negras=70 / Camisas=110 / Facturación: $450.000
Me quedan más remeras verdes."""

class Tienda():
    def __init__(self, nombre) -> None:
        self.nombre = nombre
        self.listaPrendas = ["camisa", "remera"]

    def agProductos(self):
        hayMas = "s"
        while hayMas == "s":
            prenda = input("que prenda desea agregar: ")
            if prenda in self.listaPrendas[0]:
                prenda = Camisa(100, prenda, 30000)
                hayMas = input("desea agregar mas?: ")
            else:
                color = input("de que color?: ")
                if color == "negro":
                    prenda = Remera(100, prenda, 15000, color)      # estoy fallando acaa, y capaz en todo pero aca pasa algo raro
                    hayMas = input("desea agregar mas?: ")
                elif color == "verde":
                    prenda = Remera(100, prenda, 15000, color)
                    hayMas = input("desea agregar mas?: ")
                else:
                    pass

    def vender(self):
        pass

class Ropa():
    def __init__(self, stock, prenda) -> None:
        self.stock = stock
        self.prenda = prenda

class Remera(Ropa):
    def __init__(self, stock, prenda, precio, color):
        super().__init__(stock, prenda)
        self.precio = precio
        self.color = color
        remNegra = 100
        remVerde = 100
        if self.color == "negro":
            remNegra += 1
        else:
            remVerde += 1
        if remVerde > remNegra:
            print("Me quedan mas remeras verdes")
        elif remVerde < remNegra:
            print("Me quedan mas remeras negras")
        else:
            pass
        return f"remeras negras: {remNegra}, remeras verdes: {remVerde}"
        
class Camisa(Ropa):
    def __init__(self, stock, prenda, precio) -> None:
        super().__init__(stock, prenda)
        self.precio = precio
        self.stock = stock
        if self.stock <= 20:
            print("COMPRAR CAMISAS URGENTE")
            self.stock += 100
        else:
            pass

tienda1 = Tienda("adidas")
tienda1.agProductos()