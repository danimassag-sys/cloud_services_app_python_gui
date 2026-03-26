# ULTIMATE Cloud Desktop Platform (Enterprise Level)
# PyQt5 + FastAPI backend + AWS + Docker + Monitoring

# ================= BACKEND (FastAPI) =================
from fastapi import FastAPI
import boto3
import docker
import psutil

app = FastAPI()

ec2 = boto3.client('ec2')
docker_client = docker.from_env()

@app.get("/servers/ec2")
def list_ec2():
    res = ec2.describe_instances()
    instances = []
    for r in res['Reservations']:
        for i in r['Instances']:
            instances.append({
                "id": i['InstanceId'],
                "state": i['State']['Name']
            })
    return instances

@app.post("/servers/ec2/start/{instance_id}")
def start_ec2(instance_id: str):
    ec2.start_instances(InstanceIds=[instance_id])
    return {"status": "starting"}

@app.post("/servers/ec2/stop/{instance_id}")
def stop_ec2(instance_id: str):
    ec2.stop_instances(InstanceIds=[instance_id])
    return {"status": "stopping"}

@app.get("/docker")
def list_containers():
    return [{"name": c.name, "status": c.status} for c in docker_client.containers.list(all=True)]

@app.post("/docker/start/{name}")
def start_container(name: str):
    c = docker_client.containers.get(name)
    c.start()
    return {"status": "started"}

@app.post("/docker/stop/{name}")
def stop_container(name: str):
    c = docker_client.containers.get(name)
    c.stop()
    return {"status": "stopped"}

@app.get("/monitor")
def monitor():
    return {
        "cpu": psutil.cpu_percent(),
        "ram": psutil.virtual_memory().percent
    }

# ================= DESKTOP GUI =================
import sys
import requests
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton,
    QListWidget, QLabel
)

API = "http://localhost:8000"

class CloudDashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ULTIMATE Cloud Manager")
        self.resize(700, 500)

        layout = QVBoxLayout()

        self.label = QLabel("Monitoring")
        layout.addWidget(self.label)

        self.refresh_btn = QPushButton("Refresh")
        self.refresh_btn.clicked.connect(self.load_all)
        layout.addWidget(self.refresh_btn)

        self.ec2_list = QListWidget()
        layout.addWidget(QLabel("EC2 Instances"))
        layout.addWidget(self.ec2_list)

        self.docker_list = QListWidget()
        layout.addWidget(QLabel("Docker Containers"))
        layout.addWidget(self.docker_list)

        layout.addWidget(self.refresh_btn)

        self.setLayout(layout)
        self.load_all()

    def load_all(self):
        try:
            ec2 = requests.get(f"{API}/servers/ec2").json()
            self.ec2_list.clear()
            for i in ec2:
                self.ec2_list.addItem(f"{i['id']} - {i['state']}")

            containers = requests.get(f"{API}/docker").json()
            self.docker_list.clear()
            for c in containers:
                self.docker_list.addItem(f"{c['name']} - {c['status']}")

            monitor = requests.get(f"{API}/monitor").json()
            self.label.setText(f"CPU: {monitor['cpu']}% | RAM: {monitor['ram']}%")
        except Exception as e:
            self.label.setText(str(e))

# ================= RUN =================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CloudDashboard()
    window.show()
    sys.exit(app.exec_())