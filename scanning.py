import requests
import json

API_URL = 'https://censys.io/api/v1'
API_ID = 'YOUR_API_ID'
API_SECRET = 'YOUR_API_SECRET'

def censys_ip_query(ip):
    endpoint = f"/view/ipv4/{ip}"
    return censys_api_request(endpoint)

def censys_bulk_ip_query(ips):
    endpoint = '/search/ipv4'
    data = {'query': ' OR '.join(ips)}
    return censys_api_request(endpoint, data)

def censys_api_request(endpoint, data=None):
    url = f"{API_URL}{endpoint}"
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }
    auth = (API_ID, API_SECRET)
    
    try:
        response = requests.post(url, headers=headers, auth=auth, data=json.dumps(data))
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

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
