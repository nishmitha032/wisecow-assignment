import requests
import time

APP_URL = "http://localhost:5000"  # Replace with your Flask app's URL
CHECK_INTERVAL = 60  # Check every 60 seconds

def check_application():
    try:
        response = requests.get(APP_URL, timeout=5)
        if response.status_code == 200:
            print(f"{time.ctime()}: Application is UP!")
        else:
            print(f"{time.ctime()}: Application is DOWN! Status: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"{time.ctime()}: Application is DOWN! Error: {e}")

# Main function
if __name__ == "__main__":
    while True:
        check_application()
        time.sleep(CHECK_INTERVAL)
