import requests
import subprocess

XRAY_CLIENT_ID = "YOUR_CLIENT_ID"
XRAY_CLIENT_SECRET = "YOUR_CLIENT_SECRET"

def get_token():
    url = "https://xray.cloud.getxray.app/api/v2/authenticate"
    payload = {
        "client_id": XRAY_CLIENT_ID,
        "client_secret": XRAY_CLIENT_SECRET
    }

    response = requests.post(url, json=payload)
    return response.text.strip('"')

def run_tests():
    subprocess.run("behave -f json -o reports/cucumber.json", shell=True)

def upload_results(token):
    url = "https://xray.cloud.getxray.app/api/v2/import/execution/cucumber"

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    with open("reports/cucumber.json") as f:
        data = f.read()

    response = requests.post(url, headers=headers, data=data)
    print("Upload response:", response.text)

if __name__ == "__main__":
    run_tests()
    token = get_token()
    upload_results(token)