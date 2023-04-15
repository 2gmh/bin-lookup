import requests

bin_number = input("Escribe un bin: ")

response = requests.get(f"https://lookup.binlist.net/{bin_number}")

if response.status_code == 200:
    data = response.json()
    scheme = data.get("scheme", "None")
    brand = data.get("brand", "None")
    bank_name = data["bank"].get("name", "None")
    bank_url = data["bank"].get("url", "None")
    bank_phone = data["bank"].get("phone", "None")
    bank_city = data["bank"].get("city", "None")
    country_name = data["country"].get("name", "None")
    country_alpha2 = data["country"].get("alpha2", "None")
    country_alpha3 = data["country"].get("alpha3", "None")
    country_numeric = data["country"].get("numeric", "None")
    currency = data["country"].get("currency", "None")
    latitude = data["country"].get("latitude", "None")
    longitude = data["country"].get("longitude", "None")
    
    print(f"BIN: {bin_number}")
    print(f"Scheme: {scheme}")
    print(f"Brand: {brand}")
    print(f"Bank Name: {bank_name}")
    print(f"Bank URL: {bank_url}")
    print(f"Bank Phone: {bank_phone}")
    print(f"Bank City: {bank_city}")
    print(f"Country Name: {country_name}")
    print(f"Country Alpha2: {country_alpha2}")
    print(f"Country Alpha3: {country_alpha3}")
    print(f"Country Numeric: {country_numeric}")
    print(f"Currency: {currency}")
    print(f"Latitude: {latitude}")
    print(f"Longitude: {longitude}")
else:
    print("No se pudo obtener la información del BIN.")