import azure.functions as func
import json
import math
import psutil
import platform
import time
import random
import logging



def isPrime(number):
    start = 2
    limit = math.sqrt(number)
    while start <= limit:
        if (number % start < 1):
            return False
        start += 1
    return number


def CalcPrimes(context):
    logging.getLogger().setLevel(logging.INFO)

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
    mem = psutil.virtual_memory()
    logging.info(mem)
    os = platform.release()
    stop = int(time.time()*1000)
    uptime = int((stop/1000)-psutil.boot_time())
    #runtime = stop - start
    load = psutil.getloadavg()

    ID = context.invocation_id

    logging.info(ID)

    response = {
                "id":	ID,
                "count" : count,
                "model1" : model[0],
                "speed1" : speed[0],
                "user1" : times[0].user*1000,
                "sys1" : times[0].system*1000,
                "idle1" : times[0].idle*1000,
                "os" : os,
                "uptime" : uptime,
                "time"	:	stop,
                "load1" : load[0],
                "load5" : load[1],
                "load15" : load[2]}
    return response	


def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    response = CalcPrimes(context)
    return func.HttpResponse(body=json.dumps(response),
   status_code=200,mimetype='application/json')