class terminal:
    #START finish
    msg_connect = {"creating" : "Creating Socket",
                   "created" : "Socket Creation Succesful"}

    def head(status,msg):
        print("["+status+"]" + msg)
    def temp_options(status,options,select): #(list,string)
        for ops in options:
            if(ops == select):
                head(status,options[ops])
    #END finish

    class prototypes:
        def main_menu():
            menu = """[PROGRAM] 1 - Create server
[PROGRAM] 2 - Create socket
[PROGRAM] 3 - http test
[PROGRAM] x - exit"""
            print(menu)
            entry = input("[PROGRAM] Select : ")
            return int(entry)
        def init_server():
            menu = "[INIT] Creating Server"
            PORT = input("[PROGRAM] Select Port : ")
            return PORT
        def init_socket():
            menu = "[INIT] Creating socket"
            PORT = input("[PROGRAM] Select Port : ")
            IP = input("[PROGRAM] Select IP : ")
            return PORT,IP
