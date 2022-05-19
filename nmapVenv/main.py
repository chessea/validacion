from servicios.filtro.funcionesFiltros import FuncionesFiltro
from servicios.netmiko.comando import Comando
from pingDatos.ping import Ping
from ports.puertos import Puertos
import openpyxl
from bullet import VerticalPrompt, Input, Password


print("Inicio")
cli= VerticalPrompt([
    Input(prompt="Ingrese usuario: "),
    Password(prompt="Ingrese password : ", hidden="*")],spacing=0)
result=cli.launch()

usuario=result[0][1]
password=result[1][1]



with open("/home/Python/Test/CAJ-telnet-hosts", "r") as datos:
    lista = [linea.rstrip() for linea in datos]    



listaValidada = Ping.ipValidaLista(lista)


book =openpyxl.load_workbook('/home/Python/git-proyect/validacion/nmapVenv/store/validacion.xlsx')
sheet = book['levantamiento']
contador=1
for ip in listaValidada:
    
    listaComandos=['sh run']  
    comando=Comando.enviarComando(listaComandos,ip, usuario, password)
      
    ott=FuncionesFiltro.filtroOTT(comando)
    cs=FuncionesFiltro.filtroCS(comando)
    print(ott)    
    
    datos=Puertos.validarPuertos(ip)
    contador=contador+1
    
    sheet[f'A{contador}']=ip
    sheet[f'B{contador}']=datos[0]
    sheet[f'C{contador}']=datos[1]
    sheet[f'D{contador}']=ott
    sheet[f'E{contador}']=cs
    
    
    book.save(f'/home/Clientes/CAJ/levantamientoPruebas.xlsx')
    print('DATOS INGRESADOS') 
                 

    
