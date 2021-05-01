import sys
import sqlite3
import datetime
from sqlite3 import Error
import os
import csv


folio=0 #esta variable nos creara folios consecutivos
separador = ("-"*50)


def crear_folio():
    registrador = open("folio.csv", "w")
    registrador.write(str(folio))


#LEEMOS EL ULTIMO FOLIO QUE SE REGISTRÓ, SI NO EXISTE EL CSV SE CREA UNO 
try:
    with open("folio.csv", "r") as archivo:
        lector = csv.reader(archivo)
        for folio_csv in lector:
            folio_list = folio_csv
except:
    crear_folio()




with open("folio.csv", "r") as archivo:
    lector = csv.reader(archivo)
    for folio_csv in lector:
        folio_list = folio_csv

folio=int(folio_list[-1])      #IGUALAMOS EL ULTIMO FOLIO QUE SE GUARDÓ EN LA VARIABLE folio



def crear_db():
    try:
        with sqlite3.connect("Ventas.db") as conn:
            c = conn.cursor()
            c.execute("CREATE TABLE IF NOT EXISTS registro_ventas(Folio_numerico INTEGER PRIMARY KEY);")
            c.execute("CREATE TABLE IF NOT EXISTS detalle_ventas(Folio INTEGER, Descripcion TEXT NOT NULL, Piezas INT, Precio DECIMAL(6,2), Fecha TIMESTAMP NOT NULL, FOREIGN KEY (Folio) REFERENCES registro_ventas(Folio_numerico));")
            print("Tablas creadas exitosamente")
    except Error as e:
        print (e)
    except:
        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")

#Se crea la base de datos SQLite, en caso de que no exista
if os.path.isfile('Ventas.db'):
    pass
else:
    crear_db()



def insertar_venta():
    global folio
    folio=folio+1   
    folio_list.append(folio)
    print(separador)
    print(f"Su numero de folio es: {folio} úselo para consultar la venta en el futuro")
    print(separador)
    fecha = input("Iingrese la fecha que desea capturar en formato dd/mm/yyyy. ")

    Monto = []

    fecha_convertida = datetime.datetime.strptime(fecha, "%d/%m/%Y").date()
    fecha_con_tiempo = datetime.datetime.combine(fecha_convertida, datetime.datetime.min.time()) #Es importante complementar la fecha con la parte horaria
    x = 1
    while True:
        

        Descripcion = input("Ingresa la descripcion del producto ")
        cantidad = int(input("Ingrese la cantidad de piezas vendidas "))
        precio = float(input("Ingrese el precio por unidad "))

        venta_total = precio * cantidad
        Monto.append(venta_total)



        try:
            with sqlite3.connect("Ventas.db") as conn:
                print("Conexión establecida")
                mi_cursor = conn.cursor()
                
                if x == 1:
                    #INSERTAR LLAVE PRIMARIA A LA TABLA REGISTRO_VENTAS
                    criterio = {"Folio":folio}
                    mi_cursor.execute("INSERT INTO registro_ventas (Folio_numerico) VALUES(:Folio)", criterio)
                else:
                    pass

                #INSERTAR DATOS A LA TABLA DETALLE_VENTAS
                valores = {"Folio":folio, "Descripcion":Descripcion, "Piezas":cantidad, "Precio":precio, "Fecha":fecha_con_tiempo}
                mi_cursor.execute("INSERT INTO detalle_ventas (Folio, Descripcion, Piezas, Precio, Fecha) VALUES(:Folio, :Descripcion, :Piezas, :Precio, :Fecha)", valores)

                print("Registro agregado exitosamente")
        except Error as e:
            print (e)
        except:
            print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
        finally:
            if (conn):
                conn.close()
                print("Se ha cerrado la conexión")
        print(separador)
        opcion = int(input("¿Desea registrar otra articulo? SI-(1)  NO-(0) "))
        if opcion == 0:
            print("El monto total de la venta es: ",Monto[-1])
            Monto = []
            break
        elif opcion == 1:
            x=0
            pass
        else:
            print("Ha ingresado una opcion inválida")
            break


def consulta_folio():
    folio_consulta = int(input("Dime el folio a consultar "))
    
    try:
        with sqlite3.connect("Ventas.db") as conn:
            mi_cursor = conn.cursor()
            criterios = {"folio":folio_consulta}
            mi_cursor.execute("SELECT * FROM detalle_ventas WHERE (Folio) = :folio;", criterios)
            registros = mi_cursor.fetchall()
            print(f"\nDatos de la venta {folio_consulta}:\n",separador)  
            for Folio_numerico, Descripcion, Piezas, Precio, Fecha in registros:
                print(f"Folio: \t\t{Folio_numerico}")
                print(f"Descripción:\t{Descripcion}")
                print(f"Piezas: \t{Piezas}")
                print(f"Precio: \t{Precio}")
                print(f"Fecha: \t\t{Fecha}\n",separador)

            
    except sqlite3.Error as e:
        print (e)
    except Exception:
        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
    finally:
        if (conn):
            conn.close()
            print("Se ha cerrado la conexión con la base de datos")






def consulta_fecha():
    fecha_consultar = input("Dime una fecha (dd/mm/aaaa): ")
    fecha_consultar = datetime.datetime.strptime(fecha_consultar, "%d/%m/%Y").date()

    try:
        with sqlite3.connect("Ventas.db", detect_types = sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES) as conn:
            mi_cursor = conn.cursor()
            criterios = {"fecha":fecha_consultar}
            mi_cursor.execute("SELECT * FROM detalle_ventas WHERE DATE(Fecha) = :fecha;", criterios)
            registros = mi_cursor.fetchall()

            print(f"\nDatos registrados en {fecha_consultar}:\n",separador) 
            for Folio_numerico, Descripcion, Piezas, Precio, Fecha in registros:
                print(f"Folio: \t\t{Folio_numerico}")
                print(f"Descripción:\t{Descripcion}")
                print(f"Piezas: \t{Piezas}")
                print(f"Precio: \t{Precio}")
                print(f"Fecha: \t\t{Fecha}\n",separador)


            
    except sqlite3.Error as e:
        print (e)
    except Exception:
        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
    finally:
        if (conn):
            conn.close()
            print("Se ha cerrado la conexión con la base de datos")




while True:
    print("Opcion 1.- registrar una venta")
    print("Opcion 2.- Consultar una venta")
    print("Opcion 3.- Reporte de ventas para fecha especifica")
    print("Opcion 4.- Salir")
    respuesta = int(input("Elige una opción :"))
    if respuesta == 1:
        crear_folio()
        insertar_venta()
    elif respuesta == 2:
        consulta_folio()
    elif respuesta == 3:
        consulta_fecha()
    elif respuesta == 4:
        print("-"*40, "\nHasta pronto")
        break