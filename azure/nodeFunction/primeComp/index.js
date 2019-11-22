module.exports = async function (context, req) {
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
let load = os.loadavg()
var id = context.executionContext.invocationId;
console.log(id)
let responseBody = {id: id,
					count: count,
					model1: cpu[0]["model"],
					speed1: cpu[0]["speed"],
					user1: cpu[0]["times"]["user"]/10, // divide by 10 to temporarily fix error at https://github.com/nodejs/node/blob/bdc09c63e6ee9208ebab7e77ac513705263bbd9a/deps/uv/src/unix/linux-core.c#L816
					sys1: cpu[0]["times"]["sys"]/10,		// it should be user /clock_ticks (*1000 if you want ms)
					idle1: cpu[0]["times"]["idle"]/10,
					os: osRel,
					uptime: uptime,
					time: stop,
					load1: load[0],
					load5: load[1],
					load15: load[2],
					};


		context.res.send(JSON.stringify(responseBody));

};