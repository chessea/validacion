
from ping3 import ping 
from ipaddress import IPv4Address

class Ping:
    @classmethod
    def ipValidaLista(cls, lista):
        ''' 
        with open('/home/fr/Documentos/validacion/nmapVenv/store/ip.txt','r') as stop_words: 
            lista = [linea.strip() for linea in stop_words]
         '''
        ips = []
        result=[]
        for ipAddress in lista:
           
            ipNueva=ipAddress
            datos=ping(ipAddress)
            if datos != None:
                ips.append(ipAddress)
            else:
                ipNueva= IPv4Address(ipAddress)+1
                datos2=ping(str(ipNueva))
                if datos2 != None:
                    ips.append(str(ipNueva))
                else:
                    ipNueva= IPv4Address(ipAddress)+2
                    datos2=ping(str(ipNueva))
                    if datos2 != None:
                        ips.append(str(ipNueva))
                    else:
                        pass   
        '''               
        for element in ips:
            if element not in result:
                result.append(element)
                
        '''
        return ips
    
if __name__ =='__main__':
    print(Ping.ipValidaLista())        
                    