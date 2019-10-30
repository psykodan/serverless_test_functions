package main


import (
   "github.com/aws/aws-lambda-go/lambda"
   "github.com/aws/aws-lambda-go/events"
   "github.com/shirou/gopsutil/cpu"
   "github.com/capnm/sysinfo"
   "github.com/shirou/gopsutil/load"
   "encoding/json"
   "time"
   "math"
   "fmt"
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


func CalcPrime(request events.APIGatewayWebsocketProxyRequest) (events.APIGatewayProxyResponse, error){
	
	start := request.RequestContext.RequestTimeEpoch

	count := 0
	for i := 1; i <= 100000; i++ {
        if IsPrime(i) {
            count++
        }
    }



    
    stop := time.Now().UnixNano()/1000000
  	runtime := stop - start
  	load1 := load.Load1
  	load5 := load.Load5
  	load15 := load.Load15

	
	
	cputime, _ := cpu.Times(true)
	cpuinfo, _ := cpu.Info()
	uptime := sysinfo.Get().Uptime

	fmt.Printf(cputime.CPU)
		

	type ResponseBody struct {
		CPU    []cpu.InfoStat
		ID     []cpu.TimesStat
		Name   int64
		
	}
	group := ResponseBody{
		CPU:	cpun,
		ID:     cpui,
		Name:   runtime,
		
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


func main() {
   // Make the handler available for Remote Procedure Call by AWS Lambda
   
   lambda.Start(CalcPrime)
}
