import cv2
import json
import time
import json
import math
import psutil
import platform
import random
import logging
import sys
import os as ops
from collections import deque


def main():
 
  fileSize = ops.path.getsize('img.png')

  imgArray = deque()

  
  start = time.time()
  numFiles = 0
  imagePath = "img.png"
  while numFiles<10:
    
    img = cv2.imread(imagePath)
    imgArray.append(img)
    numFiles += 1
  
  #print(sys.getsizeof(imgArray[0]))
  readTime=time.time()-start
  readSpeed=(1/readTime)*((numFiles*fileSize)/1000000)

  imgArray2 = deque()

  start = time.time()
  for i in range(numFiles):
    imgArray2.append(imgArray.pop())

  
  memTime=time.time()-start
  fileSize = sys.getsizeof(imgArray2[0])
  memSpeed=(1/memTime)*((numFiles*fileSize)/1000000)


  

  loop = 1
  start = time.time()
  for i in range(numFiles):
    name = "/tmp/img{}.png".format(loop)
    cv2.imwrite(name, imgArray2[-1])
    imgArray2.pop()
    loop+=1

  
  writeTime=time.time()-start
  fileSize = ops.path.getsize('/tmp/img1.png')
  writeSpeed=(1/writeTime)*((numFiles*fileSize)/1000000)

  print(readTime)
  print(readSpeed)
  print(memTime)
  print(memSpeed)
  print(writeTime)
  print(writeSpeed)

main()