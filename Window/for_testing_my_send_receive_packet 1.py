#This is main file of script.
#It uses scapy to create packet and send via ethernet.

from md_fw_declare import *
from md_fw_menu import *
#VALID UDP PORT
PKT_Default_Receive=Ether()/dot1q/IPv6(src=VALID_SRC_IPv6, dst=VALID_DST_IPv6)/UDP(sport=VALID_SPORT,dport=VALID_DPORT)/payload_default
#INVALID UDP PORT
PKT_Default_Send=Ether()/dot1q/IPv6(src=VALID_SRC_IPv6, dst=VALID_DST_IPv6)/UDP(sport=VALID_SPORT,dport=12345)/payload_default

def print_infor():
    try:
        global PKT_Default_Receive
        print("\n----------Packet-information-------------")
        PKT_Default_Receive.show()
    except Exception as ex:
        print(ex)
#16.1.15.2 Undefined UDP port message handling

def send_packet():
    global PKT_Default_Receive
    try:
        PKT_Default_Receive.show()
        sendp(PKT_Default_Receive, iface=IFACE)
    except Exception as ex:
        print(ex)
        
def main():
    cloop=True
    while cloop:
        try:
            choice = print_menu()
            if int(choice) == 1:
                print_infor()
            elif int(choice) == 2:              
                send_packet()
            elif int(choice) == 0:
                cloop=False
        except KeyboardInterrupt:
            print ('\nThanks! See you later!\n\n')
            cloop=False
if __name__ == '__main__':
    main()
    
# py for_testing_my_send_receive_packet.py