# Dataset Generator

This is the dataset generator for the poles neural network in SJSU 
Robotics intelligent systems.

## Overview
In order to train our neural network, we need to have lots of data.
Using this data, we will train our neural network and modify it so that
it can recognize poles more accurately. Our goal is to generate at least 
50 thousand images. Our initial thought was to manually label web scraped
images. However, manually labeling these images would take too long, and 
the work is tedious. Thus, we have made a dataset generator. 

## How this works
To create a fake dataset, we need a background and an image of a pole. 
The picture of the pole is pasted randomly onto the background, in a 
reasonable position, towards the bottom of the image. We will track the
position of the pole and return it in an xml file.

There are 3 main parts of this script: image generation, xml generation, 
and dataset generation. From `dataset_gen`, we call `img_gen` to proccess
images, which in turn calls `xml_generate` to create the xml file.

### Dataset Generation: `dataset_gen.py`
Here, we pass in parameters: `PATH`, `posStart`, `posMod`, `scaleFactor`. 

Here is a brief explanation of the parameters
<pre>
PATH: str()             Path of current directory
posStart: (int, int)    Initial top left corner of pole
posMod: (int, int)      (height, width) modification after each generation
scaleFactor: (int, int) Minimum and maximum pole scale down factors
</pre>

### Image Generation: `img_gen.py`
This is where the pole is pasted onto the background. 

Here is a brief explanation of the parameters
<pre>
pole: str()             Name of pole
background: str()       Name of background
PATH: str()             Path of current directory
saveName: str()         Name of to be saved file
pos: (int, int)         Position of top left corner of pole
scaleFactor: int()      Scaling down pole factor
subfolder: str()        Name of subfolder (ex: 'b1p2)
</pre>

### XML Generation:: `xml_generate.py`


## Old code / related repositories
1. [Batch partition script](https://github.com/jerrylee17/batch-partition-script)

