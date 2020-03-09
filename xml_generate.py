from xml.etree.ElementTree import Element, SubElement, tostring, ElementTree
import sys
import os

# function takes in basic arguments from a data generator, and then outputs them
# as an xml file in a specific subdirectory
'''
Inputs:
    PATH: str()         Path of current directory
    file: str()         Name of output file
    size: (int, int)    Contains width and height of the pole in image
    object: (string, [int, int, int, int])     
                        Contains name of pole and it's four corners
    subfolder: str()    Name of subfolder   ex: 'b1p2
'''

def create_xml(PATH, file, size, object, subfolder=''):

    annotation = Element('annotation')

    # creating the <folder> tag
    path_name = SubElement(annotation, 'folder')
    path_name.text = PATH

    # add tag containing file name
    file_name = SubElement(annotation, 'file_name')
    file_name.text = file

    # nested tags for the width/height of the object passed
    size_of_object = SubElement(annotation, 'size')
    size_width = SubElement(size_of_object, 'width')
    size_width.text = str(size[0])

    size_height = SubElement(size_of_object, 'height')
    size_height.text = str(size[1])

    size_depth = SubElement(size_of_object, 'depth')
    size_depth.text = "3"

    # nested tags to deconstruct the tuple passed through
    object_element = SubElement(annotation, 'object')

    object_name = SubElement(object_element, 'name')
    object_name.text = object[0]

    # hardcode in pose, truncate and difficult to fit specifications
    object_pose = SubElement(object_element, 'pose')
    object_pose.text = "Unspecified"

    object_truncate = SubElement(object_element, 'truncated')
    object_truncate.text = "0"

    object_difficult = SubElement(object_element, 'difficult')
    object_difficult.text = "0"

    # box tag containing all the x/y min and max vals
    object_box = SubElement(object_element, 'box')

    object_xmin = SubElement(object_box, 'xmin')
    object_xmin.text = str(object[1][0])

    object_ymin = SubElement(object_box, 'ymin')
    object_ymin.text = str(object[1][1])

    object_xmax = SubElement(object_box, 'xmax')
    object_xmax.text = str(object[1][2])

    object_ymax = SubElement(object_box, 'ymax')
    object_ymax.text = str(object[1][3])

    # write the entire thing to a file as an xml file
    tree = ElementTree(annotation)
    path_name = 'xml_files/' + subfolder + '/'
    file = file.split('.')[0]
    DIRECTORY = os.path.join(path_name, file + '.xml')
    try:
        tree.write(open(DIRECTORY, 'wb'))
    except:
        os.mkdir(path_name)
        DIRECTORY = os.path.join(path_name, file + '.xml')
        tree.write(open(DIRECTORY, 'wb'))

# create_xml("desert-pole", "habib", (256, 256), ('habib', (15, 15, 40, 40)))


'''
UNCOMMENT THESE AND ADD A print(prettify(annotation)) AT THE END
 OF THE FUCNTION IF YOU WANT TO SEE HOW THE XML SHOULD ACTUALLY LOOK LIKE
 OR JUST USE A PARSER IN VSCODE TO FORMAT IT
'''
# from xml.etree import ElementTree as ET
# from xml.dom import minidom
# def prettify(elem):
#     """Return a pretty-printed XML string for the Element.
#     """
#     rough_string = ET.tostring(elem, 'utf-8')
#     reparsed = minidom.parseString(rough_string)
#     return reparsed.toprettyxml(indent="  ")

# How XML should look like at the end
'''
Folder
Size
Object
  name
  box
    xmin
    ymin
    xmax
    ymax
'''
