from library.pymetasploit3.msfrpc import MsfRpcClient

def init(client,host):
    cid = client.consoles.console().cid
    scanner = client.modules.use('auxiliary','scanner/smb/smb_ms17_010')
    #Setting target IP
    scanner['RHOSTS'] = host
    #retrieve readable outputs
    output = (client.consoles.console(cid).run_module_with_output(scanner).split('['))
    x=1
    while x < len(output):
        if "Host" in output[x]:
            print("[{}".format(output[x]),end= '')
            if "+]" in output[x]:
                return(True)
            elif "-]" in output[x]:
                print("The host {} cannot be attacked".format(rhost))
                return()
        x+=1
    print("The connection to {} cannot be establish".format(rhost))
    return()

if __name__ == '__main__':
    client = MsfRpcClient('123',port=55552)
    host= input("Enter the host address: ")
    init(client,host)