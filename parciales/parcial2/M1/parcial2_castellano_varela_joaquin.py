class Camisa():
    def __init__(self, stock) -> None:
        self.stock = stock
        self.precio = 30000
    
    def venta(self, cant):
        facturacion = 0
        if self.stock < cant:
            facturacion = self.precio * self.stock
            self.stock = 0
            print('ADVERTENCIA! No se realizo el total de la venta por falta de stock.')
        else:
            facturacion = self.precio * cant
            self.stock -= cant
        
        return facturacion

class Remera(Camisa):
    def __init__(self, stock, color) -> None:
        super().__init__(stock)
        self.color = color
        self.precio = 15000

class Tienda():
    def __init__(self) -> None:
        self.camisas = Camisa(100)
        self.remerasVerdes = Remera(100, 'Verdes')
        self.remerasNegras = Remera(100, 'Negras')

    def venta(self, cam, rV, rN):
        '''
        Metodo venta 
            Parametros:
            Cantidad a vender
                - cam: camisas
                - rV: remeras verdes
                - rN: remeras negras
        '''
        facturacion = self.camisas.venta(cam)
        facturacion += self.remerasVerdes.venta(rV)
        facturacion += self.remerasNegras.venta(rN)
        
        print(f'Remeras: {self.remerasVerdes.color}={self.remerasVerdes.stock}', end='. ')
        print(f'{self.remerasNegras.color}={self.remerasNegras.stock}', end=' / ')
        print(f'Camisas={self.camisas.stock}', end=' / ')
        print(f'Facturación: ${facturacion}')

        if self.remerasVerdes.stock > self.remerasNegras.stock:
            print('Me quedan más remeras verdes.')
        elif self.remerasVerdes.stock < self.remerasNegras.stock:
            print('Me quedan más remeras negras.')
        else:
            print('Me quedan la misma cantidad de remeras negras y verdes')
        
        if self.camisas.stock < 20:
            print('COMPRAR CAMISAS URGENTE!')
            self.camisas.stock += 100


t1 = Tienda()

t1.venta(40, 10, 0)

t1.venta(50, 0, 0)

t1.venta(0, 0, 30)
