# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import os
import re
import subprocess


def regex():
    subprocesscheck = subprocess.Popen("ipconfig", shell=True, stdout=subprocess.PIPE)
    subprocess_return = subprocesscheck.stdout.read()

    search = re.search(rb'(?<=IPv4).*\w+', subprocess_return)
    print(search)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    regex()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
