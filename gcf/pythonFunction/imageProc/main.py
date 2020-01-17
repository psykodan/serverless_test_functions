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

from flask import jsonify

def imageProc():
	logging.getLogger().setLevel(logging.INFO)


	imgArray = []
	scale_percent=100


	f = open("/proc/cpuinfo")
	lines = f.readlines()
	f.close()
	model = []
	speed = []
	for l in lines:
		if (l.find('model name') != -1):
			sp = l.split(":")
			model.append(sp[1][1:-1])
			
		if (l.find('cpu MHz') != -1):
			sp = l.split(":")
			speed.append(int(float(sp[1][1:-1])))
			
	
	times=psutil.cpu_times(percpu=True)
	os = platform.release()

#Read time test
	

	#memSize = int(context.memory_limit_in_mb)
	#initMemPerc = psutil.virtual_memory().percent
	#initMem = memSize * (initMemPerc/100)
	#safeMem = (memSize-initMem) *1000000
	
	imgArray = deque()
	numFiles = 0
	imagePath = "img.png"

	start = time.time()

	while numFiles<10:
		img = cv2.imread(imagePath)
		imgArray.append(img)
		numFiles += 1

	
	readTime=time.time()-start
	fileSize = ops.path.getsize('img.png')
	readSpeed=(1/readTime)*((numFiles*fileSize)/1000000)



#Memory Bandwidth test

	imgArray2 = deque()

	start = time.time()
	for i in range(numFiles):
		imgArray2.append(imgArray.pop())


	memTime=time.time()-start
	fileSize = sys.getsizeof(imgArray2[0])
	memSpeed=(1/memTime)*((numFiles*fileSize)/1000000)



#Write time test

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




	stop = int(time.time()*1000)
	uptime = int((stop/1000)-psutil.boot_time())
	load = psutil.getloadavg()
	head=""
	temp=""
	for i in range(7):
		temp = str(hex(math.floor(random.random() *255 )))
		head += (temp.split("x"))[1]
		
	ID = head + str(stop)
	logging.info(ID)
	count = len(imgArray)

	response = {
	"id":	ID,
	"readTime" : readTime,
	"readSpeed" : readSpeed,
	"memTime" : memTime,
	"memSpeed" : memSpeed,
	"writeTime": writeTime,
	"writeSpeed" : writeSpeed,
	"numFiles" : numFiles,
	"time"	:	stop,
	"uptime" : uptime,
	"model1" : model[0],
	"speed1" : speed[0],
	"user1" : times[0].user*1000,
	"sys1" : times[0].system*1000,
	"idle1" : times[0].idle*1000,
	"model2" : model[1],
	"speed2" : speed[1],
	"user2" : times[1].user*1000,
	"sys2" : times[1].system*1000,
	"idle2" : times[1].idle*1000,
	"os" : os,
	"load1" : load[0],
	"load5" : load[1],
	"load15" : load[2]


	}
	
	return response
		

def main(request):
    # TODO implement
    response = imageProc()
    
    return jsonify(response)
#