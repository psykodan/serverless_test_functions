from pymongo import MongoClient
import requests
import json
from multiprocessing import Process
import time

url = 'mongodb://mongodb5446kd:na3zez@danu7.it.nuigalway.ie:8717/mongodb5446';


def f(users):
	client = MongoClient(url)
	db = client['mongodb5446']
	collection = db['Azure']
	start = int(time.time() *1000)
	r = requests.get('https://funcbench2.azurewebsites.net/api/funcBench')
	stop = int(time.time() *1000) 
	
	data = r.json()
	runtime = stop - start
	data['request'] = start;
	data['response'] = stop;
	data['runtime'] = runtime;
	data['startLag'] = data['start'] - start;
	
	data['memory'] = "n/a";
	collection.insert_one(data)



def runInParallel(fns, num):
  for x in range(num):
    p = Process(target=fns, args=(num,))
    p.start()

#cold start
f(1)
#f128(1)
#f256(1)
#f512(1)
#f1024(1)
#f2048(1)
"""
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
"""

