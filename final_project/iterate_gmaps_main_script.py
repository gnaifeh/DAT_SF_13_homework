
import json
import urllib2
import pandas as pd
import numpy as np
from numpy import division
from datetime import datetime


array_of_entries = np.array([])
query_time = datetime.now().isoformat(' ')
query_origins = np.array(result2['origin_addresses'])
query_destinations = np.array(result2['destination_addresses'])
#iterate through and print all trips
if result2['status'] == 'OK':
    query_rows = result2['rows']
    for i in np.arange(len(query_rows)):
        query_elements = query_rows[i]['elements']
        for n in np.arange(len(query_elements)):
            try:
                print "Trip from {} to {}".format(query_origins[i],query_destinations[n])
                print
                if 'duration' in query_elements[n]:
                    this_trip_duration = query_elements[n]['duration']['value']
                else:
                    this_trip_duration = None
                if 'distance' in query_elements[n]:
                    this_trip_distance = query_elements[n]['distance']['value']
                else:
                    this_trip_distance = None
                if 'fare' in query_elements[n]:
                    this_trip_fare = query_elements[n]['fare']['value']
                else:
                    this_trip_fare = None
                print "Duration:", this_trip_duration
                print "Distance:", this_trip_distance
                print "Fare:", this_trip_fare
            except:
                if (query_elements[n]['status'] != "OK"):
                    print "Element status is: {}".format(query_elements[n]['status'])
            entry_array = np.array([query_time, query_origins[i], query_destinations[n], this_trip_duration, this_trip_distance, this_trip_fare])
            array_of_entries = np.append(array_of_entries, entry_array)
else:
    print 'The status of the query was not listed as "Ok"'
    print 'The status of the query was listed as: {}'.format(result2['status'])
print datetime.now().isoformat(' ')
print array_of_entries
