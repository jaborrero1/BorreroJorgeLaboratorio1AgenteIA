#INSTRUCCIONES
#Ingreso de Ubicaciones Puesto1 - Puesto2 - Puesto3
#Ingreso del estado 0 / 1, donde 0 significa buenas puntadas y 1 malas puntadas

def maquina_coser():
    #Inicializacion del estado objectivo
    # 0 indica Buenas puntadas y 1 malas puntadas
    estado_objetivo = {'Puesto1': '0', 'Puesto2': '0', 'Puesto3': '0'}
    costo = 0

    #El confeccionista indica la ubicación de la maquina de coser
    ingresar_ubicacion = input("Ingreso de la ubicacion de la maquina de coser: ")

    # El confeccionista indica si la maquina de coser se encuentra realizando buenas puntadas 
    # o malas puntadas (0/1) en la ubicación señalada.
    ingresar_estado = input("Ingreso de la ubicacion : " +ingresar_ubicacion+ " ")

    #El confeccionista ingresa el Puesto1
    if (ingresar_ubicacion == 'Puesto1'):
        
        # el usuario indica si la maquina de coser se encuentra realizando una buena puntadas 
        # o mala puntada (0/1) en la ubicación señalada.
        estado_ubicacion2 = input("Ingreso del estado del puesto 2: ")
        estado_ubicacion3 = input("Ingreso del estado del puesto 3: ")

        #Se imprime el resultado obtenido
        print("Destino Deseado Obtenido:" + str(estado_objetivo))

        # Se imprime en que puesto esta ubicado la maquina de coser
        print("La maquina de coser se encuentra en el puesto 1")

        #La maquina de coser del puesto 1 se encuentra realizando malas puntadas
        if(ingresar_estado == '1'):
            print("La maquina de coser del puesto 1 se encuentra realizando malas puntadas")
            #La maquina de coser realizara buenas puntadas
            estado_objetivo['Puesto1'] = '0'
            #El costo aumentara cada vez que la maquina realice buenas puntadas
            costo += 1
            #Se imprime el resultado de la maquina de coser que esta realizando buenas puntadas
            print("La maquina de coser esta realizando buenas puntadas en el puesto 1")
            #Devuelve el costo actual
            print("El costo actual es de: " + str(costo))

            #La maquina de coser del puesto 2 se encuentra realizando malas puntadas
            if(estado_ubicacion2 == 1):
                print("La maquina de coser del Puesto 2 se encuentra realizando malas puntadas")
                print("La maquina de coser esta en el Puesto 2")
                #Se imcrementa el costo porque la maquina de coser se encuentra en el puesto 2
                costo += 1
                #Muestra el costo actual
                print("El costo actual es de: " + str(costo))
                #La maquina de coser esta realizando buenas puntadas
                estado_objetivo['Puesto2'] = '0'
                #El costo aumenta cada vez que la maquina de coser realiza buenas puntadas
                costo += 1
                print("La maquina de coser esta realizando buenas puntadas en el puesto 2")
                #Se obtiene el costo actual
                print("El costo actual es de: " + str(costo))
            else:
                #La maquina de coser esta realizando buenas puntadas
                print("La maquina de coser del puesto 2 se encuentra realizando buenas puntadas")
                print("No se realiza ninguna acción. El costo actual es de: "  + str(costo))