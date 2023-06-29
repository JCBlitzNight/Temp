import ipaddress
import csv

# Path to the CSV file
csv_file = 'path/to/csv/file.csv'

# Path to the text file containing IP addresses
ip_file = 'path/to/ip/file.txt'

# Read IP ranges, ISPs, and countries from the CSV file
ip_ranges = {}
with open(csv_file, 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        country = row[0]
        ip_range = row[1]
        isp = row[2]
        ip_ranges[ip_range] = isp

# Function to check if an IP address falls within a subnet
def ip_in_subnet(ip, subnet):
    ip_obj = ipaddress.ip_address(ip)
    network_obj = ipaddress.ip_network(subnet)
    return ip_obj in network_obj

# Process each IP address from the text file
with open(ip_file, 'r') as file:
    for line in file:
        ip = line.strip()
        found = False
        for subnet in ip_ranges:
            if ip_in_subnet(ip, subnet):
                print(f'{ip}: {ip_ranges[subnet]}')
                found = True
                break
        if not found:
            print(f'{ip}: Unknown')
