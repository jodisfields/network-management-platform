from concurrent.futures import ThreadPoolExecutor
from csv import reader
from datetime import datetime, date
from getpass import getpass
from re import S
from netmiko.ssh_autodetect import SSHDetect
from netmiko.ssh_dispatcher import ConnectHandler
from os import system
from pick import pick
from ping3 import ping
from subprocess import check_output
from subprocess import check_output, CalledProcessError, run
import logo
import openpyxl
import sys
import time


def cdp_neighbour():
    username = input("Enter Username: ")
    password = getpass("Enter Password: ")
    secret = getpass("Enter Enable Secret: ")
    with open("devices.txt", "r") as device:
        for ip in device:
            device = {
                "device_type": "autodetect",
                "username": username,
                "password": password,
                "secret": secret,
                "ip_address": ip,
            }
    net_connect = ConnectHandler(device)
    output = net_connect.send_command("sh run | i host")
    output = output.split()
    hostname = output[1]
    print("Connecting To " + hostname)


if __name__ == "__main__":
    cdp_neighbour()
