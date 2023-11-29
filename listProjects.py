# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://tvasavi.atlassian.net/rest/api/3/project"
API_TOKEN = "ATATT3xFfGF0UuWP4geyj0h55SJoMxYkxtfShKYBf8PqoQybZ1CBB4RjyT-KJEDMtJRhEUfyslWAEJcR3ckkNoPZheUZ5tYx31UCRAc6p2cq0e2ozdkKzTqdbhtSCWLLDu38R-GqIBQL964Yvq35fTDzhMm75jEbASisM-_iAjAoHd1OV7tz9FU=D5C6E7EA"

auth = HTTPBasicAuth("vasavi.balanagu@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

output = json.loads(response.text)
print(output[0]["name"]) #To print project name
