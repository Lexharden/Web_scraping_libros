import bs4

import requests

# --------------------------------------------------------------------------------
# Obtener imagenes y descargar y guardar
resultado = requests.get('https://www.escueladirecta.com/courses')
sopa = bs4.BeautifulSoup(resultado.text, 'lxml')
imagenes = sopa.select('.course-box-image')[0]['src']
print(imagenes)
imagen_descarga_1 = requests.get(imagenes)
f = open('../Mi_imagen.jpg', 'wb')
f.write(imagen_descarga_1.content)
f.close()

# print(imagen_descarga_1.content)
# for i in imagenes:
#     print(i)

# OBTENER DATOS DE PARRAFOS Y MAS
# --------------------------------------------------------------------------------
# resultado = requests.get('https://escueladirecta.com/p/analisis-de-datos-con-pandas-y-python')
# sopa = bs4.BeautifulSoup(resultado.text, 'lxml')
# columna_lateral = sopa.select('.course-description p')
# for p in columna_lateral:
#     print(p.getText())
# --------------------------------------------------------------------------------
# parrafo_especial = sopa.select('p')[3].getText()
# print(sopa.select('title')[0].getText())
