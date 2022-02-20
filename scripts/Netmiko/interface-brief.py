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
        filename = ("Output/Interface Brief/" + device + ".txt")
        output = net_connect.send_command("show ip int brief")
        print(output)
        log_file = open(filename, "a")
        log_file.write(output)
        net_connect.disconnect()
