# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://tvasavi.atlassian.net/rest/api/3/issue"
API_TOKEN = "ATATT3xFfGF0UuWP4geyj0h55SJoMxYkxtfShKYBf8PqoQybZ1CBB4RjyT-KJEDMtJRhEUfyslWAEJcR3ckkNoPZheUZ5tYx31UCRAc6p2cq0e2ozdkKzTqdbhtSCWLLDu38R-GqIBQL964Yvq35fTDzhMm75jEbASisM-_iAjAoHd1OV7tz9FU=D5C6E7EA"


auth = HTTPBasicAuth("vasavi.balanagu@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "Order entry fails when selecting supplier.",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    "summary": "Git hub ticket test",    
    "issuetype": {
      "id": "10006"
    },
    "labels": [
      "bugfix",
      "blitz_test"
    ],
    "project": {
      "key": "TVAS"
    }
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))