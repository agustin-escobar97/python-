from PIL import Image, ImageDraw, ImageFont
import math

shade = " .:-=+*#%@"[::-1]
shadeArray = list(shade)
shadeLen = len(shadeArray)
interval = (shadeLen/256)

reescalado = 0.5

def getShade(inputInt):
    return shadeArray[math.floor(inputInt*interval)]

text_file = open("Output.txt", "w")

imagen = Image.open("esteban.png") #abre la imagen de esteban
x, y = imagen.size #saco la altura y ancho de la imagen
imagen = imagen.resize((int(reescalado*x), int(reescalado*y)), Image.NEAREST)
x, y = imagen.size
foto = imagen.load() #carga la imagen de esteban en una variable

for height in range(y):
    for width in range(x):
        r, g, b, a  = foto[width, height] #saco el RGB del pixel a convertir
        gris = int((r + g + b)/3) #dividir el RGB por 3 me da una escala de gris
        foto[width, height] = (gris, gris, gris)
        text_file.write(getShade(gris))
    
    text_file.write("\n")
imagen.save("estebangris.png")
