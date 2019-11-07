exports.handler = async (event, context) =>  {
	//let start = Date.now();
	//let start = event.requestContext.requestTimeEpoch;
	
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



let count = 0;
for(i = 0; i<250000; i++){
	if(isPrime(i) != false){
		count++;
	}
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
					model1: cpu[0]["model"],
					speed1: cpu[0]["speed"],
					user1: cpu[0]["times"]["user"]/10, // divide by 10 to temporarily fix error at https://github.com/nodejs/node/blob/bdc09c63e6ee9208ebab7e77ac513705263bbd9a/deps/uv/src/unix/linux-core.c#L816
					sys1: cpu[0]["times"]["sys"]/10,		// it should be user /clock_ticks (*1000 if you want ms)
					idle1: cpu[0]["times"]["idle"]/10,
					model2: cpu[1]["model"],
					speed2: cpu[1]["speed"],
					user2: cpu[1]["times"]["user"]/10,
					sys2: cpu[1]["times"]["sys"]/10,
					idle2: cpu[1]["times"]["idle"]/10,
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

};