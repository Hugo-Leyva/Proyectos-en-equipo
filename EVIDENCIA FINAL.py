registro_ventas = {}
venta_total = 0
dict_venta = {}

while True:
    print("\n***MENU***")
    print("1. Registrar una venta")
    print("2. Consultar una venta")
    print("3  Salir")
    opcion = input("Ingrese una opcion: ")

    if opcion == '1':
        identificador = input("\nDime un numero identificador para la venta: ")
        if identificador in registro_ventas:
            print("\nEse identificador ya esta registrado, intenta con otro")
        else:
            registro_ventas[identificador] = []
            while True:
                desc_articulo = input("Dime la descripcion del articulo: ")
                piezas_vendidas = int(input("Dime la cantidad de piezas vendidas: "))
                precio_venta = float(input("Dime el precio de venta: "))
                monto_total = piezas_vendidas * precio_venta
                print("Su monto total a pagar es de $ ",monto_total)
                venta_total = venta_total + monto_total
                registro_ventas[identificador].append([desc_articulo, piezas_vendidas, precio_venta, monto_total])
                respuesta = input("\n¿Deseas capturar otro articulo? (1-Si / 0-No): ")
                if respuesta == '0':
                    print("El monto total de la venta es: ",venta_total)
                    dict_venta[identificador]=venta_total
                    venta_total = 0
                    break

    elif opcion == '2':
        id_buscar = input("\nDime el identificador de la venta que deseas consultar: ")
        if id_buscar in registro_ventas:
            print("\nLa venta con ese identificador es: ", id_buscar)
            print(f'{"Descripcion":<25} {"Cantidad":^10} {"Precio venta":^10} {"Precio total":>15}')
            print(f'{"-----------":<25} {"--------":^10} {"------------":^10} {"------------":>15}')
            for articulo in registro_ventas[id_buscar]:
                print(f'{articulo[0]:<25} {articulo[1]:^10} {articulo[2]:^10.2f} {articulo[3]:>15.2f}')
            print(f'El precio total de la venta es: {dict_venta[id_buscar]}')   #consultamos el elemento 1 del diccionario que es la lista y el elemento 4 de la lista

        else:
            print("\nLo siento, ese identificador no fue capturado")
    elif opcion == '3':
        print("Gracias por su compra, vuelva pronto")
        break
    else: 
        print("Has introducido una opcion invalida") 