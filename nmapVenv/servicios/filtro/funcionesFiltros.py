
import itertools


class FuncionesFiltro:
   
    @classmethod    
    def filtroCSs(cls,comandoShRun):
        busquedaCS =  ["10000","7880","7879","66678","717020"]
        for litadoBusqueda in busquedaCS:
            filtroCS = [s for s in comandoShRun if litadoBusqueda in s]
           
            if len(filtroCS)>0:
                filtroListaCS=filtroCS[0].split(' ')
                filtroCS = [s for s in filtroListaCS if litadoBusqueda in s]
                if len(filtroCS)<10:
                    filtroListaCS=filtroCS[0].split(':')
                    filtroCS = [s for s in filtroListaCS if litadoBusqueda in s]  
                if len(filtroCS)<10:
                    filtroListaCS=filtroCS[0].split('_')
                    filtroCS = [s for s in filtroListaCS if litadoBusqueda in s] 
                else:
                    datos=filtroCS
                    return datos
                return  filtroCS[0]
              
        
    @classmethod
    def filtroOTTs(cls,comandoShRun):
      
        busquedaOTT = ["71701","712008","7200","7210","7180","7190", "7170", "7160" ,"7150"]
        for litadoBusqueda in busquedaOTT:
            filtroOTT = [s for s in comandoShRun if litadoBusqueda in s]
       
            if len(filtroOTT)>0:
                filtroListaOTT=filtroOTT[0].split(' ')
                filtroOTT = [s for s in filtroListaOTT if litadoBusqueda in s]
                if len(filtroOTT)<10:
                    filtroListaOTT=filtroOTT[0].split(':')
                    filtroOTT = [s for s in filtroListaOTT if litadoBusqueda in s]  
                if len(filtroOTT)<10:
                    filtroListaOTT=filtroOTT[0].split('_')
                    filtroOTT = [s for s in filtroListaOTT if litadoBusqueda in s] 
                else:
                    datos=filtroOTT
                    return datos
                
                return  filtroOTT[0]
   
   
    @classmethod
    def filtroModel(cls, comandoModel):
        datos=comandoModel[0].split(' ')
        if len(datos[1])>6:
            return datos[1]
        else:
            return 'sin datos'
        
    
    @classmethod
    def filtroProtocolo(cls, comandoRoute):
        router=comandoRoute[0].split(' ')
        if router[1]:
            return router[1]
        else:
            return 'sin datos'
        
    
    @classmethod
    def filtroLoop(cls, comandoLoop):
        router=comandoLoop[0].split(' ')
        nueva_lista = [sublista for sublista in router if sublista]
        if nueva_lista[1]:
            return nueva_lista[1]
        else:
            return 'sin datos'

    @classmethod
    def shVlan40(cls,comandoVlan40):
        router=comandoVlan40[0].split(' ')
        nueva_lista = [sublista for sublista in router if sublista]
        if nueva_lista[1]:
            return nueva_lista[1]
        else:
            return 'sin datos'     

    @classmethod
    def shVlan1(cls,vlan1, vlan1A, vlan1B):
     
        lst_all = list(itertools.chain(vlan1, vlan1A, vlan1B))
        nueva_lista = [sublista for sublista in lst_all if sublista]
        lst=nueva_lista[0].split(' ')
        lista = [sublista for sublista in lst if sublista]
        if lista[1]:
            return lista[1]
        else:
            return 'sin datos'
        
        
        