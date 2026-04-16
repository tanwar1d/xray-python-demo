import requests
import subprocess
import os
import json

XRAY_CLIENT_ID = os.getenv("XRAY_CLIENT_ID")
XRAY_CLIENT_SECRET = os.getenv("XRAY_CLIENT_SECRET")

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

    params = {
        "testPlanKey": "SAU-24"   # 👈 replace with your actual Test Plan key
    }

    with open("reports/cucumber.json") as f:
        data = json.load(f)

    response = requests.post(url, headers=headers, params=params, json=data)

    print("Status Code:", response.status_code)
    print("Upload response:", response.text)

if __name__ == "__main__":
    run_tests()
    token = get_token()
    upload_results(token)