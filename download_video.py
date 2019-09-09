#!/usr/bin/env python3.6

import os.path
import glob
import youtube_dl
import re
from ultrastartxt import set_attr


youtube_id = re.compile('[A-Za-z0-9_-]+$')


def songs():
    for file in glob.glob("files/*.txt"):
        ytfile = file + '_youtube'
        if os.path.exists(ytfile):
            yield os.path.basename(file), open(file).read().splitlines(), open(ytfile).read().splitlines()


def main():
    for file, content, youtubelinks in songs():
        print(file)
        songname = os.path.splitext(file)[0]
        dir = 'videos/' + songname

        if os.path.exists(dir):
            continue

        for ytlink in youtubelinks:
            try:
                videofile = None

                def progress(kwargs):
                    nonlocal videofile
                    if 'filename' in kwargs:
                        videofile = kwargs['filename']

                with youtube_dl.YoutubeDL({'format': 'best', 'progress_hooks': [progress]}) as ydl:
                    ydl.download([ytlink])

                break
            except Exception as ex:
                print('download failed: ' + str(ex))

        if not videofile:
            continue

        os.mkdir(dir)
        with open(dir + '/' + file, 'w') as f:
            content = set_attr(content, videofile, 'VIDEO')
            content = set_attr(content, videofile, 'MP3')
            f.writelines(content)
        os.rename(videofile, dir + '/' + videofile)


if __name__ == '__main__':
    main()
