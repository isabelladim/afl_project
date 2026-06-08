import requests
import pandas as pd

def get_api_info(url_extension, year, teams, user_agent):
    response = requests.get(f"https://api.squiggle.com.au/?q={url_extension};year={year};team={teams}", headers={"User-Agent": user_agent})
    data = response.json()
    return pd.DataFrame(data[url_extension])

def get_ladder_info(year, user_agent):
    response = requests.get(f"https://api.squiggle.com.au/?q=standings;year={year}", headers={"User-Agent": user_agent})
    data = response.json()
    return pd.DataFrame(data["standings"])


