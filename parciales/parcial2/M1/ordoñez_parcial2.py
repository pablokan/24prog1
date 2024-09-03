'''
Tengo un negocio de ropa y quiero hacer un seguimiento de las ventas de remeras y camisas.

Hay dos tipos de remeras, verdes y negras. Todas valen $15000. 

Las camisas son todas iguales, con un precio unitario de $30000.

Cuando comencé con la tienda, arranqué con un stock inicial de 100 remeras de cada color y también 100 camisas.

Con respecto al stock: 
camisas: me preocupa quedarme sin camisas para vender por lo que implementé que se lance un aviso cuando me queden menos de 20 unidades. Dicho aviso
se debe disparar al realizar una venta. Y automáticamente le sumo 100 al stock de camisas (simulo una compra solamente, no hace falta un método)
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

'''

class Ropa():
    def __init__(self) -> None:
        pass

class Remeras(Ropa):

    def negras(self, cantidad):
        self.cantidad = cantidad
        self.precio = 15000
        self.stock = 100

        if self.cantidad <= 100:
            cantStock = self.stock - self.cantidad  
            total = self.cantidad * self.precio
            print(f"Remeras negras restantes: {cantStock}, Total vendido: {total} ")        

    def verdes(self, cantidad):
        self.cantidad = cantidad
        self.precio = 15000
        self.stock = 100

        if self.cantidad <= 100:
            cantStock = self.stock - self.cantidad  
            total = self.cantidad * self.precio
            print(f"Remeras verdes restantes: {cantStock}, Total vendido: {total} ")
        

class Camisas(Ropa):
   
    def camisaComun (self, cantidad):
        self.cantidad = cantidad
        self.precio = 30000
        self.stock = 100

        if self.cantidad <= 100:
            cantStock = self.stock - self.cantidad  
            total = self.cantidad * self.precio
            print(f"Camisas restantes: {cantStock}, Total vendido: {total} ")

ropa = Ropa()
camisa = Camisas()
remeras = Remeras()

remeras.verdes(10)
camisa.camisaComun(40)

camisa.camisaComun(50)

remeras.negras(30)