from censys import search

API_ID = 'YOUR_API_ID'
API_SECRET = 'YOUR_API_SECRET'

def censys_ip_query(ip):
    c = search.CensysIPv4(API_ID, API_SECRET)
    return c.view(ip)

def censys_bulk_ip_query(ips):
    c = search.CensysIPv4(API_ID, API_SECRET)
    return c.search(' OR '.join(ips))

# Example usage for single IP query
ip_address = '8.8.8.8'
response = censys_ip_query(ip_address)
if response:
    print(f"Results for {ip_address}:")
    print(response)

# Example usage for bulk IP query
ip_addresses = ['8.8.8.8', '1.1.1.1']
response = censys_bulk_ip_query(ip_addresses)
if response:
    print("Bulk results:")
    print(response)
