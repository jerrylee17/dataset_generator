import numpy as np
from PIL import Image
import os
from pathlib import Path

# Generates 1 image based on input of 2 images
def img_gen(image1, image2, dirname):
    # Pull image from location
    try:
        im1 = Image.open(dirname+'/pole/'+image1)
        im2 = Image.open(dirname+'/background/'+image2)
    except:
        print('No image')
        return 'No image'
    
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
    scale_down = (im1.width//3, im1.height//3)
    im1 = im1.resize(scale_down)
    im2.paste(im1, (300, 300), im1)
    
    # Determine new path
    NEW_PATH = dirname + '/generated-images/'
    
    # Call Habib's xml file to save xml
    create_xml(NEW_PATH, image1, im2.size, ('pole', dim))
    
    # Save image
    im2.save(NEW_PATH+image1, 'PNG')


dirname = os.path.abspath(__file__)
dirname = '/'.join((dirname.split('/')[:-1]))
img_gen('woodPost1.png', 'background1.png', dirname)
