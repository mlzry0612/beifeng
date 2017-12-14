import requests
import urllib
import json
import string

class Song():
    def __init__(self, album_id, hash, song_name, singer, download_url):
        self.album_id = album_id
        self.hash = hash
        self.song_name = song_name
        self.singer = singer
        self.download_url = download_url


play_url = 'http://www.kugou.com/song/#hash=1201B5A4A57039ACFD226F46E539CB6C&album_id=549266'
song_name = '风筝误'
split = play_url.split('&album_id=')
album_id= split[1]
file_hash = split[0].split('#hash=')[1]
songs = []


def get_download_url(url):
    global songs_metadata
    get = requests.get(url)
    songs_metadata = json.loads(get.text)
    return songs_metadata['data']['play_url']


pre_download_url = 'http://www.kugou.com/yy/index.php?r=play/getdata&hash=' + file_hash + '&album_id=' + album_id + '&_=1512833230864'
response = requests.get(pre_download_url)
songs.append(Song(album_id, file_hash, song_name, '', get_download_url(pre_download_url)))


x = len(songs)
for song in songs:
    print('***** ' + song.song_name + '.mp3 *****' + ' Downloading...')
    try:
        urllib.request.urlretrieve(song.download_url, './music/' +  song.song_name + '.mp3')
    except Exception as e:
        print(e)
        x = x - 1
        print('Download wrong~')
