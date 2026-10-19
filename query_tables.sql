CREATE TABLE  (
  id_producto INTEGER PRIMARY KEY NOT NULL,
  nombre_producto VARCHAR(50) NOT NULL,
  precio_venta NUMERIC NOT NULL,
  costo_compra NUMERIC NOT NULL,
  categoria VARCHAR(50) NOT NULL,
  cantidad INTEGER NOT NULL,
  proveedor INTEGER NOT NULL,
);
