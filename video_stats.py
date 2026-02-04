import requests
import json

import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="./.env")

CHANNEL_HANDLE = "MrBeast"
API_KEY = os.getenv("API_KEY")
url = f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={CHANNEL_HANDLE}&key={API_KEY}"

def get_playlist_id ():
    
    try:
        response = requests.get(url)

        response.raise_for_status()

        data = response.json()

        #print(json.dumps(data, indent=4))

        channel_items = data["items"][0]
        channel_playlistsId =  channel_items["contentDetails"]["relatedPlaylists"]["uploads"]

        print(channel_playlistsId)
        return channel_playlistsId
    
    except requests.exceptions.RequestException as errex:
        raise errex
    

if __name__ == "__main__":
    get_playlist_id()
    