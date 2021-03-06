from os import system
from sys import platform


def logo():
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


def main():
    if platform == "linux" or platform == "linux2":
        system("clear")
    elif platform == "darwin":
        system("clear")
    elif platform == "win32":
        system("cls")
    logo()


if __name__ == "__main__":
    main()
