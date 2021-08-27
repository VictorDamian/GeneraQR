# Genera un archivo QR
## Librerias utilizadas
>qrcode

>os

qrcode para su instalacion con el siguiente comando:

>pip install qrcode

Mas inforcación sobre qrcode en la pagina de [Python](https://pypi.org/project/qrcode/)

## Su funcionamiento es el siguiente:

### Metodo GetListTxt

Lee cada linea de texto que se encuentra en un fichero y nos retorna dichas lineas.

### Metodo GetListImgs

Obtine una lista con todos los archivos existentes de un directorio, esto nos devolvera el nombre de los archivos, sin embargo nos los proporciona con su extension, para ello necesitamos solo guardar su nombre, con el metodo `split` delimitamos lo que queremos que omita en este caso `.png` ó `.jpg` segun su formato. Despues agrega a una nueva lisata el indice donde se encuentra solo el nombre del archivo.

Se puede trabajar con cualquiera de los dos metodos, su funcionamiento es el mismo, obtener una lista existe de su contenido en un fichero o en un directorio.

### Metodo WriteInFile

Su funcion es sobre escribir en el fichero, en el siguiente metodo se explica mas a detalle su propisito.

### Metodo CreateQR

Genera una imagen QR que a su vez implementa el metodo `WriteInFile`

### Metodo ValidateExist

Este metodo se encarga de verificar si es que existe un id dentro del fichero, si es asi, manda un mensaje en consola de que ya existe, de lo contrario crea el archivo utilizando el metodo `CreateQR` que a su vez, este sobre escribe en el fichero el nuevo QR generado.