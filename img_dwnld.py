from fastai.vision import (
    download_images
)

from pathlib import Path

path = Path('./data/')
classes = ['inca','maya','aztec', 'toltec', 'olmec', 'nasca']

for folder in classes:
    dest = path/folder
    print(dest)
    dest.mkdir(parents=True, exist_ok=True)
    download_images(path/"{}.csv".format(folder), dest, max_pics=700)