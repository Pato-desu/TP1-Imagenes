import cv2
import numpy as np
import matplotlib.pyplot as plt
import os


def local_histogram_equalization(image, window_size):
    # Obtener las dimensiones de la imagen
    height, width = image.shape[:2]
    half_window = window_size // 2
    result_image = np.zeros_like(image)

    for y in range(height):
        for x in range(width):
            # Definir las coordenadas de la ventana
            y1, y2 = max(0, y - half_window), min(height, y + half_window + 1)
            x1, x2 = max(0, x - half_window), min(width, x + half_window + 1)

            # Extraer la región de la imagen dentro de la ventana
            window = image[y1:y2, x1:x2]

            # Calcular el histograma de la región de la ventana
            #hist = cv2.calcHist([window], [0], None, [256], [0, 256])

            # Realizar la ecualización del histograma local
            hist_equalized = cv2.equalizeHist(window)

            # Asignar el valor ecualizado al píxel de la imagen de resultado
            result_image[y, x] = hist_equalized[window_size // 2, window_size // 2]

    return result_image

img = cv2.imread('Imagen_con_detalles_escondidos.tif', cv2.IMREAD_GRAYSCALE)

img = cv2.copyMakeBorder(img, 1, 1, 1, 1, cv2.BORDER_REPLICATE)

window_size =12  # Tamaño de la ventana (puede ajustarse según sea necesario)
# Aplicar la ecualización local del histograma
output_image = local_histogram_equalization(img, window_size)

# Aplicar un filtro de mediana para eliminar el ruido
kernel_size = 3  # Tamaño del kernel de mediana (puede ajustarse según sea necesario)
denoised_image = cv2.medianBlur(output_image, kernel_size)

# Guardar la imagen denoised
cv2.imwrite('output_image.png', output_image)