from math import sqrt
from builtins import range
import cv2
import numpy as np
import insightface
from insightface.app import FaceAnalysis
# from insightface.data import get_image as ins_get_image
import os 
import logging
  
#Create and configure logger
logging.basicConfig(filename="distFile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
  
#Creating an object
logger=logging.getLogger()
  
#Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)


app = FaceAnalysis()
app.prepare(ctx_id=0, det_size=(640, 640))
count = 0


def check(img_one, img_two):
    one = cv2.imread(img_one)
    print(one)
    two = cv2.imread(img_two)
    print(two)
    logger.info(f"converted two images into numpy array")
    faces1 = app.get(one)
    faces2 = app.get(two)
    # logger.info(f"detected faces - file path img1 {img_one}, img2 {img_two}")
    # rimg = app.draw_on(one, faces1)
    # rimg2 = app.draw_on(two, faces2)
    
    im1 = faces1[0]
    im2 = faces2[0]
    print(faces2)
    dist = euclidean_distance(im1['embedding'], im2['embedding'])
    logger.info(f'dist: {dist} - image1 : {img_one} - image2 : {img_two}')
    # for i in faces1:
    #     for j in faces2:
    #         print(dist)

def euclidean_distance(a, b):
    return sqrt(sum((e1-e2)**2 for e1, e2 in zip(a,b)))
        
fols = "forTest"
fol_list = os.listdir(fols)
# fol_list.sort()
for folder in fol_list:
     sub_dir = os.listdir(f'{fols}/{folder}')
     t = len(sub_dir) 
     if t > 1:
            _one = f'{fols}/{folder}/{sub_dir[0]}'
            _two = f'{fols}/{folder}/{sub_dir[1]}'
            try:    
                 check(_one, _two)
            except Exception as e:
                logger.debug(f'Failed: {e}')
                count = count + 1 
 