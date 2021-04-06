from PIL import Image, ImageDraw, ImageFont
import math

shade = " .:;"[::-1]
shadeArray = list(shade)
shadeLen = len(shadeArray)
interval = (shadeLen/256)

#text_file = open("Output.txt", "w")

imagen = Image.open("gamer.png") #abre la imagen de esteban
x, y = imagen.size #saco la altura y ancho de la imagen
foto = imagen.load() #carga la imagen de esteban en una variable

for height in range(y):
    for width in range(x):
        r, g, b, a  = foto[width, height] #saco el RGB del pixel a convertir
        if r > 200 and g > 200 and b > 200:
            foto[width, height] = (r, g, b, 0)    

    
imagen.save("truepng.png")
