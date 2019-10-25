package main


import (
   "github.com/aws/aws-lambda-go/lambda"
   "github.com/aws/aws-lambda-go/events"
   "encoding/json"
   "time"
   "log"
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


func CalcPrime(request events.APIGatewayProxyRequest) (events.APIGatewayProxyResponse, error){
	start := time.Now().UnixNano()/1000000
	count := 0
	for i := 1; i <= 100000; i++ {
        if IsPrime(i) {
            count++
        }
    }

    t := time.Now().UnixNano()/1000000
    log.Println(count)
  	log.Println(start)
  	log.Println(t)
  	runtime := t - start
    response, err := json.Marshal(runtime)

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
