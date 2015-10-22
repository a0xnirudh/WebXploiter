import os

__author__ = 'Anirudh Anand (a0xnirudh)'


class Install():
    """
    This will manage the entire installation and necessary packages

    Supported Distros:- Debian, Ubuntu, Linux Mint & others with apt support

    """
    def __init__(self):
        self.os_install_tools = "install/req.txt"
        self.pip_install_tools = "install/pip.txt"

    def run_command(self, command):
        print "[+] Running the command: %s" % command
        os.system(command)

    def install_pip_tools(self):
        install_file = open(self.pip_install_tools, "r")
        for i in install_file.readlines():
            self.run_command("sudo -E pip install --upgrade " + i)

    def install_os_tools(self):
        install_file = open(self.os_install_tools, "r")
        for i in install_file.readlines():
            self.run_command("sudo apt-get install " + i)


def main():
    install = Install()
    install.install_os_tools()
    install.install_pip_tools()


if __name__ == '__main__':
    main()
