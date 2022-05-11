import socket
import sys

hostname = socket.gethostname()

ip_address = socket.gethostbyname(hostname)
print(ip_address)

def portScan(ip,portlist):
    print("IP", ip, type(ip))
    try:
        for port in portlist:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            result = sock.connect_ex((ip, port))
            if result == 0:
                print("Puerto (): \t Abierto".format(port))
            else:
                print("Puerto (): \t Cerrado".format(port))
            sock.close()
    except socket.error as error:
        print(str(error))
        print("Error de conexion")
        sys.exit()
