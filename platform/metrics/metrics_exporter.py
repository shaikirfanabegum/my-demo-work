from prometheus_client import start_http_server, Gauge
import subprocess
import time

deploy_freq = Gauge("dora_deployment_frequency", "Deployment Frequency")
lead_time = Gauge("dora_lead_time_seconds", "Average Lead Time (seconds)")

def collect():
    output = subprocess.check_output(["python", "collect_dora_metrics.py"]).decode()
    for line in output.splitlines():
        k, v = line.split()
        if k == "deployment_frequency":
            deploy_freq.set(float(v))
        if k == "avg_lead_time_seconds":
            lead_time.set(float(v))

if __name__ == "__main__":
    start_http_server(9105)
    while True:
        collect()
        time.sleep(300)
