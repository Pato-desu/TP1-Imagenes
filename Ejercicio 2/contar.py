import cv2
import numpy as np
import matplotlib.pyplot as plt

def contar_caracteres_y_palabras(img):
#Identifica caracteres
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
    
    caracteres_indices = []
    caracteres = []
    for i in range(0, len(columns_indxs), 2):
        caracteres_indices.append((columns_indxs[i][0], columns_indxs[i+1][0]))
        caracteres.append(img[renglones_indxs[0][0]:renglones_indxs[1][0], columns_indxs[i][0]:columns_indxs[i+1][0]])

    palabras_indices = []
    palabras=[]
    if caracteres_indices == []:
        return 0,0
    
    if len(caracteres) == 1:
        return 1,1
    
    inicio = caracteres_indices[0][0]
    espacios = []
    
    for j in range(len(caracteres_indices)-1):
        if j == len(caracteres_indices)-2:
            fin = caracteres_indices[j+1][1]
            palabras_indices.append((inicio, fin))
            palabras.append(img[renglones_indxs[0][0]:renglones_indxs[1][0], inicio:fin])
            break
        elif caracteres_indices[j+1][0] - caracteres_indices[j][1] < 11:
            fin = caracteres_indices[j+1][1]
        else:
            espacios.append((caracteres_indices[j][1], caracteres_indices[j+1][0]))
            fin = caracteres_indices[j][1]
            palabras_indices.append((inicio, fin))
            palabras.append(img[renglones_indxs[0][0]:renglones_indxs[1][0], inicio:fin])
            inicio = caracteres_indices[j+1][0]

    return len(caracteres+espacios),len(palabras)