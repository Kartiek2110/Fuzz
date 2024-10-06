
import dns.resolver

def fuzz_subdomains(domain):
    subdomains = ['www', 'mail', 'dev', 'staging']
    results = []
    resolver = dns.resolver.Resolver()
    
    for sub in subdomains:
        try:
            answers = resolver.resolve(f"{sub}.{domain}")
            results.append(f"Found subdomain: {sub}.{domain}")
        except dns.resolver.NXDOMAIN:
            pass
    return results
