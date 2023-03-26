# py jpec_to_png_conveter.py Pokedex png
import sys
import os
import shutil
from PIL import Image

# get first and second arguments
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# delete old folder
if os.path.exists(output_folder):
    shutil.rmtree(output_folder)
# create new folder
os.makedirs(output_folder)

for file in os.listdir(image_folder):
    img = Image.open(os.path.join(image_folder, file))
    filename = os.path.splitext(file)[0] + ".png"
    img.save(os.path.join(output_folder, filename))
    print("all done!")
