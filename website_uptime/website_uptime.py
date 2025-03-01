import requests
import time

def check_website(url):
    try:
        response=requests.get(url)
        if response.status_code == 200:
            print(f"Website {url} is up and running fine")
        else:
            print(f"Website {url} returned with the status : {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error checking the website {url}: {e}")


url = 'https://www.geeksforgeeks.org/hangman-game-python/?ref=lbp'

while True:
    check_website(url)
    time.sleep(10)
