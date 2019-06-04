import sock as net
import terminal
def main():
    print("[PROGRAM] Initilazed fuzz_0")
    console = terminal.terminal.prototypes
    entry = console.main_menu()
    if(1 == entry):
        PORT = console.init_server()
        net_0 = net.netsock(0,PORT,"server")
    elif(2 == entry):
        PORT,IP = console.init_socket()
        net_0 = net.netsock(IP,PORT,"socket")
    elif(3 == entry):
        net_0 = net.https.HTTP()
        net_0.init_test()
    elif('x' == entry):
        return 0
#start main
main()
