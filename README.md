# Proyecto final: Herramientas de ciberseguridad
Este repositorio muestra el proyecto final de Programacion para ciberseguridad. Grupo 062 E2022.


Este codigo tiene la finalidad de ejecutar las herramientas mediante un archivo main en conjunto del uso de funciones, importando clases y módulos vistos en clase. Las herramientas son las siguientes:

```
-PortScanner
-WebScrapping
-Envío de correos
-Valores Hash
-Obtencion de Metadatos

```

## Librerías

Para la ejecución de las herramientas se necesitan tener lo siguiente:

- BeautifulSoup
``` 
          pip install beautifulsoup4
```
- Pillow
```
          pip install pillow
```

## Como ejecutarlo

###### CMD
```
1.-Abrir CMD
2.-Ingresar el path de la carpeta de los archivos correspondientes. (Utiliza el comando cd)
3.-Ingresar los argumentos seguido de la llamada del archivo main, esto cambia dependiendo de la herramienta a ejecutar:

    a.PortScanner:
        ' [path de la carpeta]: python main.py -pS '
       
    b.WebScrapping:
        ' [path de la carpeta]: python main.py -wS -s *Link* '
        
    c.Envio de correos
        ' [path de la carpeta]: python main.py -e '
        
    d.Valores Hash:
        ' [path de la carpeta]: python main.py -vH -f *Nombre del archivo* '
         
    e.Obtencion de Metadatos:
    
         ' [path de la carpeta]: python main.py -oM -r *Path del archivo* '
  ```       

###### LINUX
```
1.-Abrir terminal
2.-Brindar permisos de ejecucion a los archivos:
      $ chmod +x *nombre del archivo.extension* 
3.-Agregar shebang en cada archivo
      #!/usr/bin/env python3
4.Llamar el archivo main seguido de los argumentos requeridos segun la herramienta a ejecutar
      a.PortScanner:
          $ python main.py -pS
          
      b.WebScrapping:
          $ python main.py -wS -s *Link*
          
      c.Envío de correos
          $ python main.py -e
          
      d.Valores Hash:
          $ python main.py -vH -f *Nombre del archivo*
          
      e.Obtencion de Metadatos:
          $ python main.py -oM -r *Path del archivo*
```  

###### Integrantes:
```
@EricGallegosHdz
@SFC99
@Sand0G0d
```
