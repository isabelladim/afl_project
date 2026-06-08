import requests
import pandas as pd

def get_team_games(year, teams, user_agent):
    response = requests.get(f"https://api.squiggle.com.au/?q=games;year={year};team={teams}", headers={"User-Agent": user_agent})
    data = response.json()
    return pd.DataFrame(data["games"])

def get_afl_info(url_extension, year, user_agent):
    response = requests.get(f"https://api.squiggle.com.au/?q={url_extension};year={year}", headers={"User-Agent": user_agent})
    data = response.json()
    return pd.DataFrame(data[url_extension])


