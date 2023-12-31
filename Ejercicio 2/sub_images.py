import cv2
import numpy as np
import matplotlib.pyplot as plt 
from plot_suma import plot_pix_sumat

def sub_images(nom_archivo):
    # --- Cargo imagen ------------------------------------------------------------
    img = cv2.imread(nom_archivo, cv2.IMREAD_GRAYSCALE) 
    plt.imshow(img, cmap='gray')
    plt.show(block=False)

    # Binarizar la imagen (convertirla a blanco y negro)
    _, img_bw = cv2.threshold(img, 90, 255, cv2.THRESH_BINARY)
    # plt.imshow(img_bw, cmap='gray')
    # plt.show(block=False)

    img_zeros = img_bw==0
    #plt.imshow(img_zeros, cmap='gray'), plt.show()
    img_zeros = img_zeros*1

    suma_por_columna = np.sum(img_zeros, axis=0)
    suma_por_fila = np.sum(img_zeros, axis=1)

    #plot_pix_sumat(img_zeros, suma_por_columna, suma_por_fila)

    aux_columna = list(enumerate(suma_por_columna))
    column_high = sorted(aux_columna, key = lambda x: x[1], reverse=True)
    column_high = column_high[:4]
    column_high = sorted(column_high, key = lambda x: x[0], reverse=False)

    aux_fila = list(enumerate(suma_por_fila))
    row_high = sorted(aux_fila, key = lambda x: x[1], reverse=True)
    row_high = row_high[:11]
    row_high = sorted(row_high, key = lambda x: x[0], reverse=False)

    #NYA 1,1
    nombre_apellido = img_bw[row_high[1][0]+2:row_high[2][0]-2,column_high[1][0]+2:column_high[3][0]-2]
    #EDAD 2,1
    edad = img_bw[row_high[2][0]+2:row_high[3][0]-2,column_high[1][0]+2:column_high[3][0]-2]
    #MAIL 3,1
    mail = img_bw[row_high[3][0]+2:row_high[4][0]-2,column_high[1][0]+2:column_high[3][0]-2]
    #LEGAJO 4,1
    legajo = img_bw[row_high[4][0]+2:row_high[5][0]-2,column_high[1][0]+2:column_high[3][0]-2]
    #P1 SI 6,1  #HASTA 6,2
    p1_si = img_bw[row_high[6][0]+2:row_high[7][0]-2,column_high[1][0]+2:column_high[2][0]-2]
    #P1 NO 6,2
    p1_no = img_bw[row_high[6][0]+2:row_high[7][0]-2,column_high[2][0]+2:column_high[3][0]-2]
    #P2 SI 7,1  #HASTA 7,2      
    p2_si = img_bw[row_high[7][0]+2:row_high[8][0]-2,column_high[1][0]+2:column_high[2][0]-2]
    #P2 NO 7,2
    p2_no = img_bw[row_high[7][0]+2:row_high[8][0]-2,column_high[2][0]+2:column_high[3][0]-2]
    #P3 SI 8,1  #HASTA 8,2
    p3_si = img_bw[row_high[8][0]+2:row_high[9][0]-2,column_high[1][0]+2:column_high[2][0]-2]
    #P3 NO 8,2
    p3_no = img_bw[row_high[8][0]+2:row_high[9][0]-2,column_high[2][0]+2:column_high[3][0]-2]
    #COMENTARIOS 9,1
    comentarios = img_bw[row_high[9][0]+2:row_high[10][0]-2,column_high[1][0]+2:column_high[3][0]-2]

    renglones = {"Nombre y Apellido": nombre_apellido, "Edad": edad, "Mail": mail,
              "Legajo": legajo, "Pregunta 1":[p1_si,p1_no], "Pregunta 2":[p2_si,p2_no],
              "Pregunta 3":[p3_si,p3_no], "Comentarios": comentarios}
    
    return renglones