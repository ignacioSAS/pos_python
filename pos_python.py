productos = {}
flag=True

while True:
  print('''
    1. Añadir productos.
    2. Buscar producto.
    3. Inventario.
    4. Ver productos.
    5. Venta
    6. Compra''')
  
  respuesta=int(input('Ingrese su opcion: '))
  
  if respuesta == 1:
    print('\t Agregar producto nuevo')
    nombre = str(input('Nombre de el producto: '))
    codigo = int(input('Codigo de producto: '))
    cantidad = int(input('Cantidad de producto: ')) 
    costo = float(input('Costo compra de producto :$'))
    precio = float(input('Precio venta de producto:$ '))
    categoria = str(input('Categoria de producto: '))
    productos [nombre]=[codigo,cantidad,costo,precio,categoria ]
    print(productos)

  elif respuesta == 2:
    b_nombre=str(input('Nombre del producto a buscar: '))
    if b_nombre in productos:
      print(f'Detalles de producto {productos[nombre]}')
  
  elif respuesta == 3: #incompleta solo entra a la ultima ctegoria creada
    b_categoria = str(input('Categoria a consultar: '))
    if b_categoria == categoria:
      print(f'La categoria {b_categoria} si se encuentra en la base de datos')
      print(nombre)
    else:
      print('La categoria seleccionada no se encuentra')

'''
      contado=[]
      suma=0
      while contado != cantidad:
        print('Digita 0 para terminar en cualquier momento')
        encontrado=int(input('Cantidad encontrada: '))
        contado.append(encontrado)
        print(f'Has encontrado {contado}')
        for i in contado:
          suma=sum(contado)
        print(f'Total encontrado {suma}')
        if encontrado == 0: 
          print(f'Total encontrado {suma}')
          print(f'Valor de inventario {suma*costo }')
          break
        if suma>=cantidad:
          terminar=str(input('A encotrado todos los productos deceas terminar (y/n): ')) 
          if terminar=='y':
            print(f'valor de inventario {suma*costo }')
            break
    else:
      print(f'El producto {b_categoria} no se encuentra en tu inventario')

  elif respuesta == 4:
    for i in productos:
      print(productos[i])

  elif respuesta == 5:
    venta=(str(input('Producto a vender: ')))
    print(f'Estas vendiendo {venta}')
    if venta in productos:
      cantidad=int(input('Cantidad a vender: '))
      if cantidad<=cantidad:
        cantidad= cantidad-cantidad
        productos [venta][1] = cantidad
        print(f'Has vendido {venta}')
        print(f'Haora cuentas con {cantidad} pz')
      else:
        print('No cuentas con la cantidad suficiente para la venta de este produnto')

  elif respuesta == 6:
    print('Comprar producto')
    compra=str(input('Producto a comprar: '))
    if compra in productos:
      cantidad=int(input('Cantidad a comprar: '))
      cantidad=cantidad+cantidad
      productos [compra][1]=cantidad
      print(f'Ahora cuentas con {cantidad} de {compra}')'''