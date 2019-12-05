import json
import math
import psutil
import platform
import time
import random
import logging

from flask import jsonify


def isPrime(number):
    start = 2;
    limit = math.sqrt(number);
    while start <= limit:
        if (number % start < 1):
        	return False
        start += 1
    return number


def CalcPrimes():
	logging.getLogger().setLevel(logging.INFO)
	#start = event["requestContext"]["requestTimeEpoch"]

	count = 0
	for i in range(250000):
		if isPrime(i) != False:
			count += 1




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

	response = {
	"id":	ID,
	"count" : count,
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

def main(request):
	# TODO implement
	response = CalcPrimes()
	return jsonify(response)
