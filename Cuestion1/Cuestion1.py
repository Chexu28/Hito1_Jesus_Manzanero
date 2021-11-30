import sqlite3

from sqlite3 import Error

def conectar():

    try:

        conectar = sqlite3.connect('tienda.db')

        return conectar

    except Error:

        print(Error)

def tabla(conectar):

    cursorObj = conectar.cursor()

    cursorObj.execute("CREATE TABLE clientes(id integer PRIMARY KEY, nombre text, apellido text, telefono text, edad int)")

    conectar.commit()


"""Metodo para insertar un nuevo cliente"""
def insertar(con, entities):
    cursorObj = con.cursor()

    cursorObj.execute(
        'INSERT INTO clientes(id, nombre, apellido, telefono, edad) VALUES(?, ?, ?, ?, ?)', entities)

    con.commit()

conect = conectar()

#tabla(conect)


propiedades = (4, 'Maria', 'Rodriguez', '624141785', 29)
#insertar(conect, propiedades)



""" Metodo para cambair algun parámetro"""
def update(conect):

    cursorObj = conect.cursor()

    cursorObj.execute('UPDATE clientes SET edad = 38 where id = 2')

    conect.commit()

#update(conect)



""" Metodo para seleccionar"""
def select(conect):
    cursorObj = conect.cursor()
    cursorObj.execute('SELECT nombre, apellido, edad FROM clientes')
    rows = cursorObj.fetchall()

    for row in rows:
        print(row)

#select(conect)


"""Metodo para eliminar un cliente"""
def eliminar(conect):
    cursorObj = conect.cursor()

    cursorObj.execute('DELETE FROM clientes where id = 3')

    conect.commit()

#eliminar(conect)