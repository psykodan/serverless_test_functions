import json
import os
import subprocess
import time
import math
import random




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
	res = data[2]
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
	#Aquiring the VM ID via /proc/self/cgroup

	vmID = ""
	info = ["sandbox-root"]
	
	proc = os.popen("cat /proc/self/cgroup")
	
	for line in proc:
		if info[0] in line:
			data = line.replace(" ", "").replace("\t", "").replace("\n", "").split(":")
			vmID = data[2]
			

	
  
	return vmID


def setUID():
	#Create some randome ID unique to the function and also write it to a file
	head=""
	temp=""
	for i in range(8):
		temp = str(hex(math.floor(random.random() *255 )))
		head += (temp.split("x"))[1]
		
	UID = head 

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

def isPrime(number):
    start = 2;
    limit = math.sqrt(number);
    while start <= limit:
        if (number % start < 1):
        	return False
        start += 1
    return number

def CPUutil():
	timeStart = int(time.time()*1000)
	n = 1
	res = 0
	while(int(time.time()*1000)-timeStart <= 1000):
		if(isPrime(n)!=False):
			res += 1
		n += 1

	return res


def lambda_handler(event, context):
	start = int(time.time()*1000)
	vmID = getvmID()
	UIDs = UIDcheck()
	UID = setUID()
	cputimes = getcputimes()
	cpuinfo = getcpuinfo()
	meminfo = getmeminfo()
	diskIO = iotest(512, 1000)
	uptime = cputimes[-1]
	cpuUtil = CPUutil()
	end = int(time.time()*1000)
	functime = end - start
	

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
		"uptime" : uptime,
		"CPUutil" : cpuUtil
		
	}
	return {
		'statusCode': 200,
		'body': json.dumps(response)
	}
