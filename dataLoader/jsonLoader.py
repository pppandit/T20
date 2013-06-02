'''
Created on May 25, 2013

@author: neer
'''


if __name__ == '__main__':
    pass

from pymongo import MongoClient
mongoClient = MongoClient()
db = mongoClient.cricket

collection = db.cricket

fileReader = open('../resources/597998.txt','r')
txt = fileReader.read()
fileReader.close()


import json
obj = json.loads(txt)
print obj['t2']['p']

fileReader = open('../resources/597998_inning1.txt','r')
txt = fileReader.read();
fileReader.close()

runs_inning1 = json.loads(txt)

obj['t1']['r'] = runs_inning1['runs']
print obj;

fileWriter = open('../resources/597998_complete.txt','w')
fileWriter.write(json.dumps(obj));
fileWriter.close()

