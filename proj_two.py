import os
import cv2
import numpy as np
# import insightface
from insightface.app import FaceAnalysis
# from insightface.data import get_image as ins_get_image
import logging
from math import sqrt
import time
logging.basicConfig(filename="distOP.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')


#Creating an object
logger=logging.getLogger()
  
#Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)

app = FaceAnalysis()
app.prepare(ctx_id=0, det_size=(640, 640))
count = 0
total_time = None

#function for checking imgs
count = count + 1
def check(img_one,img_two):
    one = cv2.imread(img_one)
    two = cv2.imread(img_two)
    faces1 = app.get(one)
    faces2 = app.get(two)
    im0 = faces1[0]
    im1 = faces2[0]
    # print(faces2)
    dist = euclidean_distance(im0['embedding'], im1['embedding'])
    print(f'{count} of {len(fol_list)} , dist: {dist}')
    #logger
    logger.info(f'dist: {dist}- image1 : {img_one} - image2 : {img_two} - time taken : {total_time}')
    
def euclidean_distance(a, b):
    return sqrt(sum((e1-e2)**2 for e1, e2 in zip(a,b)))   

# Taking paths of images
fols = "forTest"
fol_list = os.listdir(fols)
for folder in fol_list:
     sub_dir = os.listdir(f'{fols}/{folder}')
     t = len(sub_dir) 
     if t > 1:
            _one = f'{fols}/{folder}/{sub_dir[0]}'
            _two = f'{fols}/{folder}/{sub_dir[1]}'
            try:  
                start = time.time()  
                op = check(_one, _two)
                end = time.time()
                total_time = end-start
                # logger.info(f' image1 : {img_one} - image2 : {img_two}')
            except Exception as e:
                logger.debug(f'Failed: {e} - image1 : {_one} - image2 : {_two}')
            count = count + 1 
                
                
 