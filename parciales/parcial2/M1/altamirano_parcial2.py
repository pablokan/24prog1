"""
Pablo Altamirano M1
Enunciado:

Tengo un negocio de ropa y quiero hacer un seguimiento de las ventas de remeras y camisas.

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
Me quedan más remeras verdes.

"""



class Negocio:
    def __init__(self):
        self.remerasVerdes = Remera("Verde")
        self.remerasNegras = Remera("Negra")

    def controlarStock(Self):
        if Self.Camisa.Stock < 20:
            print("Comprar URGENTE mas camisas")
            Self.Camisa.Stock += 100
    

    def realizarVenta (self, tipoDeRopa, cantidad):
        factura=0
        if tipoDeRopa == "remerasVerdes":
            factura += self.remerasVerdes.vender(cantidad)
        elif tipoDeRopa == "remerasNegras":
            factura += self.remerasNegras.verder(cantidad)
        elif tipoDeRopa == "Camisas":
            factura += self.Camisa.verder(cantidad)
        self.controlarStock()
        return factura
    
    def calcularFacturacion(self):
        return (self.remerasVerdes.Stock * 15000 + self.remerasNegras.Stock * 15000 + self.camisas.Stock * 30000)


class Ropa:
    def __init__(self, Pr, Stock):
        self.Precio = Pr
        self.Stock = Stock
    def vender(self, cantidad):
        if cantidad > self.Stock:
            print(f"No hay suficiente stock para verder {cantidad} unidades. Solo hay {self.stock}.")
        self.Stock -= cantidad
        return cantidad * self.precio

class Remera(Ropa):
    def __init__(self, Color, Stock=100):
        super().__init__(15000, Stock)
        self.color = Color

class Camisa(Ropa):
    def __init__(self, Stock=100):
        super().__init__(30000, Stock)

    
tienda = Negocio()
ventas = [
    ("remera_verde", 10),
    ("camisa", 40),
    ("camisa", 50),
    ("remera_negra", 30)]




