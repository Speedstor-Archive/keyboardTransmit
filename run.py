import pprint
import threading
from handlers import *
import host
import client_connect
import os
import sys

pp = pprint.PrettyPrinter(indent=4)

def commandLine():
    global finnhub_websocket
    while True:
        inputString = input()
        cutIndex = -1
        command = ""
        if " " in inputString:
            cutIndex = inputString.index(" ")
            command = inputString[:cutIndex]
        else:
            command = inputString

        if "useless" == command:
            print('this is a useless placeholder commadn')
        elif "exit" == command or "stop" == command:
            os._exit(0)

def printHelp():
    print("Usage (2 ways): python3 ./run.py host <port>\n                python3 ./run.py client <hostAddress>")
    os._exit(0)

if __name__ == '__main__':
    #thread for handling input
    commandLineThread = threading.Thread(target=commandLine, args=())
    commandLineThread.start()

    print(sys.argv)
    print(str(sys.argv))
    print(sys.argv[0])

    if_host = None
    if len(sys.argv) < 2:
        printHelp()

    if sys.argv[1] == "host":
        if_host = True
    elif sys.argv[1] == "client":
        if_host = False
    else:
        printHelp()

    if if_host:
        port = None
        if len(sys.argv) >= 3:
            try:
                port = sys.argv[2]
                port = int(portOrAddress)
            except (ValueError, IndexError):
                print("Given port isn't a valid number, using default port 99.")
                port = 99
        else:
            port = 99

        host.start(port)
    else:
        if len(sys.argv) < 3:
            printHelp()
        client_connect.start(sys.argv[2])