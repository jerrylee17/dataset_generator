import numpy as np
from PIL import Image, ImageDraw
import os
from pathlib import Path
from xml_generate import create_xml

# Generates 1 image based on input of 2 images
'''
Inputs:
    pole: str()         Name of pole
    background: str()   Name of background
    PATH: str()         Path of current directory
    saveName: str()     Name of to be saved file
    pos: (int, int)     Position of top left corner of pole
    scaleFactor: int()  Scaling down pole factor
    subfolder: str()    Name of subfolder   ex: 'b1p2
'''
def img_gen(pole, background, PATH, saveName, \
    pos=(300, 300), scaleFactor=3, subfolder=''):
    
    saveName = saveName.split('.')[0]+'.png'
    # Pull image from location
    try:
        im1 = Image.open(PATH+'/pole/'+pole)
        im2 = Image.open(PATH+'/background/'+background)
    except:
        print('NO IMAGE')
        return 'NO_IMG'
    
    # Convert image to numpy array grayscale
    # Prepare for cropping
    data = np.array(im1)
    data = np.mean(data, axis=2)

    # Find where to crop
    topr, topc, botr, botc = 0,0,im1.width, im1.height
    cols = np.mean(data, axis=1)
    rows = np.mean(data, axis=0)
    for c in cols:
        if c != 0: break
        topc += 1
    for c in cols[::-1]:
        if c != 0: break
        botc -= 1 
    for r in rows:
        if r != 0: break
        topr += 1
    for r in rows[::-1]:
        if r != 0: break
        botr -= 1
    dim = topc, botc, topr, botr
    im1 = im1.crop((topr, topc, botr, botc))
    
    # Scale down pole image
    scale_down = (im1.width//scaleFactor, im1.height//scaleFactor)
    im1 = im1.resize(scale_down)
    
    if (pos[0] < 0 or pos[0] + im1.width > im2.width): 
        return 'WIDTH_ERR'
    if (pos[1] < 0 or pos[1] + im1.height > im2.height): 
        return 'HEIGHT_ERR'
    # Paste image 1 on image 2
    im2.paste(im1, pos, im1)

    # Determine new path
    NEW_PATH = PATH + '/generated-images/' + subfolder + '/'
    
    # Call Habib's xml file to save xml
    finalPos = (pos[0], pos[1], pos[0] + im1.width, pos[1]+im1.height)
    create_xml(NEW_PATH, saveName, im2.size, ('pole', finalPos), subfolder)
    
    # # Test the rectangle
    # draw = ImageDraw.Draw(im2)
    # draw.rectangle((finalPos), outline=245)
    # del draw
    # im2.show()
    
    # Save image
    im2.save(NEW_PATH+saveName, 'PNG')
    
    print('Saved: ', NEW_PATH+saveName)
    return('SAVED')


# PATH = os.path.abspath(__file__)
# PATH = '/'.join((PATH.split('/')[:-1]))
# img_gen('woodPost1.png', 'background1.png', PATH, \
#     'testing', pos=(300, 300), scaleFactor=7)
