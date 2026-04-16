import requests
import subprocess
import os

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
        "Authorization": f"Bearer {token}"
    }

    params = {
        "testPlanKey": "PROJ-200"   # 👈 YOUR TEST PLAN KEY
    }

    files = {
        "file": open("reports/cucumber.json", "rb")
    }

    response = requests.post(url, headers=headers, params=params, files=files)

    print("Upload response:", response.text)

if __name__ == "__main__":
    run_tests()
    token = get_token()
    upload_results(token)