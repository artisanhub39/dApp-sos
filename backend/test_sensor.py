import requests

data = {
    "phone": input("Enter phone: ")
}

response = requests.post(
    "http://127.0.0.1:5000/trigger",
    json=data
)

print("Status Code:", response.status_code)
print("Response:", response.text)