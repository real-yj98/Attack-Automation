from time import sleep 
from library.pymetasploit3.msfrpc import MsfRpcClient

def init(client,sid):
    session = client.sessions.session(sid)
    session.write("getuid")
    sleep(5)
    success = ''
    for line in session.read().split("\n"):
        print(line)

if __name__ == '__main__':
    client = MsfRpcClient("123",server='172.22.0.4',port=55552)
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