import requests

url = ""

class cause1(Exception):
    pass

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    res = response.json()

except requests.exceptions.ConnectionError:
    print("Connection_failed")

except requests.exceptions.MissingSchema :
    raise cause1("There is no proper URL")

except cause1:
    print("There is no proper URL and the URL is not there")