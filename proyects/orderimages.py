from os.path import expanduser
import os
import shutil

home = expanduser("~") #asigna el HOME
directory = home+"/Pictures/" #directorio al cual buscara los archivos
destino = home+"/Pictures/gifs/" #directorio de destino
destino2= home+"/Pictures/imagenes/"

if (os.path.isdir(home+"/Pictures/gifs/")) == False or (os.path.isdir(home+"/Pictures/imagenes/")) == False:
    try:
        os.mkdir(home+"/Pictures/gifs/")
        print("Se ha creado el directorio gifs")
    except:
        print("El directorio gifs ya existe")
    try:
        os.mkdir(home+"/Pictures/imagenes/")
        print("Se ha creado el directorio imagenes")
    except:
        print("El directorio imagenes ya existe")

for file in os.listdir(directory):
    filePath = (directory+file)
    if file.endswith(".gif"):
        shutil.move(filePath, destino)
    if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"):
        shutil.move(filePath, destino2)
