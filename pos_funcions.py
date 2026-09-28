#pos_fincions
from pos_python.pos_python import nombre
from pos_python.pos_python import cantidad
from pos_python.pos_python import contado
from pos_python.pos_python import categoria
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

def inventario_productos(): #incompleto
    if opcion == 3:
        print('Inventario de productos por categoria')
        i_categoria = str(input('Categoria a inventariar:' ))
        if i_categoria in productos:
            i_codigo = str(input('Codigo de producto encontrado'))
            if i_codigo in [productos] [categoria]:
                contado = []
                suma = 0

def ver_productos():
    if opcion == 4:
        print('Mostrando todos los productos')
        for i in productos:
            print (productos[i])

def venta_producto():
    print('Vendiendo producto')
    v_producto = str(input('Nombre de producto a vender: '))
    if v_producto in productos:
        v_cantidad = int(input('Cantidad a vender: '))
        if v_cantidad <= cantidad:
            cantidad = cantidad - v_cantidad
            #productos [v_producto][1] = [cantidad]
            print(f'Has vendido {v_cantidad} de {nombre} ahora cuentas con {cantidad}')
        else:
            print('La cantidad de producto en venta exede el producto disponible')
    else:
        print(f'El producto {v_producto} no se encuentra en el inventario')

def compra_producto():
    print('Comprando producto')
