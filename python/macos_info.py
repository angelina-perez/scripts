#!/usr/local/bin/python3
'''
Collect machine, OS data.
    computer name (nodename/name of machine on network)
    ip address
    uptime
    username
    ssid (name of wifi network)
    os

Export the data in JSON format.
    {
     machine name
     ip address
     uptime
     username
     ssid
     os
    }
'''

import os
import socket
import subprocess
import platform
import sys

#@TODO: Step 0: TEST
#@TODO: Step 1: create functions (and function names) to clearly describe what work is being done
#@TODO: Step 2: Run those functions, collect the info into ___ format
#@TODO: Step 3: JSON


# For learning to preform tests ...

# def add_a_and_b_then_subtract_c(a, b, c):
#     '''
#     Function to explain unit testing.
#     given a, b, and c, add a and b. then subtract c.
#     '''
#     return (a + b) - c


def get_computer_name():
    '''
    
    https://docs.python.org/3/library/os.html#os.uname
    Returns information identifying the current operating system. The return value is an object with
    five attributes:

    sysname - operating system name
    nodename - name of machine on network (implementation-defined)
    release - operating system release
    version - operating system version
    machine - hardware identifier

    '''
    user_info = os.uname()
    computer_name = user_info[1]
    return computer_name


def get_ip_address():
    ip_address = socket.gethostbyname(socket.gethostname())
    return ip_address

def get_uptime():
    uptime = subprocess.Popen("uptime")
    return uptime

def get_username():
    username = os.getlogin()
    return username

def get_ssid():
    ssid = subprocess.run(["/System/Library/PrivateFrameworks/Apple80211.framework/Resources/airport", "-I"], capture_output=True)
    return ssid

def get_os_version():
    os_version = subprocess.run(["sw_vers", "-productVersion"], capture_output=True)
    return os_version



def main():
    print(get_computer_name())
    print(get_ip_address())
    print(get_uptime())
    print(get_username())
    print(get_ssid())
    print(get_os_version())
    # pass

if __name__ == '__main__':
    main()