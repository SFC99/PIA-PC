import requests
from bs4 import BeautifulSoup


def Basic_Info(url):
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')
    title_name = soup.title.string
    title_parent = soup.title.parent.name

    print('\n Basic information:')
    print('\n\t Title name: ', title_name)
    print('\n\t Title parent: ', title_parent)


def respuesta(url):
    r = requests.get(url)
    if r.status_code == 200:
        return 1
    else:
        return 0


def Links(url):
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')
    title_name = soup.title.string
    fo = open(f"{title_name}.txt", "a")
    for link in (soup.find_all('a')):
        if (link.get('href')) is not None:
            enlace = link.get('href')
            fo.write(f"\n {enlace} \n")
            print('\t ', link.get('href'))
    fo.close()


def WebScrapping(ip):
    try:
        pStatus = url_Status(ip)
        if pStatus == 1:
            cont = False
        else:
            input("\n La pagina no responde. Por favor presiona enter.")
    except:
        input('\n Algo salio mal.')

    Basic_Info(ip)
    print("\n Todos los links en la pagina \n")
    Find_Links(ip)
