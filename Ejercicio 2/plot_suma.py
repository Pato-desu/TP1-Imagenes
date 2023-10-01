import numpy as np
import matplotlib.pyplot as plt 

def plot_pix_sumat(img_zeros, suma_por_columna, suma_por_fila):
    # Crear vectores para los ejes x e y
    x = np.arange(img_zeros.shape[1])
    y = np.arange(img_zeros.shape[0])

    # Crear una figura y ejes
    fig, ax = plt.subplots()

    # Graficar la suma de píxeles en el eje x y eje y en el mismo gráfico
    ax.plot(x, suma_por_columna, label='Suma por Columna', color='blue')
    ax.plot(suma_por_fila, y, label='Suma por Fila', color='red')

    # Invertir ejes si es necesario
    ax.invert_xaxis()
    ax.invert_yaxis()

    # Configurar las etiquetas de los ejes
    ax.set_xlabel('Suma de Píxeles')
    ax.set_ylabel('Posición en el Eje X / Eje Y')

    # Agregar una leyenda
    ax.legend()

    # Mostrar el gráfico
    plt.show(block = False)