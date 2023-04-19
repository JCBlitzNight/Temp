import csv

# IP addresses and number of failed login attempts
ip_count = {}

# Threshold for number of failed login attempts
threshold = 10

# Read network logs from a CSV file
with open('network_logs.csv', 'r') as logs:
    logs_reader = csv.reader(logs)
    for row in logs_reader:
        if 'failed login' in row[4]:
            ip = row[2]
            if ip in ip_count:
                ip_count[ip] += 1
            else:
                ip_count[ip] = 1

# Identify IP addresses that exceeded the threshold
brute_forcers = [ip for ip, count in ip_count.items() if count >= threshold]

# Print the identified IP addresses
print("Brute Forcers:")
for ip in brute_forcers:
    print(ip)

    
 def is_sequential_ports(port_list):
    if len(port_list) < 3:
        return False
    
    port_list = sorted(port_list)
    for i in range(len(port_list) - 2):
        if port_list[i+1] == port_list[i]+1 and port_list[i+2] == port_list[i]+2:
            return True
    
    return False

from itertools import groupby

def is_sequential(ip_list):
    # Group IP addresses by subnet
    subnet_groups = []
    for subnet, ips in groupby(sorted(ip_list), lambda ip: '.'.join(ip.split('.')[:3])):
        subnet_groups.append(list(ips))

    # Check for sequential IPs in each subnet group
    for subnet_ips in subnet_groups:
        if len(subnet_ips) < 3:
            continue
        sorted_ips = sorted(subnet_ips, key=lambda ip: [int(num) for num in ip.split('.')])
        for i in range(len(sorted_ips) - 2):
            current_ip = sorted_ips[i].split('.')
            next_ip = sorted_ips[i + 1].split('.')
            after_next_ip = sorted_ips[i + 2].split('.')
            if (int(next_ip[3]) - int(current_ip[3]) == 1 and
                int(after_next_ip[3]) - int(next_ip[3]) == 1):
                return True
    return False

# define the necessary constants and structures
STD_OUTPUT_HANDLE = -11
class CONSOLE_CURSOR_INFO(ctypes.Structure):
    _fields_ = [("dwSize", ctypes.c_int), ("bVisible", ctypes.c_long)]

def hide_cursor():
    # get the console handle and cursor info
    handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    cursor_info = CONSOLE_CURSOR_INFO()
    ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(cursor_info))

    # set the cursor visibility to False
    cursor_info.bVisible = False
    ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(cursor_info))

def show_cursor():
    # get the console handle and cursor info
    handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    cursor_info = CONSOLE_CURSOR_INFO()
    ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(cursor_info))

    # set the cursor visibility to True
    cursor_info.bVisible = True
    ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(cursor_info))
