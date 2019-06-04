import http.client
import urllib.parse

#TODO:
# - errors states

class HTTP:
    connection = None
    IP = None
    DNS = None
    PORT = None
#READ/RECEIVE
    bytes = 200
    recv1 = None
    recv2 = None
#WRITE/POST
    params = None
    headers = None
    url = None
#connection
    def connect(self,DNS,IP,PORT = 80):
        print("[CONNECTION] Setting up connection")
        self.connection = http.client.HTTPSConnection(IP,PORT)
        self.connection.set_tunnel(DNS)
        self.connection.request("HEAD","/index.html")
        print("[CONNECTION] Connection setup finished")
        print("[SETUP] Assigning variables...")
        self.IP = IP
        self.DNS = DNS
        self.PORT = PORT

#read/write
    def request_GET(self):
        print("[REQUEST] sending GET request")
        connection.request("GET","/")
        self.recv1 = connection.getresponse()
        print("[DATA] Receiving Data blocks")
        while not self.recv1.closed:
            print(recv1.read(self.bytes)) # 200 bytes\
    def request_HEAD(self):
        print("[REQUEST] sending HEAD request")
        connection.request("HEAD","/")
        self.recv1 = connection.getresponse()
        print("[CODE] ",self.recv1.status, self.recv1.reason)

    def chunk_data(data, chunk_size):
        dl = len(data)
        ret = ""
        for i in range(dl // chunk_size):
            ret += "%s\r\n" % (hex(chunk_size)[2:])
            ret += "%s\r\n\r\n" % (data[i * chunk_size : (i + 1) * chunk_size])

        if len(data) % chunk_size != 0:
            ret += "%s\r\n" % (hex(len(data) % chunk_size)[2:])
            ret += "%s\r\n" % (data[-(len(data) % chunk_size):])
        ret += "0\r\n\r\n"
        return ret
    def send_POST():
        connection.putrequest('POST', url)
        connection.putheader('Transfer-Encoding', 'chunked')
        connection.endheaders()
        connection.send(chunk_data(body, size_per_chunk).encode('utf-8'))
#status

#init
    def init_test(self):
        params = urllib.parse.urlencode({'@number': 12524, '@type': 'issue', '@action': 'show'})
        headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}

        self.connect("www.python.org","localhost",8080)
        self.request()
        self.connection.close()
#errors
