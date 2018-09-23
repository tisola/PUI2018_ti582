{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pylab as pl\n",
    "import os\n",
    "import json\n",
    "try:\n",
    "    import urllib2 as urllib\n",
    "except ImportError:\n",
    "    import urllib.request as urllib\n",
    "\n",
    "%pylab inline\n",
    "pl.rc('font', size=15)\n",
    "\n",
    "url = \"http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json\"\n",
    "#url = \"http://api.openweathermap.org/data/2.5/weather?q=\" + \\\n",
    "#    \"New York&APPID=\" + os.getenv(\"OPENWEATHERKEY\") \n",
    "\n",
    "#print (url)\n",
    "response = urllib.urlopen(url)\n",
    "data = response.read().decode(\"utf-8\")\n",
    "data = json.loads(data)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "PUI2016_Python3",
   "language": "python",
   "name": "pui2016_python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.5.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
