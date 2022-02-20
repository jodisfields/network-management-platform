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
        print("Gathering Facts On: " + device)
        filename = ("Output/Map Topology/" + device + ".txt")
        showcdp = net_connect.send_command("show cdp neigh")
        showarp = net_connect.send_command("show ip arp")
        ospfnei = net_connect.send_command("show ip ospf neigh")
        lsdb = net_connect.send_command("show ip ospf database")
        iproute = net_connect.send_command("show ip route")
        intdesc = net_connect.send_command("show int desc")
        showver = net_connect.send_command("show version")
        log_file = open(filename, "a")
        log_file.write(showcdp)
        log_file.write("\n")
        log_file.write(showarp)
        log_file.write("\n")
        log_file.write(ospfnei)
        log_file.write("\n")
        log_file.write(lsdb)
        log_file.write("\n")
        log_file.write(iproute)
        log_file.write("\n")
        log_file.write(intdesc)
        log_file.write("\n")
        log_file.write(showver)
        log_file.write("\n")
        net_connect.disconnect()
