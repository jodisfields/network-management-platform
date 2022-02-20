 from csv import reader
from datetime import date, datetime
from logging import log
from netmiko import ConnectHandler
from ping3 import ping, verbose_ping
from subprocess import check_output, CalledProcessError
from os import system
from pick import pick
import getpass
import os
from concurrent.futures import ThreadPoolExecutor
import logging
import sys
import time


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


if not os.path.isdir("Output/Running Config"):
    os.makedirs("Output/Running Config")

if not os.path.isdir("Output/CDP Neighbour"):
    os.makedirs("Output/CDP Neighbour")

if not os.path.isdir("Output/Network Discovery"):
    os.makedirs("Output/Network Discovery")

if not os.path.isdir("Output/Interface Brief"):
    os.makedirs("Output/Interface Brief")

if not os.path.isdir("Output/Interface Description/"):
    os.makedirs("Output/Interface Description/")

if not os.path.isdir("Output/Traceroute Results"):
    os.makedirs("Output/Traceroute Results")


now = datetime.now()
dt_string = now.strftime("%m-%d-%Y_%H-%M")


def backup(host, username, password, enable_secret):
    cisco_ios = {
        "device_type": "cisco_ios",
        "host": host,
        "username": username,
        "password": password,
        "secret": enable_secret
    }
    net_connect = ConnectHandler(**cisco_ios)
    net_connect.enable()
    output = net_connect.send_command("show running-config")
    hostname = net_connect.send_command("show version | include uptime")
    hostname = hostname.split()
    hostname = hostname[0]
    fileName = hostname + "_" + dt_string
    backupFile = open("Output/Running Config/" + fileName + ".txt", "w+")
    backupFile.write(output)
    print("Configuration Saved To: " + fileName + ".txt!")


def manual_input():
    host = input("\nIP: ")
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    enable_secret = getpass.getpass("Enable Secret: ")
    ip = host
    ip_ping = ping(ip)
    if ip_ping == None:
        fileName = "DOWN_" + dt_string + ".txt"
        downDeviceOutput = open("Output/Running Config/" + fileName, "a")
        downDeviceOutput.write(str(ip) + "\n")
    else:
        backup(ip, username, password, enable_secret)


def cdp_neighbour(host, username, password, enable_secret):
    cisco_ios = {
        "device_type": "cisco_ios",
        "host": host,
        "username": username,
        "password": password,
        "secret": enable_secret
    }
    hostname = net_connect.send_command("show version | include uptime")
    hostname = hostname.split()
    hostname = hostname[0]
    fileName = hostname + "_" + dt_string
    backupFile = open("Output/CDP Neighbour/" + fileName + ".txt", "w+")
    backupFile.write(output)
    print("Output Saved To: " + fileName + ".txt!")
    print(output)


def discovery(host, username, password, enable_secret):
    cisco_ios = {
        "device_type": "cisco_ios",
        "host": host,
        "username": username,
        "password": password,
        "secret": enable_secret
    }
    net_connect = ConnectHandler(**cisco_ios)
    net_connect.enable()
    hostname = net_connect.send_command("show version | include uptime")
    hostname = hostname.split()
    hostname = hostname[0]
    filename = hostname + "_" + dt_string
    showver = net_connect.send_command("show version")
    showcdp = net_connect.send_command("show cdp neigh")
    ospfnei = net_connect.send_command("show ip ospf neigh")
    showarp = net_connect.send_command("show ip arp")
    iproute = net_connect.send_command("show ip route")
    lsdb = net_connect.send_command("show ip ospf database")
    intdesc = net_connect.send_command("show int desc")
    intbrief = net_connect.send_command("show int brief")
    showvlan = net_connect.send_command("show vlan")
    log_file = open("Output/Discovery/" + filename, "a")
    log_file.write(showver)
    log_file.write("\n")
    log_file.write(showcdp)
    log_file.write("\n")
    log_file.write(ospfnei)
    log_file.write("\n")
    log_file.write(showarp)
    log_file.write("\n")
    log_file.write(iproute)
    log_file.write("\n")
    log_file.write(lsdb)
    log_file.write("\n")
    log_file.write(intdesc)
    log_file.write("\n")
    log_file.write(intbrief)
    log_file.write("\n")
    log_file.write(showvlan)
    log_file.write("\n")
    net_connect.disconnect()


def write_config(host, username, password, enable_secret):
    cisco_ios = {
        "device_type": "cisco_ios",
        "host": host,
        "username": username,
        "password": password,
        "secret": enable_secret
    }
    net_connect = ConnectHandler(**cisco_ios)
    net_connect.enable()
    hostname = net_connect.send_command("show version | include uptime")
    hostname = hostname.split()
    hostname = hostname[0]
    print("-"*79)
    print("Writting: " + hostname)
    print("-"*79)
    output = net_connect.save_config()
    print(output)
    print("-"*79)
    print("Config Saved ")
    print("-"*79)
    net_connect.disconnect()


def int_brief(host, username, password, enable_secret):
    cisco_ios = {
        "device_type": "cisco_ios",
        "host": host,
        "username": username,
        "password": password,
        "secret": enable_secret
    }
    net_connect = ConnectHandler(**cisco_ios)
    net_connect.enable()
    hostname = net_connect.send_command("show version | include uptime")
    hostname = hostname.split()
    hostname = hostname[0]
    output = net_connect.send_command("show ip int brief")
    fileName = hostname + "_" + dt_string
    backupFile = open("Output/Interface Brief/" + fileName + ".txt", "w+")
    backupFile.write(output)
    print("Output Saved To: " + fileName + ".txt!")
    print(output)
    net_connect.disconnect()


def int_desc(host, username, password, enable_secret):
    cisco_ios = {
        "device_type": "cisco_ios",
        "host": host,
        "username": username,
        "password": password,
        "secret": enable_secret
    }
    net_connect = ConnectHandler(**cisco_ios)
    net_connect.enable()
    hostname = net_connect.send_command("show version | include uptime")
    hostname = hostname.split()
    hostname = hostname[0]
    output = net_connect.send_command("show int desc")
    fileName = hostname + "_" + dt_string
    backupFile = open("Output/Interface Description/" +
                      fileName + ".txt", "w+")
    backupFile.write(output)
    print("Output Saved To: " + fileName + ".txt!")
    print(output)
    net_connect.disconnect()


def ping_cmd(host):
    PING_COMMAND = "ping -n 2"
    ip = host
    cmd = f"{PING_COMMAND} {ip}"
    split_cmd = cmd.split()
    print(f"running: {cmd}")
    try:
        check_output(split_cmd)
    except CalledProcessError:
        print(f"{ip} is UNREACHABLE!")
        return
    print(f"{ip} is reachable")


def ping_devices():
    FILENAME = "Inventory/Network/Network_FIEP"
    with open(FILENAME, "r") as f:
        ips = f.read().splitlines()
    for ip in ips:
        ping(ip)


formatter = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(stream=sys.stdout, format=formatter, level=logging.DEBUG)


def tracert_title(section_name):
    section_tracert_title = "\n" + "*" * 70 + \
        f"\n{section_name}\n" + "*" * 70 + "\n"
    return section_tracert_title


def health_checks(ip):
    CURRENT_DIR = "Output/Tracerout Results/"
    PING_COMMAND = "ping -n 1"
    TRACEROUTE_COMMAND = "tracert"
    ping_cmd = f"{PING_COMMAND} {ip}"
    trace_cmd = f"{TRACEROUTE_COMMAND} {ip}"
    ping_status = run_command(ping_cmd)
    trace_status = run_command(trace_cmd)
    filename = f"{CURRENT_DIR}{os.sep}{ip}.txt"
    with open(filename, "w") as f:
        f.write(tracert_title("Ping Results:"))
        f.write(ping_status)
        f.write(tracert_title("Trace Results:"))
        f.write(trace_status)
    logging.info(f"Wrote outputs to: {filename}")
    logging.debug(ping_status)
    logging.debug(trace_status)


def run_command(command):
    logging.info(f"running: {command}")
    split_cmd = command.split()
    try:
        output = check_output(split_cmd).decode("utf-8")
    except CalledProcessError:
        return "FAILED"
    return output


def tracert():
    START_TIME = time.time()
    MAX_THREADS = 5
    FILENAME = "Inventory/Network/Network_FIEP"
    with open(FILENAME, "r") as f:
        ips = f.read().splitlines()
        num_ips = len(ips)
    with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        [executor.submit(health_checks, ip) for ip in ips]
    end_time = time.time() - START_TIME
    logging.info(f"Checked {num_ips} hosts in {round(end_time)} seconds.")


def select_enclave():
    title = "Select Environment: "
    options = ["FIEP", "FIES", "CMFP", "CNFC"]
    option, index = pick(options, title, indicator="=>", default_index=0)
    if option == "FIEP":
        csv_name = "Inventory/Network/Network_FIEP.csv"
        with open(csv_name, "r") as read_obj:
            csv_reader = reader(read_obj)
            list_of_rows = list(csv_reader)

            rows = len(list_of_rows)

            while rows >= 2:
                rows = rows - 1

                ip = list_of_rows[rows][0]
                ip_ping = ping(ip)
                if ip_ping == None:
                    fileName = "DOWN_" + dt_string + ".txt"
                    downDeviceOutput = open(
                        "Output/Running Config/" + fileName, "a")
                    downDeviceOutput.write(str(ip) + "\n")

                else:
                    backup(
                        list_of_rows[rows][0],
                        list_of_rows[rows][1],
                        list_of_rows[rows][2],
                        list_of_rows[rows][3],
                    )
    elif option == "FIES":
        csv_name = "Inventory/Network/Network_FIES.csv"
        with open(csv_name, "r") as read_obj:
            csv_reader = reader(read_obj)
            list_of_rows = list(csv_reader)

            rows = len(list_of_rows)

            while rows >= 2:
                rows = rows - 1

                ip = list_of_rows[rows][0]
                ip_ping = ping(ip)
                if ip_ping == None:
                    fileName = "DOWN_" + dt_string + ".txt"
                    downDeviceOutput = open(
                        "Output/Running Config/" + fileName, "a")
                    downDeviceOutput.write(str(ip) + "\n")

                else:
                    backup(
                        list_of_rows[rows][0],
                        list_of_rows[rows][1],
                        list_of_rows[rows][2],
                        list_of_rows[rows][3],
                    )
    elif option == "CMFP":
        csv_name = "Inventory/Network/Network_CMFP.csv"
        with open(csv_name, "r") as read_obj:
            csv_reader = reader(read_obj)
            list_of_rows = list(csv_reader)

            rows = len(list_of_rows)

            while rows >= 2:
                rows = rows - 1

                ip = list_of_rows[rows][0]
                ip_ping = ping(ip)
                if ip_ping == None:
                    fileName = "DOWN_" + dt_string + ".txt"
                    downDeviceOutput = open(
                        "Output/Running Config/" + fileName, "a")
                    downDeviceOutput.write(str(ip) + "\n")

                else:
                    backup(
                        list_of_rows[rows][0],
                        list_of_rows[rows][1],
                        list_of_rows[rows][2],
                        list_of_rows[rows][3],
                    )
    elif option == "CNFC":
        csv_name = "Inventory/Network/Network_CNFC.csv"
        with open(csv_name, "r") as read_obj:
            csv_reader = reader(read_obj)
            list_of_rows = list(csv_reader)

            rows = len(list_of_rows)

            while rows >= 2:
                rows = rows - 1

                ip = list_of_rows[rows][0]
                ip_ping = ping(ip)
                if ip_ping == None:
                    fileName = "DOWN_" + dt_string + ".txt"
                    downDeviceOutput = open(
                        "Output/Running Config/" + fileName, "a")
                    downDeviceOutput.write(str(ip) + "\n")

                else:
                    backup(
                        list_of_rows[rows][0],
                        list_of_rows[rows][1],
                        list_of_rows[rows][2],
                        list_of_rows[rows][3],
                    )


title = "Select Inventory Source: "
options = ["Input Information Your Self.",
           "Read Information Directly From CSV"
           ]
option, index = pick(options, title, indicator="=>", default_index=0)
if option == "Input Information Your Self.":
    how_many = input("How many hosts?: ")
    how_many = int(how_many)
    i = how_many
    while i >= 1:
        manual_input()
        i = i - 1
elif option == "Read Information Directly From CSV":
    select_enclave()
