import numpy as np
plantasyparqueaderos = np.zeros((8,5)) # Matriz 8x5
entrada=0
while(entrada!="s"):
    print("1.Visualizacion de coches en cada planta, si esta en 1 hay coche si esta en 0 esta vacio")
    print("2.Aparcar")
    print("3. Sacar Coche")
    print("4.Plantas Libres")
    print("5.Plana mas Vacia")
    print("6.Total Coches")
    print("7.Mantenimiento Planta")
    print("8.Porcentajes de Ocupacion")
    print("9. No Reservadas")
    print("s.Salir")
    entrada=input("Ingrese la opcion que desea ejecutar o s para salir: ")
    if(entrada=="s"):
        print("Saliendo del programa...")
    else:
        entradaint=int(entrada)
    if(entradaint==1):
        print(plantasyparqueaderos)
    if(entradaint==2):
        planta=int(input("ingrese el numero de planta donde desea parquea: "))
        if(planta>=1 and planta<=8):
            hay_libre = 0 in plantasyparqueaderos[planta-1]
            if(hay_libre):
                print("Excelente, planta",planta,"tiene un espacio libre")
                for i in range(0,5):
                    if(plantasyparqueaderos[planta-1][i]==0):
                        plantasyparqueaderos[planta-1][i]=1
                        print("Vehiculo estacionado en la planta", planta ,"espacio", i+1)
                        break
            else:
                print("Planta ocupada no hay espacios libres para parquear")

    if(entradaint==3):
        planta = int(input("Ingrese la planta 1 a la 8: "))
        espacio = int(input("Ingrese el número de espacio 1 al 5: "))
        if planta>=1 and planta<=8 and espacio>=1 and espacio<=5:
            if plantasyparqueaderos[planta-1][espacio-1] == 1:
                plantasyparqueaderos[planta-1][espacio-1] = 0
                print("Vehículo retirado ")
            else:
                print("Ese espacio ya está vacío")
        else:
            print("Datos inválidos")

    if(entradaint==4):
        for i in range(8):
            libres = 0
            for j in range(5): 
                if plantasyparqueaderos[i][j] == 0:
                    libres += 1
            print("Planta", i+1, "tiene", libres, "espacios libres.")

    if(entradaint==5):
        max_libres = -1
        planta_vacia = -1
        for i in range(8):
            libres = 0
            for j in range(5):
                if plantasyparqueaderos[i][j] == 0:
                    libres += 1
            if libres > max_libres:
                max_libres = libres
                planta_vacia = i+1
        print("La planta más vacía es la", planta_vacia, "con", max_libres, "espacios libres.")

    if(entradaint==6):
        total = 0
        for i in range(8):
            for j in range(5):
                if plantasyparqueaderos[i][j] == 1:
                    total += 1
        print("Hay un total de", total, "coches en el parqueadero.")

    if(entradaint==7):
        planta = int(input("Ingrese la planta a vaciar (1-8): "))
        if planta>=1 and planta<=8:
            for j in range(5):
                plantasyparqueaderos[planta-1][j] = 0
            print("Planta", planta, "ahora está vacía.")
        else:
            print("Número de planta inválido.")

    if(entradaint==8):
        for i in range(8):
            ocupados = 0
            for j in range(5):
                if plantasyparqueaderos[i][j] == 1:
                    ocupados += 1
            porcentaje = (ocupados * 100) / 5
            print("Planta", i+1, ":", porcentaje, "% ocupación.")

    if(entradaint==9):
        for i in range(8):
            vacios = 0
            for j in range(5):
                if plantasyparqueaderos[i][j] == 0:
                    vacios += 1
            print("Planta", i+1, "tiene", vacios, "espacios no reservados")