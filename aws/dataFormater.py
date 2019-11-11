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
goodVals = ["INFO", "REPORT"]
for test in ["nodePrimeComp","nodePrimeLimit","goPrimeComp","goPrimeLimit","pythonPrimeComp","pythonPrimeLimit"]:
    for memorySize in ["128","256","512","1024","2048"]:
        for name in ["", "-1","-100","-1000"]:
            fileName = "{}/{}{}{}.txt"
            outName ="{}/F{}{}{}.csv"
            logName = "logs/{}{}.txt"
            f = open(fileName.format(test,test,memorySize,name))
            out = open(outName.format(test,test,memorySize,name), "a")
            log = open(logName.format(test,memorySize))
            runtimes = []
            ID = []
            for l in log:
                temp = l.replace(" ","@")
                temp = temp.replace("\t","@")
                temp = temp.replace("\n","@")
                temp = temp.split("@")
                list(filter(lambda a: a != "", temp))
                
                if "INFO" in temp or "[INFO]" in temp:
                    if "go" in test:
                        ID.append([temp[3],temp[5]])
                        
                    elif "node" in test:
                        ID.append([temp[1],temp[3]])
                    elif "python" in test:
                        ID.append([temp[2],temp[3]])
                        
                
                if "REPORT" in temp:
                    
                    if "Init" in l:
                        
                        runtimes.append([temp[2],float(temp[4])+float(temp[21])])
                    else:
                        runtimes.append([temp[2],temp[4]])
                





            for line in f:

                if line not in badVals:
                    jsonline = json.loads(line)

                    if test == "nodePrimeLimit" or test == "goPrimeLimit" or test == "pythonPrimeLimit":
                        if test == "goPrimeLimit":
                            testID = str(jsonline["ID"])
                            runtime = IDpair(testID)
                                    


                            out.write(str(jsonline["ID"]) + "," + str(jsonline["Count"]) + "," + str(jsonline["Prime"]) + "," + jsonline["Model1"] + "," + str(jsonline["Speed1"]) + "," + str(jsonline["User1"]) + "," + str(jsonline["Sys1"]) + "," + str(jsonline["Idle1"]) + "," + str(jsonline["Model2"]) + "," + str(jsonline["Speed2"]) + "," + str(jsonline["User2"]) + "," + str(jsonline["Sys2"]) + "," + str(jsonline["Idle2"]) + "," + jsonline["OS"] + "," + str(jsonline["Uptime"]) + "," + str(runtime) + "," + str(jsonline["Time"]) + "," + str(jsonline["Load1"]) + "," +str(jsonline["Load5"]) + "," +str(jsonline["Load15"])+"\n")
                        
                        else:
                            testID = str(jsonline["id"])
                            runtime = IDpair(testID)                      

                            out.write(str(jsonline["id"]) + "," + str(jsonline["count"]) + "," + str(jsonline["prime"]) + "," + jsonline["model1"] + "," + str(jsonline["speed1"]) + "," + str(jsonline["user1"]) + "," + str(jsonline["sys1"]) + "," + str(jsonline["idle1"]) + "," + str(jsonline["model2"]) + "," + str(jsonline["speed2"]) + "," + str(jsonline["user2"]) + "," + str(jsonline["sys2"]) + "," + str(jsonline["idle2"]) + "," + jsonline["os"] + "," + str(jsonline["uptime"]) + "," + str(runtime) + "," + str(jsonline["time"]) + "," + str(jsonline["load1"]) + "," +str(jsonline["load5"]) + "," +str(jsonline["load15"])+"\n")
                    else:
                        if test == "goPrimeComp":
                            testID = str(jsonline["ID"])
                            runtime = IDpair(testID)
                            
                            out.write(str(jsonline["ID"]) + "," + str(jsonline["Count"]) + "," +  jsonline["Model1"] + "," + str(jsonline["Speed1"]) + "," + str(jsonline["User1"]) + "," + str(jsonline["Sys1"]) + "," + str(jsonline["Idle1"]) + "," + str(jsonline["Model2"]) + "," + str(jsonline["Speed2"]) + "," + str(jsonline["User2"]) + "," + str(jsonline["Sys2"]) + "," + str(jsonline["Idle2"]) + "," + jsonline["OS"] + "," + str(jsonline["Uptime"]) + "," +str(runtime) + "," + str(jsonline["Time"]) + "," + str(jsonline["Load1"]) + "," +str(jsonline["Load5"]) + "," +str(jsonline["Load15"])+"\n")
                            

                        else:
                            testID = str(jsonline["id"])
                            runtime = IDpair(testID)
                                                               

                            out.write(str(jsonline["id"]) + "," + str(jsonline["count"]) + "," + jsonline["model1"] + "," + str(jsonline["speed1"]) + "," + str(jsonline["user1"]) + "," + str(jsonline["sys1"]) + "," + str(jsonline["idle1"]) + "," + str(jsonline["model2"]) + "," + str(jsonline["speed2"]) + "," + str(jsonline["user2"]) + "," + str(jsonline["sys2"]) + "," + str(jsonline["idle2"]) + "," + jsonline["os"] + "," + str(jsonline["uptime"]) + "," +str(runtime) + "," + str(jsonline["time"]) + "," + str(jsonline["load1"]) + "," +str(jsonline["load5"]) + "," +str(jsonline["load15"])+"\n")

            f.close()
            out.close()
            log.close()


