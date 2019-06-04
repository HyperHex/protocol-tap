import socket
import sys
import https
#TODO:
#   - expand server()

class netsock:
    sock = None
    _PORT = None
    _IP = None

    def __init__(self,IP,PORT,mode):
        self._IP = IP
        self._PORT = PORT
        if(mode == "socket"):
            print("[SOCKET] Starting services")
            self.socket()
        elif(mode == "server"):
            print("[SERVER] Starting services")
            self.server()
        else:
            print("[ERROR] invalid mode")
    #START: socket functions
    def create(self):
        print("[SOCKET] Creating socket")
        try:
            self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            print("[SOCKET] Creation Successful")
            return 0
        except socket.gaierror:
            print("[ERROR] Creation has failed")
            sys.exit()
            return -1
    def connect_IP(self):
        print("[CONNECTION] Trying to connect")
        try:
            self.sock.connect((self._IP,int(self._PORT)))
            print("[CONNECTION] Connection Succesful")
            print ("[SOCKET] Socket has successfully connected to google \ on port == %s" %(self._IP))
            return 0
        except socket.error:
            print("[ERROR] Connection failed")
            return -1
    def receive(self):
        print(self.sock.recv(1024))
    def socket(self):
       if(self.create() == 0):
            code = self.connect_IP()
       if(code == 0):
            self.receive()
       else:
           print("[ERROR] socket does not work")
           return -1
       self.sock.close()
       return 0
    #START: server functions
    def bind(self):
        host = socket.gethostname()
        try:
            self.sock.bind((host, int(self._PORT)))
            print("[SOCKET] socket is binded to %s" %(self._PORT))
            return 0
        except socket.error:
            print("[ERROR] socket binding failed")
            return -1
    def listen(self):
        try:
            self.sock.listen(5)
            print("[CONNECTION] Listening to port")
            return 0
        except socket.gaierror:
            print("[ERROR] Listening to port failed")
            sys.exit()
            return -1
    def server(self):
        if(self.create() != 0):
            print("[ERROR] Server doesnt work")
            return -1
        if(self.bind() != 0):
            print("[ERROR] Server doesnt work")
            return -2
        if(self.listen() != 0):
            print("[ERROR] Server doesnt work")
            return -3
        while True:
            connect, addr = self.sock.accept()
            print("[CONNECTION] Got connection from", addr)
            connect("[MESSAGE] Connected to fuzz_0")
            connect.close()
        return 0
