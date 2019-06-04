import socket
import ssl
import base64

class smtp:
    def __init__():

    username = None
    password = None
    buff_usernames[1000]
    buff_passwords[1000]
    email_server = None
    DNS = None
    IP = None
    PORT = None
    netsock = None
    def connect(self,PORT,DNS):
        print("[SMTP] Starting services")
        self.netsock = socket(AF_INET, SOCK_STREAM)
        print("[SMTP] init SSL")
        self.netsock = ssl.wrap_socket(netsock)
        print("[SMTP] Connecting to ",DNS)
        self.netsock.connect((DNS, PORT))
        recv = self.netsock.recv(1024)
        print("[DATA] :",recv)
    def auth(self):
        username_b64 = base64.b64encode(bytes(username, 'utf-8'))
        username_b64_str = username_b64.decode('utf-8')
        usernameCommand = 'AUTH LOGIN {0}\r\n'.format(username_b64_str)
        client_socket.send(usernameCommand.encode())
        recv1 = client_socket.recv(1024)
        print (recv1)

        password_b64 = base64.b64encode(bytes(password, 'utf-8'))
        password_b64_str = password_b64.decode('utf-8')
        passCommand = password_b64_str + '\r\n'
        client_socket.send(passCommand.encode())
        recv1 = client_socket.recv(1024)
        print (recv1)
