import requests

def get_afl_info(url_extension, year, user_agent):
    url = f"https://api.squiggle.com.au/?q={url_extension};year={year}"
    response = requests.get(url, headers={"User-Agent": user_agent}, timeout=30)
    response.raise_for_status()
    return response.json()[url_extension]

