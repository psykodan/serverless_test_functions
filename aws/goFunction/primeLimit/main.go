package main


import (
   "github.com/aws/aws-lambda-go/lambda"
   "github.com/aws/aws-lambda-go/events"
   "github.com/aws/aws-lambda-go/lambdacontext"
   "github.com/shirou/gopsutil/cpu"
   "github.com/shirou/gopsutil/host"
   "github.com/shirou/gopsutil/load"
   "encoding/json"
   "time"
   "math"
   "context"
   "math/rand"
   "strconv"
   "fmt"
   "log"
)

//var start = time.Now().Unix()
func IsPrime(value int) bool {
    for i := 2; i <= int(math.Floor(math.Sqrt(float64(value)))); i++ {
        if value%i == 0 {
            return false
        }
    }
    return value > 1
}


func CalcPrime(ctx context.Context, request events.APIGatewayWebsocketProxyRequest) (events.APIGatewayProxyResponse, error){
	
	//deadline, _ := ctx.Deadline()
    lc, _ := lambdacontext.FromContext(ctx)

    
	start := time.Now().UnixNano()/1000000
	//start := request.RequestContext.RequestTimeEpoch

	load, _ := load.Avg()
  	load1 := load.Load1
  	load5 := load.Load5
  	load15 := load.Load15

	
	cpuinfo, _ := cpu.Info()
	osinfo, _ := host.Info()
	cputime, _ := cpu.Times(true)
	

	type ResponseBody struct {

		ID 		string
		Count	int 
		Prime 	int	
		Model1	string
		Speed1	float64
		User1	float64
		Sys1	float64
		Idle1	float64
		Model2	string
		Speed2	float64
		User2	float64
		Sys2	float64
		Idle2	float64
		OS 		string
		Uptime  uint64
		Time 	int
		Load1 	float64
		Load5 	float64
		Load15 	float64
		
		
	}

	prime := 0
	n := 3
	count := 0

	for 1 == 1{
        

        if (time.Now().UnixNano()/1000000) - start >2000{

        	for i := 1; i <= 250000; i++ {
        		IsPrime(i)
            
        
    		}



        	stop := int(time.Now().UnixNano()/10000000)
		  	//runtime := stop - start

		  	head := ""
			rand.Seed(time.Now().UnixNano())
			for i := 0; i < 7; i++ {
				head += fmt.Sprintf("%x",int(rand.Float64() * 255))
			}
			id := head + strconv.Itoa(stop)
			log.Printf("\t%s\tINFO\t" + id, lc.AwsRequestID)
		  	
			group := ResponseBody{
				ID:		id,
				Count:	count,
				Prime:	prime,
				Model1:	cpuinfo[0].ModelName,
				Speed1: cpuinfo[0].Mhz,
				User1:	cputime[0].User * 1000,
				Sys1:	cputime[0].System * 1000,
				Idle1:	cputime[0].Idle * 1000,
				Model2:	cpuinfo[1].ModelName,
				Speed2: cpuinfo[1].Mhz,
				User2:	cputime[1].User * 1000,
				Sys2:	cputime[1].System * 1000,
				Idle2:	cputime[1].Idle * 1000,
				OS:		osinfo.KernelVersion,
				Uptime:	osinfo.Uptime,
				Time:	stop,
				Load1:	load1,
				Load5:	load5,
				Load15:	load15,
				
			}


		    response, err := json.Marshal(group)


		  	if err != nil {
		    	return events.APIGatewayProxyResponse{}, err
		  	}


		   return events.APIGatewayProxyResponse{
				StatusCode:200,
				Body: string(response),
			}, nil
		        }

        if IsPrime(n) {
        	prime = n
            count++
        }
        n++
    }
    
    return events.APIGatewayProxyResponse{
				StatusCode:400,
				Body: string("Error"),
			}, nil



    
}


func main() {
   // Make the handler available for Remote Procedure Call by AWS Lambda
   
   lambda.Start(CalcPrime)
}
