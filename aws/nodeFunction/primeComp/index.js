exports.handler = async (event, context) =>  {
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

let n = 3,count = 0;
while(true){
	
	if(Date.now()-begin>1000){

		for(i = 0; i<250000; i++){
		isPrime(i)
		}	

		let stop = Date.now();
		//let runtime = stop - start;
		let load = os.loadavg()
		var head = "";
		for(var i=0;i<7;i++){
    		head += (Math.floor( Math.random() * 0xFF)).toString(16);
    
		}
		var id = head + (stop).toString();
		console.log(id)
		let resposeBody = {id: id,
							count: count,
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
							time: stop,
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
	if(isPrime(n) != false){
		prime = n;
		count++;
	}
	n++;	
}
};