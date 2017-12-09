import requests
import json

get = requests.get(
    'http://www.kugou.com/yy/index.php?r=play/getdata&hash=218E34427EF3D0DDE74282CE865E5308&album_id=1076457&_=1512833230864')
songs_metadata = json.loads(get.text)
print(songs_metadata['data']['play_url'])
