from PIL import Image
import os
import glob
image_list = []
for filename in glob.glob('./*.jpg'): #assuming gif
    image_list.append(filename[2:])
print("image_list", image_list)
csv = open('labels.csv')
new = open('final_labels.csv', 'w')
for line in csv:
    if line.split(',')[0] in image_list:
        new.write(line)

