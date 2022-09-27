import numpy as np
import matplotlib.pyplot as plt

'''
Enunciado: Distribución del dinero en el mes.
Una persona gana X cantidad de dinero, y quiere
hacer N compras, cada una de las N compras tiene un beneficio bi (i de 1 a N)
asociado. Indicar cuales compras debe hacer, de tal manera que no gaste más del
dinero que tiene en el mes y maximice el beneficio.
'''

# Pedir datos iniciales
N = 10# int(input('Ingrese el número de compras N: '))
X = 500 #int(input("Ingrese el presupuesto que tiene para comprar X: "))
bestYglobal = np.zeros((N,))

'''
# Ingresando los datos de usuario
b=[]
c=[]
for i in range(N):
    bi = int(input(f'Ingrese beneficio del producto {i} entre 1 y 5: '))
    while bi not in (1, 2, 3, 4, 5):
        print("[!] El beneficio debe ser de 1 a 5.")
        bi = int(input(f'Ingrese beneficio del producto {i} entre 1 y 5: '))
    b.append(bi)

    ci = int(input(f"Ingrese costo del producto {i}: "))
    while ci <= 0:
        print("Valor del costo incorrecto.")
        ci = int(input(f"Ingrese costo del producto {i}: "))
    c.append(ci)
'''

b = np.random.randint(low=1, high=5, size=(N,)) # Vector de beneficios
c = np.random.randint(1,20,N) # Vector de costos entre 1 y 20
bestFtglobal = 0
cycles = 20 # número de iteraciones
bestFts = np.zeros((cycles,)) # vector que guarda el mejor cromosoma en cada iteración
Z = 20
Y = np.random.randint(0, 2, (Z,N)) # Tamaño ZxN

for cycle in range(cycles):
    R = X - np.dot(Y,c) # Tamaño (5,)
    Ft = np.where(R>0, np.dot(Y,b), 0) # Tamaño
    # Guardar el mejor puntaje local y global, y el mejor cromosoma global
    bestFt = Ft.max()
    bestFts[cycle] = bestFt
    # print(f'Best Ft {bestFt} y cromosoma {Y[np.argmax(Ft)]} en iteración {cycle}')
    if bestFt > bestFtglobal:
        print(f'Y=\n{Y}')
        bestFtglobal = bestFt  # Guardando el mejor puntaje
        bestYglobal = Y[np.argmax(Ft)].copy()
        print(f'Mejor puntaje en iteración {cycle}: {bestFtglobal}')
        print(f'Mejor cromosoma en iteración {cycle}: {bestYglobal}')

    Ftsum = np.sum(Ft)
    pselect = Ft/Ftsum
    Ftmean = pselect.mean()
    score = pselect/Ftmean
    Pint = np.zeros((Z,N))
    '''
    print(f'c=\n{c}')
    print(f'b=\n{b}')
    print(f'R=\n{R}')
    print(f'Ft=\n{Ft}')
    print(f'Ftsum=\n{Ftsum}')
    print(f'Pint=\n{Pint}')
    print(f'pselect=\n{pselect}')
    print(f'Ftmean=\n{Ftmean}')
    print(f'score={score}')
    '''

    #  Muestreo estocástico del residuo
    for i in range(Z):
        Pint[i] = Y[np.argmax(score)]
        score[np.argmax(score)] -= 1
        #print(f'score={score}')
        #print()

    #print(f'Pint=\n{Pint}')

    # Generación del compañero para el cruce

    mates = np.zeros((Z,)).astype(int)

    for i in range(0, Z):
        mate = np.random.randint(0, Z)
        while mate == i:
            mate = np.random.randint(0, Z)
        mates[i] = int(mate)


    # print(f'mates = {mates}')

    # --------- Cruce de cromosomas -------- #
    # print('Cruce de cromosomas:')
    # print(f'Pint antes =\n{Pint}')
    cross_points = np.random.randint(1, N-1, size=(Z,))
    # print(f'cross points: ',cross_points)
    for i, point in enumerate(cross_points):
        # print(f'Concatenación cromosoma {i} con cromosoma {mates[i]}')
        # print(Pint[i][:point],'+',end='')
        # print(Pint[mates[i]][point:])
        Y[i] = np.r_[Pint[i][:point], Pint[mates[i]][point:]]
        # print('Resultado: ',Y[i])

    # print(f'Y después =\n{Y}')
else:
    print(f'Costos: {c}')
    print(f'Beneficios: {b}')
    print(f'Mejor cromosoma: {bestYglobal}')
    print(f'Mejor puntaje: {bestFtglobal}')
    plt.text(np.argmax(bestFts), bestFtglobal, f'Mejor puntaje: {bestFtglobal}')
    plt.stem(bestFts)
    plt.show()