
import requests

def fuzz_vhosts(base_url):
    subdomains = ['test', 'dev', 'staging']  # Add more common subdomains
    results = []
    for subdomain in subdomains:
        headers = {'Host': f"{subdomain}.{base_url}"}
        response = requests.get(base_url, headers=headers)
        if response.status_code == 200:
            results.append(f"Found Virtual Host: {subdomain}.{base_url}")
    return results
