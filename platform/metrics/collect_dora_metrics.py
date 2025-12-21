import os
import requests
from datetime import datetime, timezone

GITHUB_REPO = os.getenv("GITHUB_REPOSITORY")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}

def get_workflow_runs():
    url = f"https://api.github.com/repos/{GITHUB_REPO}/actions/runs"
    r = requests.get(url, headers=HEADERS)
    r.raise_for_status()
    return r.json()["workflow_runs"]

def calculate_deployment_frequency(runs):
    deploys = [r for r in runs if "CD" in r["name"] and r["conclusion"] == "success"]
    return len(deploys)

def calculate_lead_time(runs):
    completed = [r for r in runs if r["conclusion"] == "success"]
    if not completed:
        return 0
    times = []
    for r in completed:
        start = datetime.fromisoformat(r["created_at"].replace("Z","")).replace(tzinfo=timezone.utc)
        end = datetime.fromisoformat(r["updated_at"].replace("Z","")).replace(tzinfo=timezone.utc)
        times.append((end-start).total_seconds())
    return sum(times)/len(times)

if __name__ == "__main__":
    runs = get_workflow_runs()
    print("deployment_frequency", calculate_deployment_frequency(runs))
    print("avg_lead_time_seconds", round(calculate_lead_time(runs), 2))
