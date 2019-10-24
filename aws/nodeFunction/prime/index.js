exports.handler = async (event, context) =>  {
	let start = Date.now();
	
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
		let resposeBody = {count: count,
							prime: prime,
							cpu: cpu,
							os: osRel,
							uptime: uptime,
							runtime: runtime,
							time: start};

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
