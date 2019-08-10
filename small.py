from PIL import Image
import sys
import numpy as np

img_name = sys.argv[1]
mult = int(sys.argv[2])

im = Image.open(img_name)
pix = im.load()

channels = len(im.getbands())
h,w = im.size
hs,ws = [int(x/mult) for x in (h,w)]
pnew = np.zeros((hs, ws, channels), dtype=np.uint8)

im2 = Image.new('RGB', (hs, ws))
for i in range(hs):
        for j in range(ws):
                sum = pix[i*mult,j*mult]
                for r in range(1,mult):
                        sum = [x + y for x, y in zip(sum, pix[i*mult+r,j*mult+r])]
                sum = tuple([x/mult for x in sum])
                pnew[i,j] = sum

                
data = list(tuple(pixel) for pixel in pnew)
im2 = Image.fromarray(np.asarray(data))
im2 = im2.rotate(270, expand=True).transpose(Image.FLIP_LEFT_RIGHT)
im2.save(img_name.split('.')[0] + "_small_"+str(mult)+"." + img_name.split('.')[1])
