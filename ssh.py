
import sys
import paramiko

class ssh:
  cmd = None
  host = None
  pwd = None
  client = None
  user = None
  port = None
  key = None

  __init__(hostname,password,command,port = None, user = None):
    self.cmd = command
    self.host = hostname
    self.pwd = password
    #init fx
    self.initilize()
    self.connect(port,user)
  def initialize():
    print("[SSH] Initializing client"
    if(not paramiko.ssh_exception.BadHostKeyException(self.host, self.key, expected_key)):
      client = paramiko.SSHClient()
      client.load_system_host_keys()
      client.set_missing_host_key_policy(paramiko.WarningPolicy)
      print("[SSH] Initilizing successful")
    else:
      print("[ERROR] initializing client failed")
  def connect(port,user):
     if(not #error):
       print("[CONNECT] setting up connection to host: , self.host")
       self.client.connect(self.host,port = self.port,user = self.user,self.pwd)
       self.port = port
       self.user = user
     else:
        print("[ERROR] Connection failed")
    #pseudo-code
    def check_connection():
        while connected():
            #do something
