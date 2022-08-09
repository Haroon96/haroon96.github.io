from PIL import Image
from random import choice
import os
import json
from natsort import natsorted

ALBUMS_DIR = os.path.join('src', 'misc', 'albums')

def build_content_json():

    with open('content.json') as f:
        content = json.load(f)

    for ind, album in enumerate(content['albums']):
        
        dir_name = album['name'].replace(' ', '-').lower()
        content['albums'][ind]['dir'] = dir_name
        photos = natsorted(os.listdir(os.path.join(ALBUMS_DIR, dir_name)))
        content['albums'][ind]['photos'] = []
        for photo in photos:

            if '-thumb' in photo:
                continue

            root, ext = os.path.splitext(photo)
            content['albums'][ind]['photos'].append({ 'thumbnail': f'{root}-thumb{ext}', 'photo': photo })

    with open('content.json', 'w') as f:
        json.dump(content, f, indent=4)
        

def generate_thumbnails():
    for album in os.listdir(ALBUMS_DIR):
        album_dir = os.path.join(ALBUMS_DIR, album)

        for photo in os.listdir(album_dir):

            if '-thumb' in photo:
                continue

            root, ext = os.path.splitext(photo)

            photo_path = os.path.join(album_dir, photo)
            thumb_path = os.path.join(album_dir, f'{root}-thumb{ext}')

            if os.path.exists(thumb_path):
                continue

            # write thumbnail
            img = Image.open(photo_path)
            
            # crop to square ratio
            if img.width > img.height:
                margin = (img.width - img.height) // 2
                print((margin, 0, margin, img.height))
                img = img.crop((margin, 0, margin + img.height, img.height))
            else:
                margin = (img.height - img.width) // 2
                print((0, margin, img.width, margin))
                img = img.crop((0, margin, img.width, margin + img.width))
            
            img.thumbnail((128, 128))
            img.save(thumb_path)

def main():
    build_content_json();
    generate_thumbnails()


if __name__ == '__main__':
    main()