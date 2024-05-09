import os
from datetime import datetime

import requests

login_url = f"{os.environ['SERVICE_URL']}/auth/login"
print("logging in", login_url)
response = requests.post(
    login_url,
    json={"user": os.environ["USERNAME"], "password": os.environ["PASSWORD"]},
)
if not response.ok:
    print(response.text)
    exit(-1)

data = response.json()
token = data.pop("token")

print("sending notifications...")
date = datetime.now().isoformat()
response = requests.post(
    f"{os.environ['SERVICE_URL']}/notifications/weekly",
    json={"date": date},
    headers={"Authorization": f"Bearer {token}"},
)

if not response.ok:
    print(response.text)
    exit(-1)

print("Done. Notifications sent.")
