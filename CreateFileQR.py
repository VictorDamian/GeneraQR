#################################
##--- VictorDamian
##--- Python 3.7.8 - os - qrcode
#################################

import os
import qrcode

class GenerateQR:
    def __init__(self, pathImgs, pathFile, nameFile):
        self._pathImgs = pathImgs
        self._pathFile = pathFile
        self._nameFile = nameFile

    # Obtine el texto de cada linea dentro de un fichero
    def GetListTxt(self):
        _file = (self._pathFile)
        with open(_file) as f:
            _file = f.read().splitlines()
        return _file

    # Obtine una lista de los archvisp de un directorio
    def GetListImgs(self):
        _listImg = os.listdir(self._pathImgs)
        listAux =[]
        for i in _listImg:
            # delimita
            id = i.split('.png')
            # retorna solo el indice seleccionado
            listAux.append(id[0])
        return print(listAux)
        
    # Escribe dentro de un fichero
    def WriteInFile(self):
        try:
            file = open(self._pathFile, "a")
            file.write(self._nameFile+'\n')
        finally:
            file.close()

    # Genera una imagen QR
    def CreateQR(self):
        img = qrcode.make(self._nameFile)
        f = open('img/'+str(self._nameFile)+".png", "wb")
        GenerateQR.WriteInFile(self)
        img.save(f)
        f.close()    

    # Crea el QR segun las validaciones
    def ValidateExist(self):
        lista = GenerateQR.GetListTxt(self)
        print('Registros existentes:')
        print(lista)
        try:
            oList = lista.index(self._nameFile)
            print("El id ya existe en el indice: {}".format(oList))
        except:
            GenerateQR.CreateQR(self)
            print("El archivo se ha generado")

qr = GenerateQR(
    pathFile='yourFile.txt',
    pathImgs='yourDirFile/', 
    nameFile='yourID')
qr.ValidateExist()