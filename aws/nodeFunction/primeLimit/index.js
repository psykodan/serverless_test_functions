exports.handler = async (event, context) =>  {
	//let start = Date.now();
	let start = event.requestContext.requestTimeEpoch;
	console.log(event.requestContext.requestTimeEpoch);
	const os = require('os');


function isPrime(number) {
    let start = 2;
    const limit = Math.sqrt(number);
    while (start <= limit) {
        if (number % start++ < 1) return false;
    }
    return number;
}



var cpu = os.cpus(), osRel = os.release(), uptime = os.uptime();

var prime;

let n = 3,count = 0;
while(true){
	if(isPrime(n) != false){
		prime = n;
		count++;
	}
	if(context.getRemainingTimeInMillis() <100){
		let stop = Date.now();
		let runtime = stop - start;
		let load = os.loadavg()
		let resposeBody = {count: count,
							prime: prime,
							model1: cpu[0]["model"],
							speed1: cpu[0]["speed"],
							user1: cpu[0]["times"]["user"],
							sys1: cpu[0]["times"]["sys"],
							idle1: cpu[0]["times"]["idle"],
							model2: cpu[1]["model"],
							speed2: cpu[1]["speed"],
							user2: cpu[1]["times"]["user"],
							sys2: cpu[1]["times"]["sys"],
							idle2: cpu[1]["times"]["idle"],
							os: osRel,
							uptime: uptime,
							runtime: runtime,
							time: start,
							load1: load[0],
							load5: load[1],
							load15: load[2],
							};

		let response = {
            statusCode: 200,
            body: JSON.stringify(resposeBody),
            headers: {
                'Access-Control-Allow-Origin': '*',
            },
        }

		return response;


	}
	n++;	
}
};