module.exports = async function (context, req) {

	let begin = Date.now();
	//let start = event.requestContext.requestTimeEpoch;
	//console.log(event.requestContext.requestTimeEpoch);
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

let n = 3,count = 0, run = true;
while(run == true){
	if(isPrime(n) != false){
		prime = n;
		count++;
	};
	if(Date.now()-begin>2000){
		let stop = Date.now();
		//let runtime = stop - start;
		let load = os.loadavg()
		var id = context.executionContext.invocationId;

		console.log(id)
		let responseBody = {id: id,
							count: count,
							prime: prime,
							model1: cpu[0]["model"],
							speed1: cpu[0]["speed"],
							user1: cpu[0]["times"]["user"],
							sys1: cpu[0]["times"]["sys"],
							idle1: cpu[0]["times"]["idle"],
							os: osRel,
							uptime: uptime,
							time: stop,
							load1: load[0],
							load5: load[1],
							load15: load[2],
							};
		run = false;
		context.res.send(JSON.stringify(responseBody));


	};
	n++;	
};
};