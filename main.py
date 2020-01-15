import pytesseract
import io 
import requests
from PIL import Image, ImageEnhance 
import PIL.ImageOps

img = Image.open('akio.gif')
if type(img) == PIL.GifImagePlugin.GifImageFile:
    ittr =  img.n_frames
else:
    ittr = 1
for frame in range(ittr):

    print('Frame: ', frame + 1)

    img.seek(frame)
    imgrgb = img.convert('RGB')

    imgrgb = PIL.ImageOps.invert(imgrgb)

    enchancer = ImageEnhance.Brightness(imgrgb)

    imgrgb = enchancer.enhance(4.0)

    imgrgb = imgrgb.convert('1')

    text = pytesseract.image_to_string(imgrgb)

    print(text)
    print("------------------")