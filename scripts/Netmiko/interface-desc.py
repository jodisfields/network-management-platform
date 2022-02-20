from netmiko import ConnectHandler
from os import system


def logo():
    system("cls")
    print("""
	███████╗██╗███████╗███████╗ ██████╗         
	██╔════╝██║██╔════╝██╔════╝██╔═══██╗        
	█████╗  ██║███████╗███████╗██║   ██║        
	██╔══╝  ██║╚════██║╚════██║██║   ██║        
	██║     ██║███████║███████║╚██████╔╝        
	╚═╝     ╚═╝╚══════╝╚══════╝ ╚═════╝         
												
███╗   ██╗███████╗████████╗ ██████╗ ██████╗ ███████╗
████╗  ██║██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗██╔════╝
██╔██╗ ██║█████╗     ██║   ██║   ██║██████╔╝███████╗
██║╚██╗██║██╔══╝     ██║   ██║   ██║██╔═══╝ ╚════██║
██║ ╚████║███████╗   ██║   ╚██████╔╝██║     ███████║
╚═╝  ╚═══╝╚══════╝   ╚═╝    ╚═════╝ ╚═╝     ╚══════╝
    """)


logo()


username = input("Username: ")
password = input("Password: ")

with open("Inventory/Network/Network_FIEP") as routers:
    for IP in routers:
        Router = {
            "device_type": "cisco_ios",
            "ip": IP,
            "username": username,
            "password": password
        }
        net_connect = ConnectHandler(**Router)
        hostname = net_connect.send_command("show run | i host")
        hostname.split(" ")
        device = hostname.split(" ")
        device = device[1]
        print("Gathering Facts")
        filename = ("Output/Interface Description/" + device + ".txt")
        intdesc = net_connect.send_command("show int desc")
        log_file = open(filename, "a")
        log_file.write(intdesc)
        log_file.write("\n")
        net_connect.disconnect()
