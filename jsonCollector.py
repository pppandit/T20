import urllib2
import time
import os

start = 598001
end = 598058

prefix = 'http://www.espncricinfo.com/ci/engine/match/gfx/';
suffix = '.json?inning=1;template=wagon';

fileReader = None;
fileWriter = None;

for index in range(start,end+1):
    print "Match " + str(index) + " of " + str(end)
    requestObject = urllib2.Request(prefix+str(index)+suffix);
    requestObject.add_header('user-agent', "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11");
    
    fileReader = urllib2.urlopen(requestObject);
    
    fileWriter = open('resources/'+str(index)+'_inning1'+ '.txt', 'w');
    fileWriter.write(fileReader.read());
    fileWriter.close();
    
    time.sleep(60);
    
