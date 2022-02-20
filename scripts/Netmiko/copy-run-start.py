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
        print("-"*79)
        print("Saving Config ")
        print("-"*79)
        output = net_connect.save_config()
        print(output)
        print("-"*79)
        print("Config Saved ")
        print("-"*79)
        net_connect.disconnect()
