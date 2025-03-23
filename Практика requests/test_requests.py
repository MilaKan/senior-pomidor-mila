# import requests
#
# requests.get(url = 'https://api.example.com/data')

import requests

response = requests.get("https://example.com")
print(response.status_code)