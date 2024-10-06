
import requests

def fuzz_api(base_url):
    common_api_paths = ['/api/v1/users', '/api/v1/login', '/api/v1/data']  # Add more common API paths
    results = []
    for api in common_api_paths:
        url = f"{base_url}{api}"
        response = requests.get(url)
        if response.status_code == 200:
            results.append(f"API Found: {url}")
    return results
