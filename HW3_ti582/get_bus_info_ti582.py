# Author: Thomas Isola
# Class: PUI 2018
# This script is designed to output MTA data to a CSV file

# Make script backwards compatible
from __future__ import print_function

# Import packages
import sys
import json

try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

# Check that the script is receiving the correct number of arguments
if not len(sys.argv) == 4:
    print ("Invalid number of arguments. Run as: python get_bus_info_ti582.py APIkey BusName <filename>.csv")
    sys.exit()

# Set argument variables
APIkey = sys.argv[1]
BusLine = sys.argv[2]

# Perform the API data request
MTAurl = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s" % (APIkey, BusLine)
response = urllib.urlopen(MTAurl)
MTAdata = response.read().decode("utf-8")
data = json.loads(MTAdata)

# Extract the desireable data

data2 = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

fout = open(sys.argv[3], "w")
fout.write("Latitude,Longitude,Stop Name,Stop Status\n")
for i in range(len(data2)):
    Lat = data2[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude'],
    Long = data2[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    onCall = data2[i]['MonitoredVehicleJourney']['OnwardCalls']
    if len(onCall)==0:
        fout.write("%s,"%Lat+"%s,"%Long+"N/A,N/A\n"),
    else:
        StopName = data2[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
        StopDistance = data2[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
        fout.write("%s,"%Lat+"%s,"%Long+"%s,"%StopName+"%s\n"%StopDistance),

fout.close()
