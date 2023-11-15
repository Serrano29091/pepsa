from __future__ import print_function
from bd import obtener_conexion
import sys

def insertar_pelicula(nombre, descripcion, duracion,clasificacion):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("INSERT INTO peliculas(nombre, descripcion, duracion,clasificacion) VALUES (%s, %s, %s,%s)",
                       (nombre, descripcion, duracion,clasificacion))
            if cursor.rowcount == 1:
                ret={"status": "OK" }
            else:
                ret = {"status": "Failure" }
        code=200
        conexion.commit()
        conexion.close()
    except:
        print("Excepcion al insertar una pelicula", file=sys.stdout)
        ret = {"status": "Failure" }
        code=500
    return ret,code

def convertir_pelicula_a_json(pelicula):
    d = {}
    d['id_pelicula'] = pelicula[0]
    d['nombre'] = pelicula[1]
    d['descripcion'] = pelicula[2]
    d['duracion'] = pelicula[3]
    d['clasificacion'] = pelicula[4]
    return d

def obtener_peliculas():
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("SELECT id_pelicula, nombre, descripcion, duracion,clasificacion FROM peliculas")
            peliculas = cursor.fetchall()
            peliculasjson=[]
            if peliculas:
                for pelicula in peliculas:
                    peliculasjson.append(convertir_pelicula_a_json(pelicula))
        conexion.close()
        code=200
    except:
        print("Excepcion al obtener los peliculas", file=sys.stdout)
        peliculasjson=[]
        code=500
    return peliculasjson,code

def obtener_pelicula_por_id(id_pelicula):
    peliculajson = {}
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            #cursor.execute("SELECT id_pelicula, nombre, descripcion, duracion,clasificacion FROM peliculas WHERE id_pelicula = %s", (id_pelicula,))
            cursor.execute("SELECT id_pelicula, nombre, descripcion, duracion,clasificacion FROM peliculas WHERE id_pelicula =" + id_pelicula)
            pelicula = cursor.fetchone()
            if pelicula is not None:
                peliculajson = convertir_pelicula_a_json(pelicula)
        conexion.close()
        code=200
    except:
        print("Excepcion al recuperar un pelicula", file=sys.stdout)
        code=500
    return peliculajson,code


def eliminar_pelicula(id_pelicula):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("DELETE FROM peliculas WHERE id_pelicula = %s", (id_pelicula,))
            if cursor.rowcount == 1:
                ret={"status": "OK" }
            else:
                ret={"status": "Failure" }
        conexion.commit()
        conexion.close()
        code=200
    except:
        print("Excepcion al eliminar un pelicula", file=sys.stdout)
        ret = {"status": "Failure" }
        code=500
    return ret,code

def actualizar_pelicula(id_pelicula, nombre, descripcion, duracion, clasificacion):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("UPDATE peliculas SET nombre = %s, descripcion = %s, duracion = %s, clasificacion=%s WHERE id_pelicula = %s",
                       (nombre, descripcion, duracion, clasificacion,id_pelicula))
            if cursor.rowcount == 1:
                ret={"status": "OK" }
            else:
                ret={"status": "Failure" }
        conexion.commit()
        conexion.close()
        code=200
    except:
        print("Excepcion al eliminar un pelicula", file=sys.stdout)
        ret = {"status": "Failure" }
        code=500
    return ret,code