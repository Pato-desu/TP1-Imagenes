import cv2
import numpy as np
import matplotlib.pyplot as plt
from contar import contar_caracteres_y_palabras
from sub_images import sub_images
from checks import check

def check_y_print(nombre_archivo):
    print('\n' + nombre_archivo + ':\n')

    renglones = sub_images('Ejercicio 2/Images/'+nombre_archivo)

    n_linea = 0
    for nombre, imagen in renglones.items():
        n_linea += 1
        if type(imagen) is list:
            n_car1, n_pal1 = contar_caracteres_y_palabras(imagen[0])
            n_car2, n_pal2 = contar_caracteres_y_palabras(imagen[1])
            n_car = n_car1 + n_car2
            n_pal = n_pal1 + n_pal2
        else:
            n_car, n_pal = contar_caracteres_y_palabras(imagen)

        if check(n_linea, n_car, n_pal):
            estado = 'OK'
        else:
            estado = 'MAL'

        match(n_linea):
            case 1:
                n_tabs = 1
            case 2 | 3 | 4:
                n_tabs = 3
            case 5 | 6 | 7 | 8:
                n_tabs = 2

        print('\t' + nombre + ':' + '\t' * n_tabs + estado)

for i in range(1, 6):
    check_y_print(f'formulario_0{i}.png')
