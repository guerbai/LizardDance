# -*- coding: utf-8 -*-
from pprint import pprint
import requests

cookies = dict(appver='2.0.2')
headers = dict(referer="http://music.163.com")


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
	print r.json()['lrc']['lyric']
	pass


def main(singer):
	lyrics = []
	singer_data = get_singerid_from_singer(singer)
	albumlist = get_albumlist_from_singerid(singer_data)
	for albumid in albumlist:
		songids = get_songid_from_albumid(albumid['albumid'])
		for songid in songids:
			lyric = get_lyric_from_songid(songid)
			print lyric
			break
		break


if __name__ == '__main__':
	main('snh48')
