from builtins import range
import cv2
import numpy as np
import insightface
from insightface.app import FaceAnalysis
# from insightface.data import get_image as ins_get_image
import os 
import logging  
from math import sqrt
#Create and configure logger
logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
  
#Creating an object
logger=logging.getLogger()
  
#Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)


app = FaceAnalysis()
app.prepare(ctx_id=0, det_size=(640, 640))
# count = 0
u = None
img ='/home/syntizen/Pictures/talha.png'
img1 = '/home/syntizen/Pictures/VK.jpg'
def check(img_one,img_two):
    one = cv2.imread(img_one)
    two = cv2.imread(img_two)
    logger.info(f"converted two images into numpy array")
    faces1 = app.get(one)
    faces2 = app.get(two)
    img= faces1[0]
    img1 = faces2[0]
    global u
    u = "hello"
    dist = euclidean_distance(img['embedding'], img1['embedding'])
    logger.info(f'dist: {dist}')
    print(dist)
    
    # print(faces1[0]['embedding'])
    # print(faces2[0]['embedding'])
#     # print(faces1)
def euclidean_distance(a, b):
    return sqrt(sum((e1-e2)**2 for e1, e2 in zip(a,b)))
    
check(img,img1)

