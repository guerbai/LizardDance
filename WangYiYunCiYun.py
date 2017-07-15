# -*- coding: utf-8 -*-
import sys
import re
import requests

cookies = dict(appver='2.0.2')
headers = dict(referer="http://music.163.com")
global failtime
failtime = 0
global total_song_nums
total_song_nums = 0


def get_singerid_from_singer(singer):
    url = 'http://music.163.com/api/search/get/'
    data = {
        's': singer,
        'type': 100,
        'limit': 20,
        'offset': 0,
    }
    r = requests.post(url, headers=headers, cookies=cookies, data=data)
    data = r.json()['result']['artists'][0]
    return {
        'singerid': data['id'],
        'album_nums': data['albumSize']
    }


def get_albumlist_from_singerid(singer_data):
    url = 'http://music.163.com/api/artist/albums/{0}?offset=0&limit={1}'.format(
        singer_data['singerid'], singer_data['album_nums'])
    r = requests.get(url, headers=headers, cookies=cookies)
    album_nums = r.json()
    return [{'albumid': i['id'], 'song_nums': i['size']} for i in r.json()['hotAlbums']]


def get_songid_from_albumid(albumid):
    url = 'http://music.163.com/api/album/{}/'.format(albumid)
    r = requests.get(url, headers=headers, cookies=cookies)
    return [i['id'] for i in r.json()['album']['songs']]



def get_lyric_from_songid(songid):
    url = 'http://music.163.com/api/song/lyric?os=pc&id={}&lv=-1&kv=-1&tv=-1'.format(songid)
    r = requests.get(url, headers=headers, cookies=cookies)
    global failtime
    global total_song_nums
    total_song_nums += 1
    try:
        text = r.json()['lrc']['lyric'].encode('utf-8')
        textlist = text.split('\n')
        text = '\n'.join([re.sub(r'\[.*?\]', '', i) for i in textlist])
        return text
    except KeyError:
        failtime += 1
        return ''


def main(singer):
    lyrics = []
    singer_data = get_singerid_from_singer(singer)
    albumlist = get_albumlist_from_singerid(singer_data)
    with open(singer+'lyric.txt', 'w') as lyricfile:
        for albumid in albumlist:
            songids = get_songid_from_albumid(albumid['albumid'])
            for songid in songids:
                lyric = get_lyric_from_songid(songid)
                lyricfile.write(lyric)
                print "write once."
    print "total ", total_song_nums, 'songs.'
    print "fail ", failtime, 'times.'
    print "done"

def generate_ciyun_pic():
    import matplotlib.pyplot as plt
    from wordcloud import WordCloud
    import jieba
    from cv2 import imread

    text_from_file_with_apath = open('./{}lyric.txt'.format(singer), 'r').read().replace('作词', '').replace('作曲', '')

    wordlist_after_jieba = jieba.cut(text_from_file_with_apath, cut_all = True)
    wl_space_split = " ".join(wordlist_after_jieba)

    mask_img = imread('./mask.jpg')# , flatten=True)
    my_wordcloud = WordCloud(
            font_path='msyh.ttc',
            background_color='white',
            mask=mask_img
            ).generate(wl_space_split)

    plt.imshow(my_wordcloud)
    plt.axis("off")
    plt.show()

if __name__ == '__main__':
    singer = sys.argv[1]
    main(singer)
    # generate_ciyun_pic()
