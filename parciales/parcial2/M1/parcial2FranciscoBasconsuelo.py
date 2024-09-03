class TiendaRopa:
    def __init__(self):
        self.stock = {"remeras verdes":100}
        self.stock = {"remeras negras":100}
        self.stock = {"camisas":100}
        
        self.precios = {"remeras verdes":15000}
        self.precios = {"remeras negras":15000}
        self.precios = {"camisas":30000}
        
    def vender(self,producto,cantidad):
        if producto in self.stock:
            if cantidad <= self.stock[producto] <= cantidad:
                print(f"Vendidas {cantidad} unidades ded {producto.replace("_"," ")}")
            if producto == "camisas" and self.stock[producto]< 20:
                print("Quedan menos de 20 camisas en stock, pedir 100 camisas.")
                self.stock[producto] += 100

            self.mostrar_stock_mayor()

        elif():
            print(f"No hay suficiente stock de {producto.replace("_"," ")}")
        else:
            print("producto no valido.")
            
        
        def mostrar_stock_mayor(self):
            remeras_verdes = self.stock["remeras_verdes"]
            remeras_negras = self.stock["remeras_negras"]
            if remeras_verdes > remeras_negras:
                print("Tienes mas remeras verdes en stock.")
            elif remeras_negras > remeras_verdes:
                print("Tienes mas remeras negras en stock.")
            else:
                print("tienes la misma cantidad de remeras negras y verdes en stock")

        def mostrar_stock(self):
            for producto, cantidad in self.stock.items():
                print(f"Stock actual de {producto.replace('_', ' ')}: {cantidad}")


tienda = TiendaRopa()

tienda.vender("remeras_verdes", 10)
tienda.vender("camisas", 40)
tienda.mostrar_stock()

tienda.vender("camisas", 50)
tienda.mostrar_stock()

tienda.vender("remeras_negras", 30)
tienda.mostrar_stock()

