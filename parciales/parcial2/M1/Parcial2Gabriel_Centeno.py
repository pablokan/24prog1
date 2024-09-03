""""
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

class Producto:
    def __init__(self, tipo, color=None, precio=0, stock=0):
        self.tipo = tipo
        self.color = color
        self.precio = precio
        self.stock = stock

    def vender(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            return cantidad * self.precio
        else:
            print(f"No hay suficiente stock de {self.color or self.tipo}.")
            return 0

    def reponer_stock(self, cantidad):
        self.stock += cantidad


class Venta:
    def __init__(self):
        self.facturacion_total = 0

    def realizar_venta(self, producto, cantidad):
        facturacion = producto.vender(cantidad)
        self.facturacion_total += facturacion
        return facturacion

    def mostrar_facturacion(self):
        facturacion_formato = self.formatear_numero(self.facturacion_total)
        return facturacion_formato

    @staticmethod
    def formatear_numero(numero):
        return f"{numero:,.0f}".replace(",", ".")



class Tienda:
    def __init__(self):
        self.remeras_verdes = Producto(tipo="remera", color="verde", precio=15000, stock=100)
        self.remeras_negras = Producto(tipo="remera", color="negra", precio=15000, stock=100)
        self.camisas = Producto(tipo="camisa", precio=30000, stock=100)
        self.ventas = Venta()

    def vender_remeras(self, color, cantidad):
        if color == "verde":
            self.ventas.realizar_venta(self.remeras_verdes, cantidad)
        elif color == "negra":
            self.ventas.realizar_venta(self.remeras_negras, cantidad)
        self.mostrar_stock_mayor()
        self.mostrar_facturacion()

    def vender_camisas(self, cantidad):
        self.ventas.realizar_venta(self.camisas, cantidad)
        if self.camisas.stock < 20:
            print("COMPRAR CAMISAS URGENTE!")
            self.camisas.reponer_stock(100)
        self.mostrar_facturacion()

    def mostrar_stock_mayor(self):
        verdes = self.remeras_verdes.stock
        negras = self.remeras_negras.stock

        if verdes > negras:
            print("Me quedan más remeras verdes.")
        elif negras > verdes:
            print("Me quedan más remeras negras.")
        else:
            print("Me quedan la misma cantidad de remeras verdes y negras.")

    def mostrar_facturacion(self):
        facturacion_formato = self.ventas.mostrar_facturacion()
        print(f"Remeras: Verdes={self.remeras_verdes.stock}. Negras={self.remeras_negras.stock} / "
              f"Camisas={self.camisas.stock} / Facturación: ${facturacion_formato}")



tienda = Tienda()


tienda.vender_remeras("verde", 10)
tienda.vender_camisas(40)


tienda.vender_camisas(50)

tienda.vender_remeras("negra", 30)

    