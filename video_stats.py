import requests

import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="./.env")

API_KEY = os.getenv("API_KEY")
url1 = f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle=MrBeast&key={API_KEY}"


def get_playlist_id():
    try:
        response = requests.get(url1)
        response.raise_for_status()
        data = response.json()
    except:
        data = {
            "kind": "youtube#channelListResponse",
            "etag": "mky5yfatRnp-E8N9-BwXGY8W8Dk",
            "pageInfo": {
                "totalResults": 1,
                "resultsPerPage": 5
            },
            "items": [{
                "kind": "youtube#channel",
                "etag": "-f8h6RTCebSZttPcDz3dTkMV5yo",
                "id": "UCX6OQ3DkcsbYNE6H8uQQuVA",
                "contentDetails": {
                    "relatedPlaylists": {
                        "likes": "",
                        "uploads": "UUX6OQ3DkcsbYNE6H8uQQuVA"
                    }
                }
            }]
        }

    channel_items = data["items"][0]
    channel_playlistId = channel_items["contentDetails"]["relatedPlaylists"]["uploads"]
    print(channel_playlistId)
    return channel_playlistId

if __name__=="__main__":
    get_playlist_id()
# url2 = "https://accounts.rbstaging.in/api/v1/partners_list/"

# headers = {
#     "Content-Type": "application/json",
#     "secret-key": "dCr8hEr8WWaSlxoNrh6Dst9PLzWQJnqD",
#     "Api-key": "945dbc41-8587-4c62-82ca-741f914077cf",
# }

# payload = {
#     "as_on": "01/07/2025",
#     "return_type": "unique_code",
#     "users": ["EM00024739"],
#     "include": ["_email"],
# }

# try:
#     response = requests.post(url2, headers=headers, json=payload, timeout=30)
#     print("Status code:", response.status_code)

#     try:
#         print("Response JSON:", response.json())
#     except ValueError:
#         print("Response text:", response.text)
# except requests.exceptions.RequestException as exc:
#     print("Request failed:", exc)


