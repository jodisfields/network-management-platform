from netmiko.ssh_autodetect import SSHDetect
from netmiko.ssh_dispatcher import ConnectHandler

remote_device = {
    "device_type": "autodetect",
    "host": "192.168.161.218",
    "username": "admin",
    "password": "admin",
    "port": "10017"
}

guesser = SSHDetect(**remote_device)
best_match = guesser.autodetect()
print(best_match)  # Name of the best device_type to use further
print(guesser.potential_matches)  # Dictionary of the whole matching result
