import os
import sys

sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__),
                '..')))

__author__ = 'Anirudh Anand (a0xnirudh)'

from Modules.loggingManager.logging_manager import LoggingManager


class Install():
    """
    This will manage the entire installation and necessary packages

    Supported Distros:- Debian, Ubuntu, Linux Mint & others with apt support

    """
    def __init__(self):
        self.file_location = os.path.abspath(os.path.dirname(__file__))
        self.os_install_tools = self.file_location + "/req.txt"
        self.pip_install_tools = self.file_location + "/pip.txt"

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
    logger=LoggingManager()
    install = Install()
    try:
        install.install_os_tools()
    except Exception as e:
        logger.install_log(e)
        print("Error while installing os tools. Check install log.")
        exit()
    try:
        install.install_pip_tools()
    except Exception as e:
        logger.install_log(e)
        print("Error while installing python pip tools. Check install log.")
        exit()

if __name__ == '__main__':
    main()
