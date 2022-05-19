import netmiko

from servicios.netmiko.tipoConexion import TipoConexion





class Comando:
    @classmethod
    def enviarComando(cls,comando, ip,usuario , password ):
        lista= []
        try:
            cisco_router_telnet=TipoConexion.conexionTelnet(ip, usuario ,password)
            ssh = netmiko.ConnectHandler(**cisco_router_telnet)
            ssh.enable()
            
            shRun = ssh.send_command(comando[0], delay_factor=2)
            comandoListShRun=shRun.split('\n')

            
            ssh.exit_enable_mode()
            print("CONEXION TELNET OK",ip)
            lista.append(comandoListShRun)
            
            return lista
        except Exception as e:  
            print("ERROR TELNET")   
            try:
                cisco_router_ssh=TipoConexion.conexionSSH(ip , usuario ,password)
                ssh = netmiko.ConnectHandler(**cisco_router_ssh)
                ssh.enable()
                
                shRun = ssh.send_command(comando[0], delay_factor=2)
                comandoListShRun=shRun.split('\n')
   
                
                ssh.disconnect()
                print("CONEXION SSH OK", ip)
                
                lista.append(comandoListShRun)
       
                
                return lista
            except Exception as e:
                    print("ERROR SSH")
