import os

from servicios.filtro.funcionesFiltros import FuncionesFiltro




FuncionesFiltro


class FiltroNetmiko:
    
    @classmethod
    def obtenerOTT(cls,comandoShRun):
        ott=FuncionesFiltro.filtroOTT(comandoShRun)   
        return ott  
    
    @classmethod
    def obtenerCS(cls,comandoShRun):
        cs=FuncionesFiltro.filtroCS(comandoShRun)   
        return cs      
    
            
    @classmethod
    def obtenerHostName(cls, comandoShRun):
        hostname=comandoShRun[0].split(' ')
        del(hostname[0])
        if len(hostname)>0:
            return hostname[0]
        else:
            return 'Sin Datos'
     
     
    @classmethod
    def obtenerModelo(cls, comoandoModelo):
        modelo=comoandoModelo[0].split(' ')
        if len(modelo)>0:
            return modelo[4]
        else:
            return 'Sin Datos'
    
    @classmethod
    def obtenerSNMP(cls, comandoSnmp):
        snmp=comandoSnmp[0].split(' ')
        if len(snmp)>0:
            return snmp[2]
        else:
            snmp="Sin Datos"
            return snmp   
        
    @classmethod
    def  filtroInterface(cls,comandoShRun):
        busquedaINT = ["0/0/0","0/0","0/4"]
        for litadoBusqueda in busquedaINT:
            filtroINT = [s for s in comandoShRun if litadoBusqueda in s]
            if filtroINT==[]:
                pass
            else:    
                filtroListaINT=filtroINT[0].split('_')
                if filtroListaINT != []:
                    filtroINT = [s for s in filtroListaINT if litadoBusqueda in s]
                if len(filtroINT)==1:
                    break  
        if filtroINT==[]:
            return "Sin datos"         
        return filtroINT[0]         
             
if __name__ == '__main__':
    valores=[]
    with open("datos.txt", "r") as datos:
        for ip in datos:
         valores.append(ip)

    print(FiltroNetmiko.obtenerCSOTT(valores))
       
    
    