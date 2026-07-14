import sqlite3

#usando select
def traer_productos():
    #conectar
    con =sqlite3.connect("ecommerce.db")
    
    #consultar
    cursor=con.cursor()
    
    sql="select id_cliente,nombre from clientes"
    cursor.execute(sql)
    resultado= cursor.fetchall()
    con.close()
    print(resultado)
    

def insertar_producto():
    
    con=sqlite3.connect("ecommerce.db")
    cursor=con.cursor()

    sql="Insert into clientes(nombre) values (?)"
    nombre=input("ingresar un nombre: ")

    cursor.execute(sql,(nombre,))
    con.commit()
    con.close()

def eliminar_productos():
    con=sqlite3.connect("ecommerce.db")
    cursor=con.cursor()
    sql="delete from clientes where id_cliente = 6"
    cursor.execute(sql)
    resultado=cursor.fetchall()
    con.close()
    print(resultado)
    

def actualizar():
    con=sqlite3.connect("ecommerce.db")
    cursor=con.cursor()
    sql="update clientes set nombre = ? where id_cliente = ?"
    nombre =input("ingresa nombre: ")
    id=input("ingresa id: ")
    cursor.execute(sql, (nombre, id))
    resultado=cursor.fetchall()
    con.close()
    print(resultado)


#traer_productos()
#insertar_producto()
#eliminar_productos()
actualizar()