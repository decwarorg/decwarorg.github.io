import PIL
from PIL import Image
import os
import glob

images = glob.glob('*.jpg')

def resize():
    for image in images:
        image_name = image.split('.', 1)[0]
        fixed_height = 1000
        image = Image.open(image)
        height_percent = (fixed_height / float(image.size[1]))
        width_size = int( float(image.size[0]) * float(height_percent) )
        image = image.resize((width_size, fixed_height), PIL.Image.NEAREST)
        image.save(image_name+ '.webp', 'webp', optimize=True, quality=90)

resize()
