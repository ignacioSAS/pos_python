#pos_fincions
from pos_python.pos_python import productos
productos = {}

opcion = int(input('Digite una opcion de menu: ' ))

def agregar_producto():
    if opcion == 1:
        print('Agregar producto nuevo')
        codigo = int(input('Digite o escanie codigo de producto: '))
        nombre = str(input('Escriba el nombre del producto: '))
        costo = float(input('Costo compra de producto: $'))
        precio = float(input('Precio venta de producto: $'))
        categoria = str(input('Categoria de producto: '))
        productos [codigo] = [nombre,costo,precio,categoria]


def buscar_producto():
    print('Buscando producto')
    if opcion == 2:
        b_nombre = str(input('Escriba el nombre del producto a consultar: '))
        if b_nombre in productos:
            print(f'Dtealles de producto: {productos [b_nombre]}')

def inventario_productos():
    print('inventario de productos')

def ver_productos():
    print('Mostrando todos los productos')

def venta_producto():
    print('Vendiendo producto')

def compra_producto():
    print('Comprando producto')
