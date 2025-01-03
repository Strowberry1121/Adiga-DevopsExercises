import docker
import time

client = docker.from_env()

def check_flask_health():
    try:
        flask_container = client.containers.get('flask_app')
        if flask_container.status != 'running':
            print("Flask app is not running, restarting...")
            flask_container.restart()
        else:
            print("Flask app is running and healthy.")
    except docker.errors.NotFound:
        print("Flask container not found.")

while True:
    print("Checking container health...")
    check_flask_health()
    time.sleep(60)  # Check every 60 seconds