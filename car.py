#shit to do: tray, run from flash (https://stackoverflow.com/questions/31091560/as3-running-an-external-program), settings pages (gotoAndStop();, copy frame) 

import miniamf.adapters._sets
import miniamf.amf3
import miniamf.amf0
import pypresence

from miniamf import sol
from pypresence import Presence

import time
import os 
import threading
import pythoncom
import psutil
import argparse

parser = argparse.ArgumentParser(description='Discord RPC for Red Ball Hacks')

parser.add_argument('-s', '--sol', dest="solPass", default="rpc", help='Name of SOL to Load')
parser.add_argument('-i', '--appid', '--id', dest="idPass", default="881010245147709440", help='Discord App ID')
parser.add_argument('-x', '--max', dest="maxPass", default="9", help='Maximum # of Levels', type=int)
parser.add_argument('-m', '--min', dest="minPass", default="8", help='Minimum # of Levels', type=int)
args = parser.parse_args()

if args.solPass:
    solArg = args.solPass

if args.idPass:
    idArg = args.idPass

def onMin():
    global isMin
    isMin = True

def onMax():
    global isMax
    isMax = True

if args.maxPass:
    maxArg = args.maxPass
    if args.maxPass == 9:
        isMax = False
    else:
        onMax()

if args.minPass:
    minArg = args.minPass - 1
    if args.minPass == 8:
        isMin = False
    else: 
        onMin()

print("Startup Initialized...")

rpc = Presence(idArg)
rpc.connect()
print(f"RPC Connected ({idArg})")

time.sleep(3)

predir = os.path.expandvars(r'%APPDATA%/Macromedia/Flash Player/#SharedObjects/')
postdir = os.listdir(predir)
posterdir = ''.join(postdir)
print(f'SO Folder Key is {posterdir}')
sendto_dir = predir + posterdir + "/localhost/" + solArg + ".sol"

flag = 0

if os.path.exists(sendto_dir) == True:
    solLoad = sol.load(sendto_dir)
    rpcSetSol = solLoad.get("setting")
    print(f"SOL File found and Loaded ({args.solPass})")
    SOLchk = True
else:
    print(f"SOL File not found ({args.solPass})")
    SOLchk = False
    os.system('pause')

if SOLchk == True:
    print("Searching for Flash...")
    for p in psutil.process_iter(attrs=['pid', 'name']):
        if p.info['name'] == "Flash Player.exe":
            flag = 1

def checkFlash():
    pythoncom.CoInitialize()
    import subprocess
    global flag
    global rpcSetFlag
    while flag == 1: 
        progs = str(subprocess.check_output('tasklist'))
        if "Flash Player.exe" in progs:
            flag = 1
        else:
            rpcSetFlag = True
            flag = 0

th = threading.Thread(target=checkFlash, name='flashchk')
if flag == 1:
    th.daemon = True
    th.start()
    print("Thread Started")

def updateRPC():
    solLoad = sol.load(sendto_dir)
    detailSol = solLoad.get("detail")
    rpcSetSol = solLoad.get("setting")

    global maxArg
    global minArg
    global isMax
    global isMin

    if isMax == True or isMin == True:
        if rpcSetSol == "On":
            minLvl = minArg
            while minLvl < maxArg:
                minLvl = minLvl + 1
                if detailSol == "In menu":
                    rpc.update(details="In Menu", large_image="icon")
                elif detailSol == f"Level {minLvl}":
                    rpc.update(state="On Level", party_size=[minLvl,maxArg], small_image=str(minArg), large_image="icon")
        else:
            print('RPC set to "Off" detected')
            global rpcSetFlag
            rpcSetFlag = True
            os.system('pause')
    else:
        if rpcSetSol == "On":
            if detailSol == "In menu":
                rpc.update(details="In Menu", large_image="car_icon")
            elif detailSol == "Level 8":
                rpc.update(state="On Level", party_size=[8,9], small_image="8", large_image="car_icon")
            elif detailSol == "Level 9":
                rpc.update(state="On Level", party_size=[9,9], small_image="9", large_image="car_icon")
        else:
            print('RPC set to "Off" detected')
            rpcSetFlag = True
            os.system('pause')

rpcSetFlag = False

if flag == 1:
    if rpcSetSol == "On":
        print("RPC is Running")
        while rpcSetFlag == False:  
            updateRPC()
            time.sleep(1)
        if flag == 0:
                rpc.close()
                print("Game Exit Detected")
                th.join()
                os.system('pause')
    else:
        if flag == 1:
            print('RPC set to "Off" in game so RPC was not ran')
            os.system('pause')
elif SOLchk == True:
    print("RPC not ran because Flash Player was not found")
    os.system('pause')