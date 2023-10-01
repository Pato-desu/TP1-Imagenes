import cv2
import numpy as np
import matplotlib.pyplot as plt

def ver_nombre(img):
#Identifica letras
    img = cv2.imread('prueba_bw123.png', cv2.IMREAD_GRAYSCALE)
    img_zeros = img == 0

    img_row_zeros = img_zeros.any(axis=1)
    x = np.diff(img_row_zeros)
    renglones_indxs = np.argwhere(x) 
    # *** Modifico índices ***********
    ii = np.arange(0,len(renglones_indxs),2) 
    renglones_indxs[ii]+=1

    img_columns_zeros = img_zeros.any(axis=0)
    y = np.diff(img_columns_zeros)
    columns_indxs = np.argwhere(y) 
    # *** Modifico índices ***********
    jj = np.arange(0,len(columns_indxs),2)
    columns_indxs[jj]+=1

    xx = np.arange(img.shape[1])
    yy = np.zeros(img.shape[1])
    yy[columns_indxs] = (img.shape[0]-1)
    
    letras_indices = []
    letras = []
    for i in range(0, len(columns_indxs), 2):
        letras_indices.append((columns_indxs[i][0], columns_indxs[i+1][0]))
        letras.append(img[renglones_indxs[0][0]:renglones_indxs[1][0], columns_indxs[i][0]:columns_indxs[i+1][0]])
    
    print(letras_indices)

    palabras_indices = []
    palabras=[]
    inicio = letras_indices[0][0]
    for j in range(len(letras_indices)-1):
        if letras_indices[j+1][0] - letras_indices[j][1] < 11:
            fin = letras_indices[j+1][1]
        else:
            fin = letras_indices[j][1]
            palabras_indices.append((inicio, fin))
            palabras.append(img[renglones_indxs[0][0]:renglones_indxs[1][0], inicio:fin])
            inicio = letras_indices[j+1][0]

    print(palabras_indices)

    return cant_palabras, cant_letras

ver_nombre('prueba_bw123.png')