from pingDatos.ping import Ping
from ports.puertos import Puertos
import openpyxl



with open("/home/Python/proyecto/check/servicio/pingDatos/CAJ-lista2", "r") as datos:
    lista = [linea.rstrip() for linea in datos]    



listaValidada = Ping.ipValidaLista(lista)


book =openpyxl.load_workbook('/home/Python/proyecto/validacion/nmapVenv/store/validacion.xlsx')
sheet = book['levantamiento']
contador=1
for ip in listaValidada:
    datos=Puertos.validarPuertos(ip)
    contador=contador+1
    
    sheet[f'A{contador}']=ip
    sheet[f'B{contador}']=datos[0]
    sheet[f'C{contador}']=datos[1]
    
    
    book.save(f'/home/Clientes/CAJ/levantamiento_lista2.xlsx')
    print('DATOS INGRESADOS') 
                 

    
