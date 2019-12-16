from time import sleep
from library.pymetasploit3.msfrpc import MsfRpcClient
import os,subprocess

numbering=1
stagelist=[]
tactlist=[]
catlist=[]
modulelist=[]


def switch_no():
    global numbering
    for x in os.listdir('.'):
    
        if "stage" in x:
            print("{}.".format(numbering), x)
            stagelist.append(x)
            numbering+=1

    switcher = {
        '1': "stage4",
        '2': "stage3",
        '3': "stage2"
    }
    numbering=1
    switch=input("Choose your Stage:")
    strr=switcher.get(switch, "invalid command")
    return(strr)

def switch_tact(stage):
    global numbering
    for x in os.listdir('{}'.format(stage)):
        if 'py' not in x:
            print("{}.".format(numbering), x)
            tactlist.append(x)
            numbering+=1
    while len(tactlist) <4:
        tactlist.append('none')
    switcher = {
        '1':tactlist[0],
        '2':tactlist[1],
        '3':tactlist[2],
        '4':tactlist[3]
    }
    numbering =1
    switch=input("Choose your Tactics:")
    strr=switcher.get(switch, "invalid command")
    return(strr)

def switch_cat(stage,tact):
    global numbering
    for x in os.listdir('{}/'.format(stage)+'{}'.format(tact)):
        if 'py' not in x:
            print("{}.".format(numbering), x)
            catlist.append(x)
            numbering+=1
    while len(catlist) <7:
        catlist.append('none')
    switcher = {
        '1':catlist[0],
        '2':catlist[1],
        '3':catlist[2],
        '4':catlist[3],
        '5':catlist[4],
        '6':catlist[5],
        '7':catlist[6]
    }
    numbering =1
    switch=input("Choose your Category:")
    strr=switcher.get(switch, "invalid command")
    return(strr)

def switch_module(stage,tact,cat):
    for x in os.listdir('{}/'.format(stage)+'{}/'.format(tact)+'{}'.format(cat)):
        if '__' not in x:
            mod = x.split('.py')
            print(mod[0])
            modulelist.append(mod[0])
    print("NOTE:IF THERE IS A SPACE IN THE MODULE, IT IS UNDERLINE!!")
    strr=input("Type the name of the module you want to use: ")
    return(strr)


def main():
   
    client = MsfRpcClient("123",port=55552)
    print("Select the stage of the module")
    stage = switch_no()
    subprocess.call("clear")
    tact = switch_tact(stage)
    subprocess.call("clear")
    cat = switch_cat(stage,tact)
    module = switch_module(stage,tact,cat)
    subprocess.call("python -m {}.".format(stage)+"{}.".format(tact)+"{}.".format(cat)+"{}".format(module),shell=True)

main()
