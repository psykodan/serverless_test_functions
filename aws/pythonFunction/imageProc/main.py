import cv2
import json
import time
import json
import math
import psutil
import platform
import random
import logging

def main():
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


	start = time.time()
	#print(start)
	while True:

		if time.time()-start > 1:

			imagePath = "face.jpg"
			cascPath = "faces.xml"
			# Read the image
			img = cv2.imread(imagePath)
			gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

			# Create the haar cascade
			faceCascade = cv2.CascadeClassifier(cascPath)

			# Detect faces in the image
			faces = faceCascade.detectMultiScale(
			    gray,
			    scaleFactor=1.1,
			    minNeighbors=5,
			    minSize=(30, 30)
			    #flags = cv2.CV_HAAR_SCALE_IMAGE
			)
			numFaces = len(faces)
			#print(numFaces)

			stop = int(time.time()*1000)
			uptime = int((stop/1000)-psutil.boot_time())
			#runtime = stop - start
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
			"count" : count,
			"faces" : numFaces,
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
			"uptime" : uptime,
			"time"	:	stop,
			"load1" : load[0],
			"load5" : load[1],
			"load15" : load[2]


			}
			
			return response

		else:
			# Get user supplied values
			imagePath = "img.jpg"

			# Read the image
			img = cv2.imread(imagePath)

			scale_percent = scale_percent + 100 # percent of original size
			width = int(img.shape[1] * scale_percent / 100)
			height = int(img.shape[0] * scale_percent / 100)
			dim = (width, height)
			# resize image
			resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
			imgArray.append(resized)
			#print('Resized Dimensions : ',resized.shape)

			#print(time.time()-start)
		

def lambda_handler(event, context):
    # TODO implement
    response = main()
    
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }
#