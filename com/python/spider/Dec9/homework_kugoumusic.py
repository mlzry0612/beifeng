import requests
import urllib
import json


class Song():
    def __init__(self, album_id, hash, song_name, singer, download_url):
        self.album_id = album_id
        self.hash = hash
        self.song_name = song_name
        self.singer = singer
        self.download_url = download_url


word = '爱情'
res1 = requests.get(
    'http://songsearch.kugou.com/song_search_v2?callback=jQuery112408136929846265539_1512831517754&page=1&pagesize=30&userid=-1&clientver=&platform=WebFilter&tag=em&filter=2&iscorrection=1&privilege_filter=0&_=1512831517756&keyword=' + word)
context = res1.text.strip('jQuery1234567890_()')[:-2]
print(context)
songs_metadata = json.loads(context)
songs_data = songs_metadata['data']['lists']
songs = []


def get_download_url(url):
    global songs_metadata
    get = requests.get(url)
    songs_metadata = json.loads(get.text)
    return songs_metadata['data']['play_url']


for data in songs_data:
    song_name = data['SongName'].replace('<em>', '').replace('</em>', '')
    pre_download_url = 'http://www.kugou.com/yy/index.php?r=play/getdata&hash=' + data['FileHash'] + '&album_id=' + \
                       data['AlbumID'] + '&_=1512833230864'
    response = requests.get(pre_download_url)
    songs.append(Song(data['AlbumID'], data['FileHash'], song_name, data['SingerName'], get_download_url(pre_download_url)))


print('For ' + word + ' Start download...')
x = len(songs)
for song in songs:
    print('***** ' + song.singer + ' - ' + song.song_name + '.mp3 *****' + ' Downloading...')
    try:
        urllib.request.urlretrieve(song.download_url, './music/' + song.singer + ' - ' + song.song_name + '.mp3')
    except Exception as e:
        print(e)
        x = x - 1
        print('Download wrong~')
print('For [' + word + '] Download complete ' + str(x) + 'files !')
