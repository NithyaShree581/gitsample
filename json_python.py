import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": "Python Learning",
    "body": "Learning API requests",
    "userId": 1
}

response = requests.post(url, json=data)

print(response.status_code)
print(response.json())