import requests
from secret import client_secret, client_id

class Stream:
    def __init__(self, title, streamer, game):
        self.title = title
        self.streamer = streamer
        self.game = game

# getting auth token from twitch api
def get_oauth_token():
    body = {
        'client_id' : client_id,
        'client_secret' : client_secret,
        "grant_type" : 'client_credentials'
    }
    r = requests.post('https://id.twitch.tv/oauth2/token', body)

    # data output
    keys = r.json()
    return keys['access_token']

def check_if_live(channel):
    #calling the twitch api to check if a specific channel is live
    url = "https://api.twitch.tv/helix/streams?user_login=" + channel
    token = get_oauth_token()
    HEADERS = {
        'Client-ID' : client_id,
        'Authorization' : 'Bearer' + token
    }

    try:
        req = requests.get(url, headers=HEADERS)
        res = req.json()
        if len(res['data']) > 0: #the channel is live
            data = res['data'][0]
            title = data['title']
            streamer = data['user_name']
            game = data['game_name']
            thumbnail_url = data['thumbnail_url']
            stream = Stream(title, streamer, game, thumbnail_url)
            return stream
        else:
            return "OFFLINE"
    except Exception as e:
        print(e)
        return "An error has occurred: " + str(e)
                