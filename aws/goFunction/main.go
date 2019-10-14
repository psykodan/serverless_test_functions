package main

import (
   "github.com/aws/aws-lambda-go/lambda"
   "time"
   "log"
   "strconv"
)

var gr int = 0

func f1() (string, error) {
	time.Sleep(100 * time.Millisecond)
	for i := 0; i < 10; i++{
		go f2()
	}
	time.Sleep(100 * time.Millisecond)
	var message string = "Goroutines ran" + strconv.Itoa(gr)
   return message, nil
}

func f2() (string, error) {
	gr = gr + 1
	log.Println("goroutine: ", gr)
   return "function2", nil
}

func main() {
   // Make the handler available for Remote Procedure Call by AWS Lambda
   lambda.Start(f1)
}
