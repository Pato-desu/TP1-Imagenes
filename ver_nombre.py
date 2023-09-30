import cv2
import numpy as np
import matplotlib.pyplot as plt

# def ver_nombre(img):
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

plt.imshow(img, cmap='gray')
plt.plot(xx,yy, c='r')
plt.show()
# ********************************
# xx = np.arange(img.shape[0])
# yy = np.zeros(img.shape[0])
# yy[renglones_indxs] = (img.shape[1]-1)
# plt.imshow(img, cmap='gray')
# plt.plot(yy, xx, c='r')
# plt.show()
# x_indxs = renglones_indxs[:(len(renglones_indxs)//2)*2]
# x_indxs = x_indxs.reshape((-1,2))
# # Obtengo renglones 
# renglones = []
# for ir, idxs in enumerate(x_indxs):
#     # renglones.append(img[idxs[0]:idxs[1],:])
#     renglones.append({
#         "ir": ir+1,
#         "cord": idxs,
#         "img": img[idxs[0]:idxs[1],:]
#     })

# plt.figure()
# for ii, renglon in enumerate(renglones):
#     plt.imshow(renglon["img"], cmap='gray')
#     plt.title(f"Renglón {ii+1}")
# plt.show()

# # --- Analizo en renglones -----------------------------------------------------
# letras = []
# for ir, renglon in enumerate(renglones):
#     renglon_zeros = renglon["img"]==0  # Acondiciono imagen...

#     # --- Analizo columnas del renglón ------------------------------
#     ren_col_zeros = renglon_zeros.any(axis=0)
#     ren_col_zeros_idxs = np.argwhere(renglon_zeros.any(axis=0))
#     # *** Show *************************************
#     plt.figure()
#     plt.imshow(renglon_zeros, cmap='gray')
#     xc = np.arange(renglon_zeros.shape[1])
#     yc = ren_col_zeros*(renglon_zeros.shape[0]-1)
#     plt.plot(xc, yc, c='b')
#     plt.title(f"Renglón {ir+1}")
#     plt.show()

# # --- Separo en letras ------------------------------------------
# x = np.diff(ren_col_zeros)
# letras_indxs = np.argwhere(x) 
# # *** Modifico índices ***********
# ii = np.arange(0,len(letras_indxs),2)
# letras_indxs[ii]+=1
# # ********************************
# # Re-ordeno los índices en grupos de a 2 (inicio-final)
# letras_indxs = letras_indxs[:(len(letras_indxs)//2)*2]
# letras_indxs = letras_indxs.reshape((-1,2))

# # Obtengo letras del renglon
# letras_ren = []
# for idxs in letras_indxs:
#     letras_ren.append(renglon["img"][: , idxs[0]:idxs[1]])

# # *** Show ********************************************
# plt.figure()
# Nrows = len(letras_ren)//4 + len(letras_ren)%4
# plt.suptitle(f"Renglón {ir+1}")
# for ii, letra in enumerate(letras_ren):
#     plt.subplot(Nrows, 4, ii+1)
#     plt.imshow(letra, cmap='gray')
#     plt.title(f"letra {ii+1}")
# plt.show()
# # ******************************************************

# ver_nombre('prueba_bw123.png')