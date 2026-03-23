import requests

def sensor_trigger():
    data = {"phone": "+91XXXXXXXXXX", "bike": "AP31AB1234"}
    requests.post("http://localhost:5000/sensor", json=data)

if __name__ == "__main__":
    sensor_trigger()