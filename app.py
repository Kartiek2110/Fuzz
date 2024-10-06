
from flask import Flask, render_template, request
from fuzzers.directory_fuzzer import fuzz_directories
from fuzzers.vhost_fuzzer import fuzz_vhosts
from fuzzers.api_fuzzer import fuzz_api
from fuzzers.param_fuzzer import fuzz_params
from fuzzers.subdomain_fuzzer import fuzz_subdomains

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fuzz', methods=['POST'])
def fuzz():
    url = request.form['url']
    directory_results = fuzz_directories(url)
    vhost_results = fuzz_vhosts(url)
    api_results = fuzz_api(url)
    param_results = fuzz_params(url)
    subdomain_results = fuzz_subdomains(url)
    
    return render_template('results.html', 
                           directories=directory_results, 
                           vhosts=vhost_results, 
                           apis=api_results, 
                           params=param_results, 
                           subdomains=subdomain_results)

if __name__ == "__main__":
    app.run(debug=True)
