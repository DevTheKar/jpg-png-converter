import sys
import os
from PIL import Image

#grab first argument (folder) where all jpg images are
image_folder = sys.argv[1]
output_folder = sys.argv[2]

#check if output folder exists, if not create
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

#loop through initial folder  for images
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{output_folder}{clean_name}.png', 'png')

    print('all done!')

#convert images to png

#save to the output folder