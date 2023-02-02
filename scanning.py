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
