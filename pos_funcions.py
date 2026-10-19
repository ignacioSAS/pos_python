
def agregar_producto():
    print('Agregar nuevo producto a inventario')
    id_producto = int(input('Codigo de barras de producto: '))
    nombre_producto = str(input('Nombre de producto: '))
    precio_venta = float(input('Precio veta de producto: $'))
    costo_compra = float(input('Costo compra producto: $'))
    categoria = str(input('Categoria de producto: '))
    cantidad = int(input('Cantidad critica/minima de producto: '))
    proveedor =int(input('id_proveedor'))
    

def venta_producto(venta):
    print('Realizar venta de producto')
    id_producto = int(input('Codigo:'))
    cantidad_venta = int(input('Cantidad a vender:'))

def compra_producto(compra):
    print('Realizar compra producto')

def inventario(inventario):
    print('Realizar inventario por producto')
    print('Realizar inventario por categoria')

def reportes():
    print('Reporte ventas')
    print('Reporte compras')

def proveedores():
    print('Crear nuevo proveedor')