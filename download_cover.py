#!/usr/bin/env python3.6

import glob
import requests
import os
from ultrastartxt import set_attr


def songs():
    for file in glob.glob("videos/*"):
        yield file


def get_cover(name):
    print(name)
    r = requests.get('https://genius.com/api/search/multi', params={
        'per_page': '1',
        'q': name,
    })
    return r.json()['response']['sections'][0]['hits'][0]['result']['song_art_image_url']


def main():
    for song in songs():
        print(song)
        try:
            cover_url = get_cover(os.path.basename(song))
        except:
            continue
        if 'default_cover_image' in cover_url:
            continue
        print(cover_url)
        coverfile = 'cover' + os.path.splitext(cover_url)[1].partition('?')[0]
        coverpath = song + '/' + coverfile

        with open(coverpath, 'wb') as f:
            f.write(requests.get(cover_url).content)

        txtfile = song + '/' + os.path.basename(song) + '.txt'
        content = open(txtfile).read().splitlines()
        with open(txtfile, 'w') as f:
            f.writelines(set_attr(content, coverfile, 'COVER'))


if __name__ == '__main__':
    main()
