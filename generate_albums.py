from PIL import Image
import os
import json

PHOTOS_DIR = os.path.join('src', 'misc', 'photos')

def build_content_json():

    # read content.json
    with open('content.json') as f:
        content = json.load(f)
    content['photos'] = []

    for photo in sorted(os.listdir(PHOTOS_DIR), reverse=True):

        # check if already in list or a thumbnail
        if '-thumb' in photo:
            continue

        # get filename
        root, ext = os.path.splitext(photo)
        
        # append to photo list
        content['photos'].append({ 'thumbnail': f'{root}-thumb{ext}', 'photo': photo })

    # rewrite content.json
    with open('content.json', 'w') as f:
        json.dump(content, f, indent=4)
        

def generate_thumbnails():

    for photo in os.listdir(PHOTOS_DIR):

        if '-thumb' in photo:
            continue

        root, ext = os.path.splitext(photo)

        photo_path = os.path.join(PHOTOS_DIR, photo)
        thumb_path = os.path.join(PHOTOS_DIR, f'{root}-thumb{ext}')

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
    build_content_json()
    generate_thumbnails()


if __name__ == '__main__':
    main()