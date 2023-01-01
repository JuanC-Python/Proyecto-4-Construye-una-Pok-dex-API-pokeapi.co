import requests
import matplotlib.pyplot as plt
from PIL import Image
from urllib.request import urlopen


pokemon = input ("Introduce el nombre del pokemon: ").lower()

url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
respuesta = requests.get(url, timeout=20)
if respuesta.status_code !=200:
    print("Pokémon no encontrado")
    exit()
else:
    print(respuesta)

#plt.figure(figsize=(100,4))
plt.subplots(figsize=(15, 6))# Tamaño del frame de matplotlib para poder mostrar la información completa del pokemon
plt.subplots_adjust(left=0.195,bottom=0.329)
datos = respuesta.json()
nombre = datos['name']
print(nombre)

peso = datos['weight']
print (peso)
plt.text(-100, 0, "Peso:",fontsize=8,color='red')
plt.text(-100, 5, peso,fontsize=8,color='blue')

tamaño = datos['height']
print (tamaño)
plt.text(-80, 0, "Tamaño:",fontsize=8,color='red')
plt.text(-80, 5, tamaño,fontsize=8,color='blue')

movimientos = datos['moves']
contador0=1
plt.text(-60, 0, "Movimientos:",fontsize=8,color='red')
for i in range(int(len(movimientos))):
    movimiento = movimientos[i]['move']['name']
    contador0 = contador0 + 5
    print(movimiento)
    plt.text(-60, contador0, movimiento,fontsize=8,color='blue')
    
habilidades = datos['abilities']
contador1=1
plt.text(-30, 0, "Habilidades:",fontsize=8,color='red')
for i in range(int(len(habilidades))):
    habilidad = habilidades[i]['ability']['name']    
    contador1 = contador1 + 5
    print(habilidad)   
    plt.text(-30, contador1, habilidad,fontsize=8,color='blue')
    
tipos = datos['types']
contador2=1
plt.text(-8, 0, "Tipos:",fontsize=8,color='red')
for i in range(int(len(tipos))):
    tipo = tipos[i]['type']['name']
    contador2 = contador2 + 5
    print(tipo)
    plt.text(-8, contador2, tipo,fontsize=8,color='blue')
    
url_imagen = datos['sprites']['front_default']
imagen = Image.open(urlopen(url_imagen))
plt.title(datos['name'])
imgplot = plt.imshow(imagen)
plt.axis('off')
plt.show()

with open('C:/Users/jlope/Python/UCAMP_FPYTHON/Clases_Modulo4/pokedex/pokemon.json','w') as f_archivo:
    f_archivo.write(str(nombre)+"\n")
    f_archivo.write("\n"+str(peso))
    f_archivo.write("\n"+str(tamaño))
    f_archivo.write("\n"+str(movimientos))
    f_archivo.write("\n"+str(habilidades))
    f_archivo.write("\n"+str(tipos))
    f_archivo.write("\n"+str(url_imagen))
  
# with open('C:/Users/jlope/Python/UCAMP_FPYTHON/Clases_Modulo4/pokedex/pokemon.json','a') as f_lectura:
#     print(f_lectura.read())
