import nmap3

class Puertos:
    @classmethod
    def validarPuertos(cls, ip):
        nmap = nmap3.NmapHostDiscovery()
        results = nmap.nmap_portscan_only(ip)
   
        datos=results[ip]['ports']
    
        lista=["NO","NO"]
        for estado in datos:
            if estado["portid"]=='22' and estado["state"]=='open':
                lista[0]="SI"
                   
            if estado["portid"]=='23' and estado["state"]=='open':
                 lista[1]="SI" 
  
        return lista     
     
if __name__ == '__main__':
    print(Puertos.validarPuertos())
            