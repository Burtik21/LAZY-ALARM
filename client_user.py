from datetime import datetime

import requests, datetime
import json
url_based = "http://141.147.16.43/"
endpoint = "/api/"
url = url_based + endpoint
hodina = 12
minuta = 0

# Vytvoření objektu time s uživatelským vstupem
cas = datetime.time(hodina, minuta)

print("Zadaný čas:", cas)
data = {
    "cas": cas.strftime("%H:%M")  # Přeformátování času na řetězec
}
headers = {'Content-Type': 'application/json'}

res = requests.post(url,json=data, headers=headers)
print(res.text)

