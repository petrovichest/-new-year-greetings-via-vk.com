import time
import requests


token = 'your token'
message_text = 'Happy New Year 🎅🎁🎉🎄🌟🍾🥂✨'

friends = requests.request('GET', f"https://api.vk.com/method/friends.get?access_token={token}&v=5.21").json()['response']['items']
for friend in friends:
    try:
        url = f"https://api.vk.com/method/messages.send?access_token={token}&v=5.21&user_id={friend}&message={message_text}"
        requests.request('GET', url)
    except:
        pass
    time.sleep(1)
