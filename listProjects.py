# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://tvasavi.atlassian.net/rest/api/3/project"
API_TOKEN = "ATATT3xFfGF05oRCaIE1dirgeK-_4cbiCp4ZqUbTFsZBFqMntBjqw2fcz1F6oY5yWm0EUSdblnLdBLx3rsrO4yBtx0heEPTf9dpKZr6-NURgPdJASxYwwPxL4_VJtbfCkQXRBt-VQdjOMlVhOJmLFz93mtlxqW15VIHTlxCE8hcQYdAV52S1WWE=66E960BF"

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
name = output[0]["name"]
print(name)
