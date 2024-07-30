
costoXcafe = 800
cantidadVendidaParaRegalarOtroCafe = 4
ventas = [2, 4, 9]
totalCafesEntregados = 0
totalCafesVendidos = sum(ventas)

for venta in ventas:
    cafesGratis = venta // cantidadVendidaParaRegalarOtroCafe
    cafesEntregados = venta + cafesGratis
    totalCafesEntregados += cafesEntregados

print(f"{totalCafesVendidos=}")
print(f"{totalCafesEntregados=}")
costoTotal = totalCafesEntregados * costoXcafe
print(f"Costo real total: {costoTotal}")
print(f"Costo real por café: {costoTotal / totalCafesVendidos}")

