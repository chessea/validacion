from pingDatos.ping import Ping
from ports.puertos import Puertos
import openpyxl



lista = ['10.0.0.1', '10.0.0.1','8.8.8.8']
listaValidada = Ping.ipValidaLista(lista)


book =openpyxl.load_workbook('/home/fr/Documentos/validacion/nmapVenv/store/validacion.xlsx')
sheet = book['levantamiento']
contador=1
for ip in listaValidada:
    datos=Puertos.validarPuertos(ip)
    contador=contador+1
    
    sheet[f'A{contador}']=ip
    sheet[f'B{contador}']=datos[0]
    sheet[f'C{contador}']=datos[1]
    
    
    book.save(f'/home/fr/Documentos/validacion/nmapVenv/store/levantamiento.xlsx')
    print('DATOS INGRESADOS') 
                 

    
