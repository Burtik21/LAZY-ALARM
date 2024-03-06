import requests

url_based = "http://141.147.16.43/"
endpoint = "/api/"
url = url_based + endpoint

# Specifikujeme hlavičky Content-Type
headers = {'Content-Type': 'application/json'}

response = requests.get(url, headers=headers)
print(response)
print(response.json())
# Kontrola stavového kódu odpovědi
if response.status_code == 200:
    # Získání dat z odpovědi
    data = response.json()
    print("Data získaná ze serveru:", data)
else:
    print("Došlo k chybě při získávání dat ze serveru.")
