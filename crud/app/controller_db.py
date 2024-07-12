
from data_base import conexionMySQL


# consultas -> CRUD

# Read -> SELECT
def resultados_cursos():
    # conexion
    conexion = conexionMySQL()
    # consulta db
    with conexion.cursor() as cursor:
        # Read a single record
        query = "SELECT * FROM usuarios_y_clases"
        # query2=f"SELECT * FROM productos where id = {id}"
        cursor.execute(query)
    # procesar los resultados -> fetch
        result = cursor.fetchall()
    # cerrar la conexion
        conexion.commit()
        conexion.close()
        return result
    
# Create - insert
def cargar_cursos(nombre, descripcion, precio):
    conexion = conexionMySQL()
    with conexion.cursor() as cursor:
        query = "INSERT INTO usuarios_y_clases (nombre_alumno, apellido_alumno, telefono, correo_electronico, clase) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (nombre_alumno, apellido_alumno, telefono, correo_electronico, clase))
        result = cursor
        conexion.commit()
        conexion.close()
        return result
# Update -> 1) 
def obtener_curso_por_id(id):
    conexion = conexionMySQL()
    with conexion.cursor() as cursor:
        query="SELECT * FROM usuarios_y_clases WHERE id = %s"
        cursor.execute(query, (id))
        prod = cursor.fetchone()
    conexion.commit()
    conexion.close()
    return prod
# update -> 2)
def actualizar_cursos(nombre, descripcion, precio, id):
    conexion = conexionMySQL()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE usuarios_y_clases SET nombre_alumno = %s, apellido_alumno = %s, telefono = %s, correo_electronico = %s, clase = %s WHERE id = %s",(nombre_alumno, apellido_alumno, telefono, correo_electronico, clase))
        result = cursor
    conexion.commit()
    conexion.close()
    return result

# borrar -> delete
def eliminar_curso(id):
    conexion = conexionMySQL()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM usuarios_y_clases WHERE id = %s", (id))
        result = cursor
    conexion.commit()
    conexion.close()
    return result
