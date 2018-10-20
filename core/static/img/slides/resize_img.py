#coding: utf-8
import PIL, sys
from PIL import Image

basewidth = int(sys.argv[2])

hsize = int(sys.argv[3])
name_of_file = sys.argv[1]

img = Image.open(name_of_file)
#wpercent = (basewidth / float(img.size[0]))
#hsize = int((float(img.size[1]) * float(wpercent)))
img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
img.save("new_" + name_of_file)
