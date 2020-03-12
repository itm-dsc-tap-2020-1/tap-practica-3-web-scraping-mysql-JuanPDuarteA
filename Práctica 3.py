from urllib.request import urlopen
from bs4 import BeautifulSoup
import mysql.connector as mysql
from tkinter import messagebox as mBox

def guardar(pagina_inicial):
    try:
        url=urlopen(pagina_inicial)
        bs=BeautifulSoup(url.read(),'html.parser')
    except:
        return

    for enlaces in bs.find_all("a"):
        try:
            print("Enlace hallado: "+str(enlaces.get("href")))
            try:
                operacion.execute("INSERT into Informacion values('"+str(enlaces.get('href'))+"','"+str(False)+"' );")
            except mysql.errors.DataError:
                pass
            print(enlaces.get("href"))
            conexion.commit()
        except mysql.errors.IntegrityError:    
            pass
cont=0
conexion = mysql.connect( host='localhost', user= 'root', passwd='', db='Practica_3' )
operacion = conexion.cursor()
pagina_inicial=input("Ingresar página: ")
operacion.execute("update Informacion set status=True where pagina='"+pagina_inicial+"';")
guardar(pagina_inicial)
while(True):
    operacion.execute("select * from Informacion;")
    for pag,est in operacion.fetchall():
        if est=="False":
            guardar(pag)
            operacion.execute("update Informacion set status="+str(True)+" where pagina='"+pag+"';")
            cont+=1
    if cont==200:
        break
