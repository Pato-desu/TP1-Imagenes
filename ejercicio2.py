import cv2
import numpy as np
import matplotlib.pyplot as plt 

#CONTAR ESPACIO

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
    inicio = caracteres_indices[0][0]

    for j in range(len(caracteres_indices)-1):
        if j == len(caracteres_indices)-2:
            fin = caracteres_indices[j+1][1]
            palabras_indices.append((inicio, fin))
            palabras.append(img[renglones_indxs[0][0]:renglones_indxs[1][0], inicio:fin])
            break
        elif caracteres_indices[j+1][0] - caracteres_indices[j][1] < 11:
            fin = caracteres_indices[j+1][1]
        else:
            fin = caracteres_indices[j][1]
            palabras_indices.append((inicio, fin))
            palabras.append(img[renglones_indxs[0][0]:renglones_indxs[1][0], inicio:fin])
            inicio = caracteres_indices[j+1][0]

    return len(caracteres),len(palabras)

def check(linea, n_car, n_pal):
    match linea:
        case 1:  
            if n_pal > 1 and n_car < 26:
                return True
            
        case 2:
            if n_car in [2, 3]:
                return True
        
        case 3:
            if n_pal == 1 and n_car < 26:
                return True
                
        case 4:
            if n_pal == 1 and n_car == 8:
                return True
        
        case 5 | 6 | 7:                 
            if n_car == 1: 
                return True
                    
        case 8:
            if n_car < 26:
                return True       
            
    return False

def check_y_print(nombre_archivo):
    print('\n' + nombre_archivo + ':\n')

    renglones = sub_images(nombre_archivo)

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

#check_y_print('formulario_vacio.png')

for i in range(1, 6):
    check_y_print(f'formulario_0{i}.png')
