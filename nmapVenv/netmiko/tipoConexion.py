class TipoConexion:
        
    
    @classmethod
    def conexionTelnet(cls,ip, usuario , password):
       
        
        cisco_router_telnet = {
            'device_type': 'cisco_ios_telnet',
            'host': ip,
            'username': usuario,
            'password': password,
            'port': 23
        }    
        return  cisco_router_telnet  
    
    
    
    @classmethod
    def conexionSSH(cls, ip, usuario , password):
    
        cisco_router_ssh = {
            'device_type': 'cisco_ios',
            'host': ip,
            'username': usuario,
            'password': password,
            'port': 22
        }    
        return  cisco_router_ssh