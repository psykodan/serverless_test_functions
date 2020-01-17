import json
import os
import subprocess
import time
import math
import random

from flask import jsonify




def iotest(size, cnt):
	
	#IO throughput/latency test using dd command

	proc = subprocess.Popen(["dd",
							 "if=/dev/urandom",
							 "of=/tmp/ioload.log",
							 "bs=%s" % size,
							 "count=%s" % cnt,
							 "conv=fdatasync",
							 "oflag=dsync"],
							stderr=subprocess.PIPE)
	err, out = proc.communicate()
	data = str(out)
	data = data.split(",")
	res = data[3]
	res = res.replace(" ","").replace("\\n'", "")

	return res
	
	

def getcpuinfo():

	#Aquiring the CPU model info via /proc/cpuinfo

	cpuinfo = []
	info = ["processor", "model", "model name", "cpu MHz", "cache size"]
	
	proc = os.popen("cat /proc/cpuinfo")

	for line in proc:
		if any(val in line for val in info):
			data = line.replace(" ", "").replace("\t", "").replace("\n", "").split(":")
			cpuinfo.append(data[1])
	
  
	return cpuinfo


def getmeminfo():

	#Aquiring the memory info via /proc/meminfo

	meminfo = 0
	info = ["MemTotal"]
	
	proc = os.popen("cat /proc/meminfo")

	for line in proc:
		if any(val in line for val in info):
			data = line.replace(" ", "").replace("\t", "").replace("\n", "").split(":")
			meminfo = data[1]
	
  
	return meminfo

def getcputimes():

	#Aquiring the CPU times info via /proc/stat

	cputimes = []
	info = ["cpu", "btime"]
	
	proc = os.popen("cat /proc/stat")
	#print(proc.read())
	for line in proc:
		if info[0] in line:
			raw = line.replace("\t", "").replace("\n", "").split(" ")
			data = ' '.join(raw).split()
			cputimes.append(data[0])
			cputimes.append(data[1])
			cputimes.append(data[3])
			cputimes.append(data[4])
		elif info[1] in line:
			data = line.replace("\t", "").replace("\n", "").split(" ")
			cputimes.append(data[1])
	
  
	return cputimes


def getvmID():
	#Aquiring the VM ID via a temporary file

	vmID = ""
	
	
	path = "/tmp/vmID.txt"
	if os.path.exists(path):
		f = open(path)
		res = f.read()
		f.close()
		vmID = res
	else:
		head=""
		temp=""
		for i in range(8):
			temp = str(hex(math.floor(random.random() *255 )))
			head += (temp.split("x"))[1]
			
		vmID = head 

		f = open(path, "a")
		f.write(vmID)
		f.close()
	
	return vmID


def setUID():
	#Create some randome ID unique to the function and also write it to a file
	head=""
	temp=""
	for i in range(7):
		temp = str(hex(math.floor(random.random() *255 )))
		head += (temp.split("x"))[1]
		
	UID = head + str(int(start)) 

	f = open("/tmp/UID.txt", "a")
	f.write(UID)
	f.write("\n")
	f.close()

	return UID

def UIDcheck():
	UIDs = []
	path = "/tmp/UID.txt"
	if os.path.exists(path):
		f = open(path)
		res = f.read()
		f.close()
		UIDs = res.split("\n")
	
	return UIDs


def main(request):
	start = int(time.time()*1000)
	vmID = getvmID()
	UIDs = UIDcheck()
	UID = setUID()
	cputimes = getcputimes()
	cpuinfo = getcpuinfo()
	meminfo = getmeminfo()
	diskIO = iotest(512, 1000)
	end = int(time.time()*1000)
	functime = end - start
	uptime = cputimes[-1]
	
	response = {
		"vmID" : vmID,
		"UID" : UID,
		"UIDs" : UIDs,
		"cputimes" : cputimes,
		"cpuinfo" : cpuinfo,
		"meminfo" : meminfo,
		"diskIO" : diskIO,
		"start" : start,
		"end" : end,
		"funcTime" : functime,
		"uptime" : uptime
		
	}
	return jsonify(response)