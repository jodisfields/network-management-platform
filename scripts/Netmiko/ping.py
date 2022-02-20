from os import system
from subprocess import CalledProcessError, check_output


def logo():
    system("cls")
    print(
        """
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
    """
    )


logo()


def ping(host):
    PING_COMMAND = "ping -n 3"
    ip = host
    cmd = f"{PING_COMMAND} {ip}"
    split_cmd = cmd.split()
    print(f"running: {cmd}")
    try:
        check_output(split_cmd)
        print(f"{ip} is reachable")
        UP_FILE = "Reachable.txt"
        UP_FILE = open(UP_FILE, "a")
        UP_FILE.write(ip + "\n")
        UP_FILE.close()
    except CalledProcessError:
        print(f"{ip} is UNREACHABLE!")
        DOWN_FILE = "Unreachable.txt"
        DOWN_FILE = open(DOWN_FILE, "a")
        DOWN_FILE.write(ip + "\n")
        DOWN_FILE.close()


def main():
    FILENAME = "inventory/devices.txt"
    with open(FILENAME, "r") as f:
        ips = f.read().splitlines()
    for ip in ips:
        ping(ip)


if __name__ == "__main__":
    main()
