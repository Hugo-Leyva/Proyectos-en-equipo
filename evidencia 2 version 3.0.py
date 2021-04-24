import datetime
import os
import csv
import pandas as pd

folio=0 #esta variable nos creara folios consecutivos
registro_ventas_csv={}
columnas=["Fecha", "Folio", "Descripcion", "Piezas Vendidas", "Precio de venta", "Monto Total"]

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

while True:
    print("\n***MENU***")
    print("1. Registrar una venta")
    print("2. Consultar una venta")
    print("3. Consultar Reporte de ventas")
    print("4.  Salir")
    opcion = input("Ingrese una opcion: ") 

    if opcion == '1':

        folio=folio+1   
        folio_list.append(folio)
        crear_folio()


        
        #precio_total=[]
                 
        print(f"VENTA {folio}")
        
        while True:
            desc_list=[]
            cant_list=[]
            precio_list=[]
            fecha_list=[]

            descripcion=input("Dime la descripcion del articulo: : ")
            desc_list.append(descripcion)
            
            cantidad=int(input("Dime la cantidad de piezas vendidas: "))
            cant_list.append(cantidad)
            
            precio=float(input("Dime el precio de venta: "))
            #precio_total.append(precio*cantidad)
            precio_list.append(precio)

            #monto total de la venta
            venta_total = precio*cantidad
        
            tiempo_actual = datetime.datetime.now()
            tiempo_actual2 = tiempo_actual.strftime('%d/%m/%Y')
            fecha_list.append(str(tiempo_actual2))
            
            
            registro_ventas_csv["Folio"]=folio
            registro_ventas_csv["Descripcion"]=desc_list
            registro_ventas_csv["Cantidad"]=cant_list
            registro_ventas_csv["Precio"]=precio_list
            registro_ventas_csv["Fecha"]=fecha_list

            #Aqui se genera el reporte de ventas mediante un dataframe de pandas
            DF_REPORTE_VENTAS=pd.DataFrame(registro_ventas_csv)
            
            ruta = "datos.csv"
            DF_REPORTE_VENTAS.to_csv(ruta, index=None, mode="a", header=not os.path.isfile(ruta))
            
            #se incrementa el folio

            respuesta = input("\n¿Deseas capturar otro articulo? (1-Si / 0-No): ")
            if respuesta == "0":
                print("El monto total de la venta es: ",venta_total)
                break


    elif opcion == '2':
        try:
            datos_1 = pd.read_csv('datos.csv')
            df_datos_recuperados = pd.DataFrame(datos_1)
            venta=int(input("Dime el folio que quieres consultar "))
            folio_datos = df_datos_recuperados[df_datos_recuperados['Folio']==venta]
            print(folio_datos)
        except:
            print("Folio no encontrado")  



    elif opcion == '3':
        datos_1 = pd.read_csv('datos.csv')
        df_datos_recuperados = pd.DataFrame(datos_1)
        print(df_datos_recuperados)

    elif opcion=="4":
        print("Hasta pronto")
        break
    else: 
        print("Has introducido una opcion invalida")
    