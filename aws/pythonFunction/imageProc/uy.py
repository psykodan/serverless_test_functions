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
import ctypes
import numpy

def main():
  vals = [ctypes.c_byte(0) for x in range(100000)]
  #vals2 = [ctypes.c_byte(1) for x in range(100000)]
  #ByteArray = ctypes.c_byte()# * len(vals)
  #print(fileSize)
  vals2 = []

  start = time.time()
  for x in range(len(vals)-1, -1, -1):
    #print(hex(ctypes.addressof(vals[x])))

    #print(vals[x])
    #print(hex(ctypes.addressof(p[x].contents)))
    #print(vals[x])
    #vals2.append(p[x])
    #print(vals2[x])
    #ctypes.memmove(ctypes.addressof(vals2[x]),ctypes.addressof(vals[x]),sys.getsizeof(vals[x]))
    vals2.append(vals.pop())
    #input(x)
    #vals2 = ByteArray(*vals)
    #print(hex(ctypes.addressof(vals2[x])))
    #print(vals2[x])
    #print(sys.getsizeof(vals[x]))
  #vals = [ctypes.c_float(0) for x in range(367647)]
  memTime = time.time()-start
  fileSize = 136#sys.getsizeof(vals[0])
  numFiles = 100000#len(vals)
  memSpeed = (1/memTime)*((numFiles*fileSize)/1000000)


  print(memTime)
  print(memSpeed)
  #print(vals)
  #print(vals2)

 
  # fileSize = ops.path.getsize('img.png')

  # imgArray = deque()

  # c_float_p = ctypes.POINTER(ctypes.c_float)
  # start = time.time()
  # numFiles = 0
  # imagePath = "img.png"
  # while numFiles<10:
    
  #   img = cv2.imread(imagePath)
  #   imgArray.append(numpy.ctypeslib.as_ctypes(img))
  #   #imgArray.append(img)
  #   numFiles += 1
  
  # #print(sys.getsizeof(imgArray[0]))
  # readTime=time.time()-start
  # readSpeed=(1/readTime)*((numFiles*fileSize)/1000000)





  # #print(imgArray[0])
  # #pi = ctypes.pointer(numpy.ctypeslib.as_ctypes(imgArray[0]))
  # c_imgArray = (((ctypes.c_ubyte * 3) * 1050) * 1050)(*imgArray)
  # #print(pi.contents)
  # #temp = []
  # #temp.append(pi)
  # #print(temp[0])
  # for x in range(numFiles):
  #   print(ctypes.addressof(c_imgArray[x]))
  # print("------------------------------------")

  # imgArray2 = deque()

  # start = time.time()
  # for i in range(numFiles):
  #   imgArray2.append(imgArray.pop())

  
  # memTime=time.time()-start
  # fileSize = sys.getsizeof(imgArray2[0])
  # memSpeed=(1/memTime)*((numFiles*fileSize)/1000000)

  # print(imgArray2[0])
  # for x in range(numFiles):
  #     print(ctypes.addressof(imgArray2[x]))
  

  # loop = 1
  # start = time.time()
  # for i in range(numFiles):
  #   name = "/tmp/img{}.png".format(loop)
  #   cv2.imwrite(name, imgArray2[-1])
  #   imgArray2.pop()
  #   loop+=1

  
  # writeTime=time.time()-start
  # fileSize = ops.path.getsize('/tmp/img1.png')
  # writeSpeed=(1/writeTime)*((numFiles*fileSize)/1000000)

  # print(readTime)
  # print(readSpeed)
  # print(memTime)
  # print(memSpeed)
  # print(writeTime)
  # print(writeSpeed)

main()