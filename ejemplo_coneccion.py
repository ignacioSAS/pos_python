import psycopg2

try:
    # Establecer la conexión
    conexion = psycopg2.connect(
        host="localhost",
        database="tienda",
        user="postgres",
        password="postgres",
        port=5432
    )
    
    # Crear un cursor para ejecutar consultas
    cursor = conexion.cursor()
    
    # Probar una consulta simple
    cursor.execute("SELECT version();")
    version = cursor.fetchone()
    print("Conectado exitosamente a PostgreSQL. Versión:", version)
    
    # Cerrar cursor
    cursor.close()
    
    # Cerrar conexión
    conexion.close()
    print("Conexión cerrada.")

except Exception as error:
    print("Error al conectar a PostgreSQL:", error)
