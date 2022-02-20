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

with open("devices.txt") as routers:
    for IP in routers:
        Router = {
            "device_type": "cisco_ios",
            "ip": IP,
            "username": username,
            "password": password
        }
        net_connect = ConnectHandler(**Router)

        ######################################
        #                                    #
        #         INSERT CODE HERE           #
        #                                    #
        ######################################

        net_connect.disconnect()
