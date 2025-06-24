import requests

response = requests.get("http://172.16.1.119:11434/api/tags")
if response.status_code == 200:
    models = response.json().get("models", [])
    for model in models:
        print(model["name"])
else:
    print("Failed to fetch models:", response.status_code)