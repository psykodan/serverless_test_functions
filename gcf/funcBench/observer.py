from pymongo import MongoClient
import requests
import json
from multiprocessing import Process
import time

url = 'mongodb://mongodb5446kd:na3zez@danu7.it.nuigalway.ie:8717/mongodb5446';


def f128(users):
	client = MongoClient(url)
	db = client['mongodb5446']
	collection = db['GCF']
	start = (int)(time.time() *1000)
	r = requests.get('https://us-central1-spherical-plane-258017.cloudfunctions.net/funcBench128')
	stop = (int)(time.time() *1000) 
	runtime = stop - start
	data = r.json()
	data['request'] = start;
	data['response'] = stop;
	data['runtime'] = runtime;
	data['startLag'] = data['start'] - start;
	data['users'] = users
	data['memory'] = 128;
	collection.insert_one(data)

def f256(users):
	client = MongoClient(url)
	db = client['mongodb5446']
	collection = db['GCF']
	start = (int)(time.time() *1000)
	r = requests.get('https://us-central1-spherical-plane-258017.cloudfunctions.net/funcBench256')
	stop = (int)(time.time() *1000) 
	runtime = stop - start
	data = r.json()
	data['request'] = start;
	data['response'] = stop;
	data['runtime'] = runtime;
	data['startLag'] = data['start'] - start;
	data['users'] = users
	data['memory'] = 256;
	collection.insert_one(data)

def f512(users):
	client = MongoClient(url)
	db = client['mongodb5446']
	collection = db['GCF']
	start = (int)(time.time() *1000)
	r = requests.get('https://us-central1-spherical-plane-258017.cloudfunctions.net/funcBench512')
	stop = (int)(time.time() *1000) 
	runtime = stop - start
	data = r.json()
	data['request'] = start;
	data['response'] = stop;
	data['runtime'] = runtime;
	data['startLag'] = data['start'] - start;
	data['users'] = users
	data['memory'] = 512;
	collection.insert_one(data)

def f1024(users):
	client = MongoClient(url)
	db = client['mongodb5446']
	collection = db['GCF']
	start = (int)(time.time() *1000)
	r = requests.get('https://us-central1-spherical-plane-258017.cloudfunctions.net/funcBench1024')
	stop = (int)(time.time() *1000) 
	runtime = stop - start
	data = r.json()
	data['request'] = start;
	data['response'] = stop;
	data['runtime'] = runtime;
	data['startLag'] = data['start'] - start;
	data['users'] = users
	data['memory'] = 1024;
	collection.insert_one(data)

def f2048(users):
	client = MongoClient(url)
	db = client['mongodb5446']
	collection = db['GCF']
	start = (int)(time.time() *1000)
	r = requests.get('https://us-central1-spherical-plane-258017.cloudfunctions.net/funcBench2048')
	stop = (int)(time.time() *1000) 
	runtime = stop - start
	data = r.json()
	data['request'] = start;
	data['response'] = stop;
	data['runtime'] = runtime;
	data['startLag'] = data['start'] - start;
	data['users'] = users
	data['memory'] = 2048;
	collection.insert_one(data)

def runInParallel(fns, num):
  for x in range(num):
    p = Process(target=fns, args=(num,))
    p.start()

#cold start
f128(1)
f256(1)
f512(1)
f1024(1)
f2048(1)

#warm start
f128(1)
f256(1)
f512(1)
f1024(1)
f2048(1)

#concurrent requests
runInParallel(f128, 50)
time.sleep(50)
runInParallel(f256, 50)
time.sleep(50)
runInParallel(f512, 50)
time.sleep(50)
runInParallel(f1024, 50)
time.sleep(50)
runInParallel(f2048, 50)



