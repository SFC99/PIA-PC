import subprocess
import argparse
import WebScraping
import Correo
import Metadata
import ValorHash
import Scan

parser = argparse.ArgumentParser(description='Argumentos para la herramienta de ciberseguridad.')


parser.add_argument("-wS","--webScraping", help="Iniciar webscraping.", action="store_true")
parser.add_argument("-s", "--Sitio", help="Sitio para hacer webscraping.", )

parser.add_argument("-pS","--Scan", help="Escaneo de puertos.", action="store_true")

parser.add_argument("-oM", "--obtMetadatos", help="Obtención de meta datos", action="store_true")
parser.add_argument("-r", "--ruta", help="La ruta absoluta de donde se obtendra la metadata")

parser.add_argument("-e", "--enviar_correo", help="Envio de correos", action="store_true")

parser.add_argument("-vH", "--valorHash", help="Obtencion de valor Hash.", action="store_true")
parser.add_argument("-f", "--file", help="Nombre del documento")

parser = parser.parse_args()


if parser.webScraping:
    print("Webscraping\n")
    sitio = parser.Sitio
    print(f"{sitio}")
    try:
        WebScraping.WebScrapping(sitio)
    except:
        print("\n\t Algo salio mal")

elif parser.Scan:
    print("Puertos\n")

    print("Completado")

elif parser.obtMetadatos:
    print("Metadatos\n")
    try:
        Metadata.printmeta(parser.ruta)
    except:
        print("\n\t Algo salió mal")


elif parser.valorHash:
    print("Valor hash\n")
    try:
        ValorHash.Hash(parser.file)
    except:
        print("\n\t Algo salió mal")


elif parser.enviar_correo:
    print("Correos.\n")
    Correo.Envio_Correo()
