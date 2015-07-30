from urllib.request import urlopen
import json
import sqlite3

# Get the dataset
# url could be param??
url = 'http://whereismypower.co.za/api/get_status.json'
#url = 'http://122.181.128.170:8080/cap-dataservice/rest/dataservice/1/CLM/1/CustomerProfiles/json/query'
response = urlopen(url)

# Convert bytes to string type and string type to dict
string = response.read().decode('utf-8')
json_obj = json.loads(string)

##print(json_obj) # prints the string with 'source_name' key
json_clob = json.dumps(json_obj, sort_keys=True, indent=4)

stage = (json_obj['active_stage']) 
stageName = (json_obj['active_stage_name'])

print(json_clob)
print (stage,stageName)


#print(json_clob)
if stageName == 'No Load Shedding':
   print ('Currently no load shedding')
else:
   print('We are currently on', stageName)
#print(stageName)

conn = sqlite3.connect('powerDown.db')
#ide = 2

#conn.execute("INSERT INTO run (id,value) \
#      VALUES (1, '5' )");

#conn.execute('delete from run')

#conn.execute('insert into run values (?,?)', (3,json_clob))

#conn.commit()

cursor = conn.execute("SELECT timeon, timeoff from wschedule where stage = 1 and Day30 like '%14%'")
for row in cursor:
   timeon  = (row[0])
   timeoff  = (row[1])
   #print ("timeon = ", row[0])
   #print ("timeoff = ", row[1])
   #print ("timeoff = ", row[1])
   #print ("ADDRESS = ", row[2])
   #print ("SALARY = ", row[3], "\n")



conn.close()

print('Loadshedding starts at', timeon, 'and will finish at', timeoff)


##data = json_obj
##for key, value in data.items():
##    print (value)

##import urllib.request
##import json
##response = urllib.request.urlopen('http://whereismypower.co.za/api/get_status.json')
##html = response.read()
##print(html.json())
