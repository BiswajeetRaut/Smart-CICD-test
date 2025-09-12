import requests
import subprocess
import time

# Start the app in a subprocess for integration testing
def test_integration_add_numbers():
    proc = subprocess.Popen(["python", "app.py"])
    time.sleep(2)  # wait for server to start

    try:
        response = requests.post("http://127.0.0.1:5000/add", json={"a": 10, "b": 20})
        assert response.status_code == 200
        assert response.json()["sum"] == 30
    finally:
        proc.terminate()
