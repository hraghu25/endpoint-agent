import requests
import yaml
import time
import argparse
from datetime import datetime

LOG_FILE = "./urlmonitoring.log"

def log_info(msg):
    with open(LOG_FILE, 'a') as f:
        f.write(f"[INFO] {datetime.now()} :: {msg}\n")

def log_error(msg):
    with open(LOG_FILE, 'a') as f:
        f.write(f"[ERROR] {datetime.now()} :: {msg}\n")

def log_debug(msg):
    with open(LOG_FILE, 'a') as f:
        f.write(f"[DEBUG] {datetime.now()} :: {msg}\n")

def check_status(url):
    try:
        response = requests.head(url)
        http_status = response.status_code
        log_debug(f"Received HTTP status code for {url} is {http_status}")
        if http_status == 200:
            log_info(f"Response code for {url} is {http_status}")
        else:
            log_error(f"Failed to get response for {url} code {http_status}")
    except requests.RequestException as e:
        log_error(f"Error querying {url}: {e}")

def main():

    parser = argparse.ArgumentParser(description='URL Monitor Script')
    parser.add_argument('--config_file', required=True, help='Path to the configuration YAML file.')
    args = parser.parse_args()

    with open(args.config_file, 'r') as f:
        data = yaml.safe_load(f)
        urls_path = data.get('urls_path', [])

    with open(urls_path, 'r') as f:
        data = yaml.safe_load(f)
        urls = data.get('urls', [])
    
    for url in urls:
        check_status(url)
        time.sleep(3)

if __name__ == "__main__":
    main()
    
