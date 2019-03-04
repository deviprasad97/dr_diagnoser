from PIL import Image
import os
import glob
image_list = []
for filename in glob.glob('./*.ppm'): #assuming gif
        im=Image.open(filename)
        im.save(filename[:len(filename)-3] + "jpg")
