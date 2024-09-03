""""Importante: 

Respetar la consigna, pero sobre todo, 

incluir los conceptos principales de orientación a objetos trabajados:

HERENCIA y COMPOSICIÓN 

Subir el programa resuelto hasta un minuto antes de la hora especificada. 

Estará DESHABILITADA LA OPCIÓN DE SUBIR EL PROGRAMA FUERA DE HORA.

Se sube el programa con lo mucho o poco que se haya podido escribir!


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

class Ropa:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def vender(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            return self.precio * cantidad
        else:
            print(f"no hay suficiente stock de {self.nombre}")
            return 0


class Remera(Ropa):
    def __init__(self, color, stock):
        super().__init__(f"remera {color}", 15000, stock)
        self.color = color


class Camisa(Ropa):
    def __init__(self, stock):
        super().__init__("camisa", 30000, stock)

    def vender(self, cantidad):
        total = super().vender(cantidad)
        if self.stock < 20:
            print("Quedan menos de 20 camisas en stock. se van a anadir 100 camisas al inventario")
            self.stock += 100
        return total


class Tienda:
    def __init__(self):
        self.remeras_verdes = Remera("verde", 100)
        self.remeras_negras = Remera("negra", 100)
        self.camisas = Camisa(100)
        self.facturacion = 0

    def vender_remeras(self, color, cantidad):
        if color == "verde":
            self.facturacion += self.remeras_verdes.vender(cantidad)
        elif color == "negra":
            self.facturacion += self.remeras_negras.vender(cantidad)
        else:
            print("Color no válido.")
        self.mostrar_stock()
        self.mostrar_mayoria_remeras()

    def vender_camisas(self, cantidad):
        self.facturacion += self.camisas.vender(cantidad)
        self.mostrar_stock()

    def mostrar_stock(self):
        print(f"Remeras: Verdes={self.remeras_verdes.stock}. Negras={self.remeras_negras.stock} / Camisas={self.camisas.stock} / Facturación: ${self.facturacion}")

    def mostrar_mayoria_remeras(self):
        if self.remeras_verdes.stock > self.remeras_negras.stock:
            print("me quedan más remeras verdes")
        elif self.remeras_negras.stock > self.remeras_verdes.stock:
            print("me quedan más remeras negras")
        else:
            print ('hay la misma cantidad')



tienda = Tienda()

tienda.vender_remeras("verde", 10)
tienda.vender_camisas(40)
tienda.vender_camisas(50)
tienda.vender_remeras("negra", 30)