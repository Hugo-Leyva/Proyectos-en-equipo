import pandas as pd
venta_detalle={}

while True:
    print("\n***MENU***")
    print("1. Registrar una venta")
    print("2. Consultar una venta")
    print("3  Salir")
    opcion = int(input("Ingrese una opcion:  "))

    if opcion == 1:
        respuesta=1
        while respuesta == 1:     
            print("\nIngresa un numero identificador para la venta: ")
            identificador=int(input())
            if identificador in  venta_detalle:
                print("\nEse identificador ya esta registrado, intenta con otro")
            else:
                desc_articulo = input ("\nDime la descripcion del articulo: ")
                piezas_vendidas= int(input("\nDime la cantidad de piezas vendidas: "))
                precio_venta= float(input("\nDime el precio de venta: "))
                monto_total= piezas_vendidas * precio_venta
                print("\nSu monto total a pagar es de $ ",monto_total)
                venta_detalle[identificador]= [desc_articulo,piezas_vendidas,precio_venta,monto_total]
            respuesta = int(input("\n ¿Deseas capturar otro registro? \n(1-Si / 0-No): "))
    elif opcion == 2:
        id_buscar =int(input("\nDime el identificador de la venta que deseas consultar: "))
        if id_buscar in venta_detalle.keys():
            print("\nLa venta con ese identificador es: ")
            print("\n",venta_detalle[id_buscar])
        else:
            print("\nLo siento, ese identificador no fue capturado")
    elif opcion == 3:
        break
    else:
        print("Has introducido una opcion invalida")