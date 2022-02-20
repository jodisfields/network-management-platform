# Import modules.
import os
from datetime import date
from getpass import getpass
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException


def main():
    # Prompts user for their SSH username and password.
    username = input('Enter your SSH username: ')
    password = getpass()
    # Opens the devices.txt file and reads each line into a python list.
    with open('devices.txt') as f:
        devices_list = f.read().splitlines()
    # Loops through each device in the devices.txt file.
    for devices in devices_list:
        print('Connecting to device" ' + devices)
        ip_address_of_device = devices
        ios_device = {
            'device_type': 'cisco_ios',
            'ip': ip_address_of_device,
            'username': username,   # Inserts the users username.
            'password': password    # Inserts the users password.
        }
        # Connects to the device using the variables above.
        try:
            net_connect = ConnectHandler(**ios_device)
        # Handles any errors that may occur, while trying to connect to the devices.
        except (AuthenticationException):
            print('Authentication failure: ' + ip_address_of_device)
            continue
        except (NetMikoTimeoutException):
            print('Timeout to device: ' + ip_address_of_device)
            continue
        except (EOFError):
            print('End of file while attempting device ' + ip_address_of_device)
            continue
        except (SSHException):
            print('SSH Issue. Are you sure SSH is enabled? ' + ip_address_of_device)
            continue
        except Exception as unknown_error:
            print('Some other error: ' + str(unknown_error))
            continue
        # Defines a variable for sending the "show run" command to the device.
        cliConfig = net_connect.send_command('show run')
        # Defines variables for extracting the hostname from the device.
        cliHostname = net_connect.send_command('show run | i hostname')
        splitHostname = cliHostname.split()
        hostname = splitHostname[1] 
        # Adds the datetime string to the backup file name.
        today = str(date.today())
        if not os.path.exists(today):
            os.makedirs(today)
        backupFile = hostname + "-" + today + ".txt"
        # Writes the config to the backup file.
        backupFile.write(cliConfig)
        backupFile.close()
        print("Backup of " + hostname + " complete!")


if __name__ == '__main__':
    main()
