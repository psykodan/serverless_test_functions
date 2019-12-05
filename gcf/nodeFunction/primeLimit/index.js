/**
 * Responds to any HTTP request.
 *
 * @param {!express:Request} req HTTP request context.
 * @param {!express:Response} res HTTP response context.
 */
exports.index = (req, res) => {

	let begin = Date.now();

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

		for(i = 0; i<250000; i++){
			isPrime(i)
		}

		let stop = Date.now();
		//let runtime = stop - start;
		let load = os.loadavg()
		var head = "";
		for(var i=0;i<7;i++){
    		head += (Math.floor( Math.random() * 0xFF)).toString(16);
    
		};
		var id = head + (stop).toString();
		console.log(id)
		let responseBody = {id: id,
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
		run = false;
		res.status(200).json(responseBody);


	};
	n++;	
};
};