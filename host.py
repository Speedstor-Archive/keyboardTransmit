import pprint
import socket
import threading
from handlers import *
import os

pp = pprint.PrettyPrinter(indent=4)

class HTTPHandler:
    def get(self, args, type):
        if args == '/':
            args = '/index.html'
            fin = open('website' + args)
        if type != "image":
            fin = open('website/' + args)

        if type == "image":
            fin = open('website/' + args, 'rb')

        # Read file contents
        content = fin.read()
        fin.close()
        return content

def handle_request(request):
    http = HTTPHandler

    if not "\r\n\r\n" in request: return None

    try:
        bodySeperatorIndex = request.index("\r\n\r\n")
        # Parse headers
        headers = request[:bodySeperatorIndex].split("\n")

        # Parse body
        body = request[bodySeperatorIndex+4:]
        if(len(headers) > 1):
            get_content = headers[0].split()
            get_param = None

            requestUrl = get_content[1]
            if "?" in requestUrl:
                getIndexSeperator = requestUrl.index("?")
                get_param = requestUrl[getIndexSeperator+1:]
                requestUrl = requestUrl[:getIndexSeperator]
                print(get_param)
                # for getItemStr in getParamsArr:
                #     if "=" not in getItemStr:


            print(f"Request: {get_content[1]}")
            if requestUrl == "/sendInput":
                return execute_input(get_param, headers, body)
            elif requestUrl == "/":
                return "This is the server that accepts inputs to be sent to the current machine. Send data to /sendInput"

            # json.dumps(database.getDatabase()).encode()
            #for web static content server
            """
            else:
                try:
                    # Filename
                    filename = requestUrl

                    if get_content[0] == "GET":
                        # content = http.get(None, requestUrl, type_content[0])
                        content = http.get(None, requestUrl, 'image')
                        return content
                except FileNotFoundError:
                    return None
            """
    except:
        return None

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

def socketThread(client_connection, client_address):
    request_data = client_connection.recv(1024).decode('utf-8')
    content = handle_request(request_data)

    # Send HTTP response
    if content:
        response = b'HTTP/1.1 200 OK\nAccess-Control-Allow-Origin: *\n\n'
        response += content.encode('ascii')
    else:
        response = b'HTTP/1.1 404 NOT FOUND\n\nFile Not Found'

    client_connection.sendall(response)
    client_connection.close()

HOST, PORT = '', 99
def start(port):
    PORT = port
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_socket.bind((HOST, PORT))
    listen_socket.listen(1)
    print(f'Serving HTTP on port {PORT} ...')

    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    print(f"""------------------------------------------------------------------
    
  Device is ready to recieve input from other devices:
  The hostAddress of this device is:
  \t {local_ip}:{PORT}

------------------------------------------------------------------""")
    while True:
        try:
            client_connection, client_address = listen_socket.accept()

            requestThread = threading.Thread(target=socketThread, args=(client_connection, client_address))
            requestThread.start()
        except Error:
            print("error recieving socket and request")