import json


def IDpair(testID):

    for r in ID:
       
        if(r[1]==testID):
            for s in runtimes:
                if s[0] == r[0]:
                    runtime = s[1]
                    runtimes.remove(s)
                    ID.remove(r)
                    
                    return runtime    
                else:
                    return "ERROR"

#
badVals = ["\n", '{"message":"Missing Authentication Token"}\n' , '{"message": "Internal server error"}\n' ]
#goodVals = ["INFO", "REPORT"]
for test in ["nodePrimeComp","nodePrimeLimit","goPrimeComp","goPrimeLimit","pythonPrimeComp","pythonPrimeLimit"]:
    for memorySize in ["128","256","512","1024","2048"]:
        for name in ["", "-1","-1000"]:
            fileName = "{}/{}{}{}.txt"
            outName ="{}/F{}{}{}.csv"
            logName = "logs/{}{}.txt"
            f = open(fileName.format(test,test,memorySize,name))
            out = open(outName.format(test,test,memorySize,name), "a")
            log = open(logName.format(test,memorySize))
            runtimes = []
            ID = []
            


            for l in log:
                jsonLogLine = json.loads(l)

                text = str(jsonLogLine["textPayload"])
                if "started" not in text:
                    if "code:200" in text:
                        temp = text.split("ms")
                        runtimes.append([str(jsonLogLine["labels"]["execution_id"]), float(temp[0].replace("Functionexecutiontook", ""))])

                    else:
                        ID.append([str(jsonLogLine["labels"]["execution_id"]), text])







           for line in f:

                if line not in badVals:
                    jsonline = json.loads(line)

                    if test == "nodePrimeLimit" or test == "goPrimeLimit" or test == "pythonPrimeLimit":
                        if test == "goPrimeLimit":
                            testID = str(jsonline["ID"])
                            runtime = IDpair(testID)
                                    


                            out.write(str(jsonline["ID"]) + "," + str(jsonline["Count"]) + "," + str(jsonline["Prime"]) + "," + jsonline["OS"] + "," + str(jsonline["Uptime"]) + "," + str(runtime) + "," + str(jsonline["Time"]) + "," + str(jsonline["Load1"]) + "," +str(jsonline["Load5"]) + "," +str(jsonline["Load15"])+"\n")
                        
                        else:
                            testID = str(jsonline["id"])
                            runtime = IDpair(testID)                      

                            out.write(str(jsonline["id"]) + "," + str(jsonline["count"]) + "," + str(jsonline["prime"]) + "," + jsonline["os"] + "," + str(jsonline["uptime"]) + "," + str(runtime) + "," + str(jsonline["time"]) + "," + str(jsonline["load1"]) + "," +str(jsonline["load5"]) + "," +str(jsonline["load15"])+"\n")
                    else:
                        if test == "goPrimeComp":
                            testID = str(jsonline["ID"])
                            runtime = IDpair(testID)
                            
                            out.write(str(jsonline["ID"]) + "," + str(jsonline["Count"]) + "," + jsonline["OS"] + "," + str(jsonline["Uptime"]) + "," +str(runtime) + "," + str(jsonline["Time"]) + "," + str(jsonline["Load1"]) + "," +str(jsonline["Load5"]) + "," +str(jsonline["Load15"])+"\n")
                            

                        else:
                            testID = str(jsonline["id"])
                            runtime = IDpair(testID)
                                                               

                            out.write(str(jsonline["id"]) + "," + str(jsonline["count"]) + "," + jsonline["os"] + "," + str(jsonline["uptime"]) + "," +str(runtime) + "," + str(jsonline["time"]) + "," + str(jsonline["load1"]) + "," +str(jsonline["load5"]) + "," +str(jsonline["load15"])+"\n")

            f.close()
            out.close()
            log.close()