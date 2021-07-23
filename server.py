import socket
import requests
# import json

HOST = "192.168.31.229"
PORT = 12404

#create socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#set connection with host and port
# s.bind((HOST, PORT))
#listening client
#backlog param: number of unaccepted connection
# that the system wil allow before refusing newconnection  
# s.listen(1)
# print("Connect is already... Waiting for listen...")
#blocks and wait for an incoming connection. a client connects, 
#it returns a new socket object representing the connection
#and a tuple holding the address of the client.
#assign this tuple to add variable.
# conn, add = s.accept()

try:
    response = requests.get("https://portal.vietcombank.com.vn/Usercontrols/TVPortal.TyGia/pXML.aspx")
    print(response.content)
    s.close()
except KeyboardInterrupt:
    # conn.close()
    s.close()
finally:
    # conn.close()
    s.close()