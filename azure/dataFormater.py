import json


def IDpair(testID):

    for s in runtimes:
        print(s)
        print(testID)
        if s[0] == testID:
            runtime = s[1]
            runtimes.remove(s)
           
            
            return runtime    
    else:
        return "ERROR"

#
badVals = ["\n", '{"message":"Missing Authentication Token"}\n' , '{"message": "Internal server error"}\n' ]
#goodVals = ["INFO", "REPORT"]
for test in ["nodePrimeComp","nodePrimeLimit","pythonPrimeComp","pythonPrimeLimit"]:
    for name in ["","-1","-1000"]:
        fileName = "{}/{}{}.txt"
        outName ="{}/F{}{}.csv"
        logName = "logs/{}.csv"
        f = open(fileName.format(test,test,name))
        out = open(outName.format(test,test,name), "a")
        log = open(logName.format(test))
        runtimes = []
        



        for l in log:
            if "duration" not in l:
                temp = l.replace('"','')
                temp = temp.replace('\n','')

                temp = temp.split(",")
                runtimes.append([temp[1],float(temp[0])])

       
        for line in f:

            if line not in badVals:
                jsonline = json.loads(line)

                if test == "nodePrimeLimit" or test == "pythonPrimeLimit":
                    
                    testID = str(jsonline["id"])
                    runtime = IDpair(testID)                      

                    out.write(str(jsonline["id"]) + "," + str(jsonline["count"]) + "," + str(jsonline["prime"]) + "," + jsonline["model1"] + "," + str(jsonline["speed1"]) + "," + str(jsonline["user1"]) + "," + str(jsonline["sys1"]) + "," + str(jsonline["idle1"]) + "," +jsonline["os"] + "," + str(jsonline["uptime"]) + "," + str(runtime) + "," + str(jsonline["time"]) + "," + str(jsonline["load1"]) + "," +str(jsonline["load5"]) + "," +str(jsonline["load15"])+"\n")
                else:
                    
                    testID = str(jsonline["id"])
                    runtime = IDpair(testID)
                                                       

                    out.write(str(jsonline["id"]) + "," + str(jsonline["count"]) + "," + jsonline["model1"] + "," + str(jsonline["speed1"]) + "," + str(jsonline["user1"]) + "," + str(jsonline["sys1"]) + "," + str(jsonline["idle1"]) + "," + str(jsonline["os"]) + "," + str(jsonline["uptime"]) + "," +str(runtime) + "," + str(jsonline["time"]) + "," + str(jsonline["load1"]) + "," +str(jsonline["load5"]) + "," +str(jsonline["load15"])+"\n")

        f.close()
        out.close()
        log.close()


