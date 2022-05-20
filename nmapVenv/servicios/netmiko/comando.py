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
            
            shModel = ssh.send_command(comando[1], delay_factor=2)
            comandoListShModel=shModel.split('\n')
            
            shRouter = ssh.send_command(comando[2], delay_factor=2)
            comandoListShRouter=shRouter.split('\n')
            
            shLoop = ssh.send_command(comando[3], delay_factor=2)
            comandoListShLoop=shLoop.split('\n')
            
            shVlan40 = ssh.send_command(comando[4], delay_factor=2)
            comandoListShVlan40=shVlan40.split('\n')
            
            shVlan1 = ssh.send_command(comando[5], delay_factor=2)
            comandoListShVlan1=shVlan1.split('\n')
            
            shVlan1A = ssh.send_command(comando[6], delay_factor=2)
            comandoListShVlan1A=shVlan1A.split('\n')
            
            shVlan1B = ssh.send_command(comando[7], delay_factor=2)
            comandoListShVlan1B=shVlan1B.split('\n')

            
            ssh.exit_enable_mode()
            print("CONEXION TELNET OK",ip)
            lista.append(comandoListShRun)
            lista.append(comandoListShModel)
            lista.append(comandoListShRouter)
            lista.append(comandoListShLoop)
            lista.append(comandoListShVlan40)
            lista.append(comandoListShVlan1)
            lista.append(comandoListShVlan1A)
            lista.append(comandoListShVlan1B)
            
            return lista
        except Exception as e:  
            print("ERROR TELNET")   
            try:
                cisco_router_ssh=TipoConexion.conexionSSH(ip , usuario ,password)
                ssh = netmiko.ConnectHandler(**cisco_router_ssh)
                ssh.enable()
                
                shRun = ssh.send_command(comando[0], delay_factor=2)
                comandoListShRun=shRun.split('\n')
   
                shModel = ssh.send_command(comando[1], delay_factor=2)
                comandoListShModel=shModel.split('\n')
                
                shRouter = ssh.send_command(comando[2], delay_factor=2)
                comandoListShRouter=shRouter.split('\n')
                
                shLoop = ssh.send_command(comando[3], delay_factor=2)
                comandoListShLoop=shLoop.split('\n')
                
                shVlan40 = ssh.send_command(comando[4], delay_factor=2)
                comandoListShVlan40=shVlan40.split('\n')
                
                shVlan1 = ssh.send_command(comando[5], delay_factor=2)
                comandoListShVlan1=shVlan1.split('\n')

                shVlan1A = ssh.send_command(comando[6], delay_factor=2)
                comandoListShVlan1A=shVlan1A.split('\n')

                shVlan1B = ssh.send_command(comando[7], delay_factor=2)
                comandoListShVlan1B=shVlan1B.split('\n')                

                ssh.disconnect()
                print("CONEXION SSH OK", ip)
                
                lista.append(comandoListShRun)
                lista.append(comandoListShModel)
                lista.append(comandoListShRouter)
                lista.append(comandoListShLoop)
                lista.append(comandoListShVlan40)
                lista.append(comandoListShVlan1)
                lista.append(comandoListShVlan1A)
                lista.append(comandoListShVlan1B)
       
                
                return lista
            except Exception as e:
                    print("ERROR SSH")
