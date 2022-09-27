from cmath import pi
from re import I
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
N = int(input('Ingrese el número de compras N: '))

X = int(input("Ingrese el presupuesto que tiene para comprar X: "))
Ft=[]
b = np.random.randint(low=1, high=5, size=(N,)) # Vector de beneficios
c = np.random.randint(1,100,N) # Vector de costos

# Ingresando los datos de usuario
'''
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
Z = 5
Y = np.random.randint(0, 2, (Z,N)) # Tamaño ZxN
'''
Y = np.array([
    [0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [1, 0, 0, 1, 1]
])
'''
# Y = np.array([13, 24, 8, 19]) # De la profe
R = X - np.dot(Y,c) # Tamaño (5,)
Ft = np.where(R>0, np.dot(Y,b), 0) # Tamaño 
#Ft = np.square(Y)
Ftsum = np.sum(Ft)
pselect = Ft/Ftsum
Ftmean = pselect.mean()
score = pselect/Ftmean
Pint = np.zeros((Z,N))

print(f'Y=\n{Y}')
print(f'c=\n{c}')
print(f'b=\n{b}')
print(f'R=\n{R}')
print(f'Ft=\n{Ft}')
print(f'Ftsum=\n{Ftsum}')
print(f'Pint=\n{Pint}')
print(f'pselect=\n{pselect}')
print(f'Ftmean=\n{Ftmean}')

print(f'score={score}')
for i in range(Z):
    Pint[i] = Y[np.argmax(score)]
    score[np.argmax(score)] -= 1
    print(f'score={score}')
    print()

print(f'Pint=\n{Pint}')

