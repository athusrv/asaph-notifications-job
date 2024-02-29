import os
from datetime import datetime

import requests


def execute():
    response = requests.post(
        f"{os.environ['SERVICE_URL']}/auth/login",
        json={"user": os.environ["USERNAME"], "password": os.environ["PASSWORD"]},
    )
    if not response.ok:
        return response.text

    data = response.json()
    token = data.pop("token")

    date = datetime.now().isoformat()
    response = requests.post(
        f"{os.environ['SERVICE_URL']}/notifications/weekly",
        json={"date": date},
        headers={"Authorization": f"Bearer {token}"},
    )

    if not response.ok:
        return response.text

    return "Done. Notifications sent."


if __name__ == "__main__":
    print(execute())
