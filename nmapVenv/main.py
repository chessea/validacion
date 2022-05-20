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
usuario='franco'
password='cisco'
book =openpyxl.load_workbook('/home/fr/unitarias-git/validacion/nmapVenv/store/validacion.xlsx')
sheet = book['levantamiento']
contador=1
for ip in listaValidada:
    try:    
        listaComandos=['sh run', 'sh inventory | i PID',
                       'show run | i router',
                       'sh ip interface brief | i  Loopback0',
                       'sh ip interface brief | i 40',
                       'sh ip interface brief | i Vlan1',
                       'sh ip interface brief | i GigabitEthernet0/1',
                       'sh ip interface brief | i GigabitEthernet0/0/1'
                       ]  
        comando=Comando.enviarComando(listaComandos,ip, usuario, password)
        shRun, shModel,shRouter,shLoop, shVlan40, shVlan1, shVlan1A, shVlan1B= comando
    
        ott=FuncionesFiltro.filtroOTTs(shRun)
        cs=FuncionesFiltro.filtroCSs(shRun)
        modelo= FuncionesFiltro.filtroModel(shModel)
        router= FuncionesFiltro.filtroProtocolo(shRouter)
        loopback= FuncionesFiltro.filtroLoop(shLoop)
        vlan40= FuncionesFiltro.shVlan40(shVlan40)
        vlan1= FuncionesFiltro.shVlan1(shVlan1,shVlan1A,shVlan1B)


        datos=Puertos.validarPuertos(ip)
        contador=contador+1

        sheet[f'A{contador}']=ip
        sheet[f'B{contador}']=datos[0]
        sheet[f'C{contador}']=datos[1]
        sheet[f'D{contador}']=ott
        sheet[f'E{contador}']=cs
        sheet[f'F{contador}']=modelo
        sheet[f'G{contador}']=router
        sheet[f'H{contador}']='CORP.A.JUD'
        sheet[f'I{contador}']=loopback
        sheet[f'J{contador}']=vlan40
        sheet[f'K{contador}']=vlan1


        book.save(f'/home/fr/unitarias-git/validacion/nmapVenv/store/levantamientoPruebas.xlsx')
        print('DATOS INGRESADOS') 
                 
    except Exception as e:
        print('ERROR')
    
