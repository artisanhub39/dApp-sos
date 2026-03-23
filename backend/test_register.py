import requests

data = {
    "name": input("Enter name: "),
    "phone": input("Enter phone: "),
    "bike": input("Enter bike number: "),
    "password": input("Enter password: ")
}

response = requests.post(
    "http://127.0.0.1:5000/register",
    json=data
)

print("Status Code:", response.status_code)
print("Response:", response.text)