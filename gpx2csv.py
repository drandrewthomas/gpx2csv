#!/usr/bin/python

import sys,os
import xml.etree.cElementTree as ET
import string

global numwpt

def main(infile):
    global numwpt
    outfile=infile+".csv"
    mainNS=string.Template("{http://www.topografix.com/GPX/1/0}$tag")
    try:
      et=ET.parse(open(infile))
    except Exception, inst:
      print "Oh deary, deary me (%s)!!!" % (inst)
      print ""
      sys.exit()
    root=et.getroot()
    with open(outfile,"w") as myfile:
      myfile.write("Type,Date/Time,Longitude,Latitude,Elevation\n")
    for child in root.findall('{http://www.topografix.com/GPX/1/0}wpt'):
      lon=child.get('lon')
      lat=child.get('lat')
      ele=child.find('{http://www.topografix.com/GPX/1/0}ele').text
      sme=child.find('{http://www.topografix.com/GPX/1/0}time').text
      tme=sme.split("T")
      with open(outfile,"a") as myfile:
        myfile.write("WPT,"+tme[0]+" "+tme[1].strip("Z")+","+lon+","+lat+","+ele+"\n")
      numwpt=numwpt+1
          

if __name__ == "__main__":
  global numwpt
  numwpt=0
  if len(sys.argv)>1:
    main(sys.argv[1])
    print "Saved "+str(numwpt)+" waypoints."
    print ""
  else:
    print "You forgot to include the filename!!!"
    print ""
    sys.exit()
    
  
