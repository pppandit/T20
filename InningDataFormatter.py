import json;
startIndex=597998
endIndex=598058;

inputPath="/home/pranav/Documents/Dropbox/Cricket/";
outputPath="/home/pranav/Documents/Dropbox/Cricket/Formatted/"

def convert(inputJson):
    if isinstance(inputJson, dict):
        return {convert(key): convert(value) for key, value in inputJson.iteritems()}
    elif isinstance(inputJson, list):
        return [convert(element) for element in inputJson]
    elif isinstance(inputJson, unicode):
        return inputJson.encode('utf-8')
    else:
        return inputJson

for index in range(startIndex, endIndex+1):
    print "Match "+str(index)
    json_inn1=open(inputPath+str(index)+"_inning1.txt");
    dataInn1=json.load(json_inn1);
    dataInn1=convert(dataInn1);
    fileWriter = open(outputPath+str(index)+'_Inn1'+ '.json', 'w');
    fileWriter.write(str(dataInn1["runs"]));
    fileWriter.close();
    
    json_inn2=open(inputPath+str(index)+".txt");
    dataInn2=json.load(json_inn2);
    dataInn2=convert(dataInn2);
    fileWriter = open(outputPath+str(index)+'_Inn2'+ '.json', 'w');
    fileWriter.write(str(dataInn2["t2"]["r"]));
    fileWriter.close();
    