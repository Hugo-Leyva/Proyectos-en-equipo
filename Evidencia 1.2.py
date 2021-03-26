import pandas as pd
registro_ventas={}
venta_total= []

while True:
    print("\n***MENU***")
    print("1. Registrar una venta")
    print("2. Consultar una venta")
    print("3  Salir")
    opcion = int(input("Ingrese una opcion:  "))

    if opcion == 1:
        respuesta=1
        identificador =int( input ("\nDime un numero identificador para la venta "))
        if identificador in  venta_total:
            print("\nEse identificador ya esta registrado, intenta con otro")
        else:
            while respuesta == 1:
                desc_articulo = input ("\nDime la descripcion del articulo: ")
                piezas_vendidas= int(input("\nDime la cantidad de piezas vendidas: "))
                precio_venta= float(input("\nDime el precio de venta: "))
                monto_total= piezas_vendidas * precio_venta
                print("\nSu monto total a pagar es de $ ",monto_total)
                venta_articulo= [desc_articulo,piezas_vendidas,precio_venta,monto_total]
                venta_total.append(venta_articulo)
                respuesta = int(input("\n ¿Deseas capturar otro articulo? \n(1-Si / 0-No): "))
            registro_ventas[identificador]=[venta_total]
            venta_total=[]
    elif opcion == 2:
        # El identificador debe de ser del mismo dato que el id a buscar para que se
        #Cumpla la condicion.
        id_buscar =int(input("\nDime el identificador de la venta que deseas consultar: "))
        if id_buscar in registro_ventas.keys():
            print("\nLa venta con ese identificador es: ")
            print("\n",registro_ventas[id_buscar])
        else:
            print("\nLo siento, ese identificador no fue capturado")
    elif opcion == 3:
        break
    else:
        print("Has introducido una opcion invalida")