# Author: Thomas Isola
# Class: PUI 2018
# This script is designed to output MTA bus information with an API key and the bus name as the input.

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
if not len(sys.argv) == 3:
    print ("Invalid number of arguments. Run as: python show_bus_locations_ti582.py APIkey BusName")
    sys.exit()

# Set argument variables
APIkey = sys.argv[1]
BusName = sys.argv[2]

# Perform the API data request
MTAurl = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s" % (APIkey, BusName)
response = urllib.urlopen(MTAurl)
MTAdata = response.read().decode("utf-8")
data = json.loads(MTAdata)

# Extract the desireable data
# print(data)
MTAinfo = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
active_buses = len(MTAinfo)

# Print out the desired output
print ("The Bus Route is: %s" % BusName)
print ("The number of active buses on the route is: %s" % active_buses)
for i in range(len(MTAinfo)):
    location = json.dumps(MTAinfo[i]['MonitoredVehicleJourney']['VehicleLocation'])
    location2 = location.split(",")
    print ("Bus %s is at latitude"%(i+1),location2[1][13:22],"and longitude",location2[0].rsplit('}',1)[0][14:]),
