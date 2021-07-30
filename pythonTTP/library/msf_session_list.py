""" 
Wait for an Metasploit session (Meterpreter or Shell) with a given IP address
"""
from time import sleep
from library.pymetasploit3.msfrpc import MsfRpcClient

def init(client, ip ='', lhost = '', time_out_sec = 300):
    print("[*] Waiting for compromised machine to establish session...")
    print("---------------------------------")
    while time_out_sec > 0:
        for id,c in client.sessions.list.items():
            if (c.get('session_host') == ip) or (c.get('tunnel_local') == lhost):
                #print(c)
                print("{})".format(id),"IP: {}".format(c.get('session_host')),"| {}".format(c.get('desc')),"{}".format(c.get('arch')))
                shell = client.sessions.session(id)
                if c.get('desc') != "meterpreter":
                    while True: # this waits until shell is usable
                        shell.write('getpid\n')
                        sleep(5)
                        if 'Current' in shell.read():
                            return id           
        time_out_sec-=1
        sleep(1)
    print("[-] Error, no session is established on targeted IP address")
    return None
    