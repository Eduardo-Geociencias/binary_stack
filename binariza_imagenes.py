"""
Programa que binariza una coleccion de imagenes .png contenidas en una carpeta
"""

import cv2
import os

# path de la carpeta que contiene las imágenes
input_images_path = r"C:\Users\eduar\Desktop\Recorta_imagenes\0 Prismas Porosidad\HJ1468-P_porosidad_efectiva"

# lista con todos los archivos dentro del path
files_names = os.listdir(input_images_path)
# print(files_names)

# Creamos una nueva carpeta donde guardaremos las imágenes procesadas
output_images_path = r"C:\Users\eduar\Desktop\Recorta_imagenes\Prismas binarizados\HJ1468-P_porosidad_efectiva"

# salta al siguiente, en caso de encontrar un archivo que no es una imagen
if not os.path.exists(output_images_path):
    os.makedirs(output_images_path)
    print('Directorio creado: ', output_images_path)

# Declaramos un contador para renombrar c/u de las imágenes procesadas
count = 0

# Leemos cada uno de los elementos de la lista que están en la carpeta
for file_name in files_names:
    # Construimos el path donde se encuentran c/u de las imágenes
    image_path = input_images_path + "/" + file_name
    # Leemos cada una de estas imágenes y las binarizamos con el cero
    img_gris = cv2.imread(image_path, 0)
    # En caso de haber un archivo que no es imagen, brincamos al sig.
    if img_gris is None:
        continue
    
    ###########################################################################
    # Obtenemos el valor del unbral con el método de Otsu
    umbral, img_bin = cv2.threshold(img_gris,0,255, cv2.THRESH_OTSU)
    
    # Guardamos cada una de las imágenes procesadas 
    # usando el contador "count" y especificando el tipo de archivo .png
    # Guardamos las imagenes con el nombre deseado
    file_name = "/HJ1468-P_ef_{:04d}.png".format(count)
    cv2.imwrite(output_images_path + file_name, img_bin)
    
    count += 1
    
    # Visualizamos cada una de las imágenes
#     cv2.imshow("Image", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()






