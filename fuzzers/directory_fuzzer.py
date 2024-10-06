
import requests

def fuzz_directories(base_url):
    wordlist = ['admin', 'login', 'backup', 'test']  # Extend this list as needed
    results = []
    for word in wordlist:
        url = f"{base_url}/{word}/"
        response = requests.get(url)
        if response.status_code == 200:
            results.append(f"Found: {url}")
    return results
