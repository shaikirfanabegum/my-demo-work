import os
import time
import requests
from datetime import datetime, timezone
from prometheus_client import start_http_server, Gauge

deploy_freq = Gauge("dora_deployment_frequency", "Deployment Frequency (count of successful CD runs in recent window)")
lead_time = Gauge("dora_avg_workflow_duration_seconds", "Average CI/CD workflow duration (seconds)")

def get_runs(repo, token, per_page=50):
    url = f"https://api.github.com/repos/{repo}/actions/runs?per_page={per_page}"
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json"}
    r = requests.get(url, headers=headers, timeout=30)
    r.raise_for_status()
    return r.json().get("workflow_runs", [])

def compute(repo, token):
    runs = get_runs(repo, token)

    # Deployment frequency: successful workflows with "CD" in name (adjust if your workflow name differs)
    cd = [r for r in runs if ("CD" in (r.get("name") or "") or "cd" in (r.get("name") or "").lower()) and r.get("conclusion") == "success"]
    deploy_freq.set(len(cd))

    # Avg duration (simple proxy you can explain; later you can compute true lead-time commit->prod)
    durations = []
    for r in runs:
        if r.get("conclusion") != "success":
            continue
        created = r.get("created_at")
        updated = r.get("updated_at")
        if not created or not updated:
            continue
        start = datetime.fromisoformat(created.replace("Z", "+00:00")).astimezone(timezone.utc)
        end = datetime.fromisoformat(updated.replace("Z", "+00:00")).astimezone(timezone.utc)
        durations.append((end - start).total_seconds())

    lead_time.set(sum(durations)/len(durations) if durations else 0.0)

if __name__ == "__main__":
    repo = os.environ.get("GITHUB_REPOSITORY", "shaikirfanabegum/humana-ai-ml-devops-demo")
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        raise SystemExit("GITHUB_TOKEN env var not set. Create a GitHub PAT with repo read access and export it.")

    start_http_server(9105)
    while True:
        try:
            compute(repo, token)
        except Exception as e:
            # exporter should stay alive even if GitHub API hiccups
            print("collector error:", e)
        time.sleep(60)
