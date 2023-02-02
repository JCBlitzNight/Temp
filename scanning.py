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

    
    TCP Connect Scan: Detects a full three-way handshake, with the SYN, SYN-ACK, and ACK packets.

TCP SYN Scan: Detects SYN packets sent to a target without completing the three-way handshake.

TCP FIN Scan: Detects FIN packets sent to a target to determine which ports are open or closed.

TCP Null Scan: Detects packets with all flags set to zero, which can be used to identify open ports.

TCP Xmas Scan: Detects packets with the FIN, PSH, and URG flags set, which can be used to identify open ports.

UDP Scan: Detects packets sent to UDP ports, which can be used to identify open or closed ports.

ACK Scan: Detects ACK packets sent to a target to determine which ports are open or closed.

Window Scan: Detects the size of the TCP window on a target, which can be used to identify open or closed ports.

Maimon Scan: Detects packets sent with the ACK and URG flags set, which can be used to identify open ports.
