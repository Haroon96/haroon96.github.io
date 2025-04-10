import json
from glob import glob

def generate_content_ids():
    json_files = glob('src/data/*.json')
    for json_file in json_files:
        with open(json_file) as f:
            js = json.load(f)
        idx = len(js)
        for entry in js:
            entry['id'] = idx
            idx -= 1
        with open(json_file, 'w') as f:
            json.dump(js, f, indent=2)

if __name__ == '__main__':
    generate_content_ids()