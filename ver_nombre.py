import cv2
import numpy as np
import matplotlib.pyplot as plt

def ver_nombre(img):
    #Identifica letras
    img = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
    img_zeros = img == 0
    img_row_zeros = img_zeros.any(axis=1)
    x = np.diff(img_row_zeros)
    renglones_indxs = np.argwhere(x) 
    # *** Modifico índices ***********
    ii = np.arange(0,len(renglones_indxs),2)
    renglones_indxs[ii]+=1
    # ********************************
    xx = np.arange(img.shape[0])
    yy = np.zeros(img.shape[0])
    yy[renglones_indxs] = (img.shape[1]-1)
    plt.imshow(img, cmap='gray')
    plt.plot(yy, xx, c='r')
    plt.show()
    x_indxs = renglones_indxs[:(len(renglones_indxs)//2)*2]
    x_indxs = x_indxs.reshape((-1,2))
    # Obtengo renglones 
    renglones = []
    for ir, idxs in enumerate(x_indxs):
        # renglones.append(img[idxs[0]:idxs[1],:])
        renglones.append({
            "ir": ir+1,
            "cord": idxs,
            "img": img[idxs[0]:idxs[1],:]
        })

    plt.figure()
    for ii, renglon in enumerate(renglones):
        plt.imshow(renglon["img"], cmap='gray')
        plt.title(f"Renglón {ii+1}")
    plt.show()

    # --- Analizo en renglones -----------------------------------------------------
    letras = []
    for ir, renglon in enumerate(renglones):
        renglon_zeros = renglon["img"]==0  # Acondiciono imagen...

        # --- Analizo columnas del renglón ------------------------------
        ren_col_zeros = renglon_zeros.any(axis=0)
        ren_col_zeros_idxs = np.argwhere(renglon_zeros.any(axis=0))
        # *** Show *************************************
        plt.figure()
        plt.imshow(renglon_zeros, cmap='gray')
        xc = np.arange(renglon_zeros.shape[1])
        yc = ren_col_zeros*(renglon_zeros.shape[0]-1)
        plt.plot(xc, yc, c='b')
        plt.title(f"Renglón {ir+1}")
        plt.show()

ver_nombre('pruebabw123.png')