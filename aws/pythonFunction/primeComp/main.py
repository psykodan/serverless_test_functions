import json
import math
import cpuinfo


def isPrime(number):
    start = 2;
    limit = math.sqrt(number);
    while start <= limit:
        if (number % start < 1):
        	return False
        start += 1
    return number


def CalcPrimes():
	count = 0
	for i in range(100000):
		if isPrime(i) != False:
			count += 1
	return count	

def lambda_handler(event, context):
    # TODO implement
    count = CalcPrimes()
    print(cpuinfo.cpu.info[0]['model name'])
    return {
        'statusCode': 200,
        'body': json.dumps(count)
    }
