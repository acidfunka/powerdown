from urllib.request import urlopen
import json

# Get the dataset
url = 'http://whereismypower.co.za/api/list_areas.json'
response = urlopen(url)

# Convert bytes to string type and string type to dict
string = response.read().decode('utf-8')
json_obj = json.loads(string)

print(json_obj) # prints the string with 'source_name' key
print(json.dumps(json_obj, sort_keys=True, indent=4))
##data = json_obj
##for key, value in data.items():
##    print (value)

##import urllib.request
##import json
##response = urllib.request.urlopen('http://whereismypower.co.za/api/get_status.json')
##html = response.read()
##print(html.json())
