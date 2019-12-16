""" 
Get timestamp of target from Metasploit session (Shell & Meterpreter)
Note that timestamp string is a different for the 2 types of session
"""
from time import sleep
from library.pymetasploit3.msfrpc import MsfRpcClient

def run(client, session_id):
    """
    Given an IP, waits for session, else Raise ValueError if timeout
    \n:param client: MsfRpcClient object
    \n:param ip_address: target's IP address
    \n:return type: string (timestamp) else None
    """
    shell = client.sessions.session(session_id)
    if('Shell' in str(type(shell))):
        shell.write('echo %date% %time%\n') # the newline is important! 
    else:
        shell.write('localtime\n')
    sleep(2)
    r = shell.read()
    if('echo' in r):
        r = r.split("\n")[1]
    return r 


# for unit testing of each technique
if __name__ == '__main__':
    client = MsfRpcClient('123')
    print(run(client, 3))
