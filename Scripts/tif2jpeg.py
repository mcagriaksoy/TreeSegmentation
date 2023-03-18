# rgba to rgb converter for geoloc - mcagriaksoy

import os
#import cv2
from PIL import Image

def main():
    yourpath = os.path.join(os.getcwd(), "aerial_60m_alnus_spec")
    for root, dirs, files in os.walk(yourpath, topdown=False):
        for name in files:
            print(os.path.join(root, name))
            if os.path.splitext(os.path.join(root, name))[1].lower() == ".tif":
                if os.path.isfile(os.path.splitext(os.path.join(root, name))[0] + ".jpg"):
                    print("A jpeg file already exists for %s" % name)
                else:
                    outfile = os.path.splitext(os.path.join(root, name))[0] + ".jpg"
                    try:
                        rgba_image = Image.open(os.path.join(root, name))
                        im = rgba_image.convert("RGB")
                        #im = cv2.cvtColor(im, cv2.COLOR_RGB2BGR)
                        print("Generating jpeg for %s" % name)
                        im.thumbnail(im.size)
                        im.save(outfile, "JPEG", quality=100)
                    except Exception as e:
                        print(e)

if __name__ == '__main__':
    main()