import requests
import urllib.parse

def fetch_location_data(parsed_data: dict) -> str | None:
    zip_code = parsed_data.get("zip_code")
    state = parsed_data.get("state")
    city = parsed_data.get("city")
    url = None

    is_zip_lookup = bool(zip_code and not city)

    if zip_code:
        url = f"https://api.zippopotam.us/us/{zip_code}"
    elif city and state:
        city_encoded = urllib.parse.quote(city)
        url = f"https://api.zippopotam.us/us/{state}/{city_encoded}"
    
    if not url: return None

    try:
        response = requests.get(url, timeout=5)
        if response.status_code != 200: return None
        data = response.json()

        res_city, res_state, res_zip = None, None, None

        if is_zip_lookup:
            if "places" in data:
                place = data["places"][0]
                res_city = place.get("place name")
                res_state = place.get("state abbreviation")
                res_zip = data.get("post code")
        else:
            res_city = data.get("place name")
            res_state = data.get("state abbreviation")
            if data.get("places"):
                res_zip = data["places"][0].get("post code")
        
        # --- ЗМІНА ТУТ: Нова логіка форматування рядка ---
        city_state_part = ", ".join(filter(None, [res_city, res_state]))
        final_parts = [part for part in [city_state_part, res_zip] if part]

        if not final_parts: return None

        return " ".join(final_parts)

    except requests.exceptions.RequestException as e:
        print(f"Помилка API запиту: {e}")
        return None