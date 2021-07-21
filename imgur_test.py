import requests
import json
import random
from imgurpython import ImgurClient

# https://api.imgur.com/oauth2/authorize?client_id=45c5fa72783a4a1&response_type=token
# https://imgur.com/#access_token=bb78ece57ea10eade629cc95fa41ff2484a96dc9&expires_in=315360000&token_type=bearer&refresh_token=361de638c55dc5065c25ad47fd3099413db7f70d&account_username=DarkScorpio&account_id=18989397

client_id = '45c5fa72783a4a1'
client_secret = '37b3e1ff6c5b591c0f4807ddc327b150f8f7b4ca'
refresh_token = '361de638c55dc5065c25ad47fd3099413db7f70d'
account = 'DarkScorpio'
account_id = '18989397'

url = "https://api.imgur.com/oauth2/token"
payload={'refresh_token': '361de638c55dc5065c25ad47fd3099413db7f70d',
'client_id': client_id,
'client_secret': client_secret,
'grant_type': 'refresh_token'}
response = requests.post(url, data=payload)
response_json = json.loads(response.text)
access_token = response_json['access_token']

client = ImgurClient(client_id, client_secret, access_token, refresh_token)
items = client.get_album_images('1n919ks')
print(f"Image count: {len(items)}")
image_url_list = [item.link for item in items]
enumerated_list = list(enumerate(image_url_list))
# random_pair = random.choice(enumerated_list)

# with open('lore.py', 'w') as f:
#     f.write(str(enumerated_list))