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