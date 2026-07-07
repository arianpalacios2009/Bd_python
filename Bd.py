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
    nombre=input("ingresar un nombre:")

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
    
