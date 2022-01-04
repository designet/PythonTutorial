import requests
import json
# import maidenhead as mh
with open('/Users/jimidelson/Downloads/YCCC Member Roster - YCCC Eligibility List.csv') as source_file, open('/Users/jimidelson/Downloads/YCCC Member Roster - YCCC Eligibility List + LatLon.csv', 'w') as dest_file:  
    for line in source_file:
        var1, var2, var3 = line.split(",")
        r =requests.get('https://callook.info/k1ir/json')
        print(r)
        # callook_json = mh.to_location(var2)
        # lat,lon=var4
        # dest_file.write(var1.strip()+','+var2.strip()+','+var3.strip()+','+str(lat)+','+str(lon)+'\n')
source_file.close()
dest_file.close()