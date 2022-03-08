import mysql.connector
from tkinter.messagebox import *
import tk_int


class Funciones():
    def __init__(self):
        mibase = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd=""
        )
        crear_base = mibase.cursor()

        crear_base.execute("create database if not exists tp_final")

        conexion1 = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="tp_final"
        )

        micursor = conexion1.cursor()

        micursor.execute("create table if not exists trabajo_final( id int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT, nombre VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL, apellido varchar(128) COLLATE utf8_spanish2_ci NOT NULL, dni int(8) UNIQUE COLLATE utf8_spanish2_ci NOT NULL )")

    def conectar(self):
        conexion1 = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="tp_final"
        )
        return conexion1

    def alta(self, datos):
        con = self.conectar()
        cursor = con.cursor()
        sql = "insert into trabajo_final(nombre, apellido, dni) values (%s,%s,%s)"
        cursor.execute(sql, datos)
        con.commit()
        con.close()

    def baja(self, dato):
        con = self.conectar()
        cursor = con.cursor()
        sql = "DELETE from trabajo_final where id=" + dato
        cursor.execute(sql)
        con.commit()
        con.close()

    def modificar(self, nom, app, doc, aid):
        con = self.conectar()
        cursor = con.cursor()
        sql = f"UPDATE trabajo_final SET nombre = '{nom}', apellido= '{app}', dni='{doc}' WHERE id='{aid}'"
        cursor.execute(sql)
        con.commit()
        con.close()

    def actualizar_tree(self, reg):
        con = self.conectar()
        cursor = con.cursor()
        cursor.execute(reg)
        

        
