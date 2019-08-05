#!/usr/bin/env python3.6

import requests
import hashlib
import bs4
import os
import re


def url_editsongs(id):
    return f'http://usdb.animux.de/index.php?link=editsongs&id={id}'


def url_detail(id):
    return f'http://usdb.animux.de/index.php?link=detail&id={id}'


def login(s):
    s.post(
        'http://usdb.animux.de/index.php?&link=home',
        data={
            'user': 'maijaecueth9vohZi9vecohwaghaht',
            'pass': 'ohleta4AeY4Ooy2eileiz1ja9alae7',
            'login': 'Login',
            'remember': '1',
        }
    )


def write_text(path, content):
    with open(path, 'w') as f:
        f.write(content)

def get(s, url):
    cache_key = hashlib.sha224(url.encode()).hexdigest()
    cache_file = f'cache/{cache_key}'

    if os.path.exists(cache_file):
        return open(cache_file).read()

    content = s.get(url).content

    with open(cache_file, 'wb') as f:
        f.write(content)

    return content

youtube_link = re.compile('https?://www.youtube.com/v/[A-Za-z0-9_-]+')

def main():
    s = requests.Session()

    login(s)

    for id in open('animux_ids.txt').readlines():
        content = get(s, url_editsongs(id))
        soup = bs4.BeautifulSoup(content, features='lxml')
        content = soup.select('textarea')[0].get_text()
        filename = soup.select('input[name="filename"]')[0]['value']
        print(filename)

        filename = filename.replace('/', '_')

        write_text(f'files/{filename}', content)

        content = get(s, url_detail(id))
        if not isinstance(content, str):
            content = content.decode()
        youtube_links = youtube_link.findall(content)

        if youtube_links:
            write_text(f'files/{filename}_youtube', '\n'.join(set(youtube_links)) + '\n')


if __name__ == '__main__':
    main()
