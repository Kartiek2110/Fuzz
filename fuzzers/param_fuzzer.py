
import requests

def fuzz_params(base_url):
    params = {'id': '1', 'search': 'test'}
    payloads = ["' OR 1=1 --", "<script>alert(1)</script>", "'; DROP TABLE users; --"]
    results = []
    
    for key, value in params.items():
        for payload in payloads:
            param_value = {key: value + payload}
            response = requests.get(base_url, params=param_value)
            if "error" in response.text or response.status_code == 500:
                results.append(f"Potential vulnerability with {key}: {payload}")
    return results
