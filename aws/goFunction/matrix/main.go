package main


import (
   "github.com/aws/aws-lambda-go/lambda"
   "github.com/aws/aws-lambda-go/events"
   "github.com/shirou/gopsutil/cpu"
   //"github.com/shirou/gopsutil/load"
   "encoding/json"
   "time"
   "math"
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
	
	count := 0
	for i := 1; i <= 100000; i++ {
        if IsPrime(i) {
            count++
        }
    }



    start := request.RequestContext.RequestTimeEpoch
    stop := time.Now().UnixNano()/1000000
   	
  	runtime := stop - start

	
	
	cpui, _ := cpu.Times(true)
	cpun, _ := cpu.Info()
	

	type ColorGroup struct {
		CPU    []cpu.InfoStat
		ID     []cpu.TimesStat
		Name   int64
		
	}
	group := ColorGroup{
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
