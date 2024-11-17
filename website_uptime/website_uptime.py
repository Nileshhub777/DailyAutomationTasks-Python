import requests
import time

def check_website(url):
    try:
        response = requests.get(url)
        if requests.status_codes == 200:
            print(f"Website {url} is up")
        else:
            print(f"website {url} returned status code {response.status_code}" )
    except requests.exceptions.RequestException as e:
        print(f"Error checking website {url}: {e}")


url='https://www.google.com'

while True:
    check_website(url)
    time.sleep(20)
