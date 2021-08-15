'''https://ghrc.nsstc.nasa.gov/hydro/es_proxy.php?esurl=_sql?sql=SELECT * from ghrc limit 1
   https://ghrc.nsstc.nasa.gov/hydro/es_proxy.php?esurl=_sql?sql=SELECT * from ghrc_inv'''

#Create a Python application to query the API and populate the data
import requests,json
headers = {
 'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)     Chrome/37.0.2049.0 Safari/537.36'
}

url1 = requests.get('https://ghrc.nsstc.nasa.gov/hydro/es_proxy.php?esurl=_sql?sql=SELECT * from ghrc limit 1', headers=headers)
url1_response = url1.json()
#print('url1response',url1_response)

url2 = requests.get('https://ghrc.nsstc.nasa.gov/hydro/es_proxy.php?esurl=_sql?sql=SELECT * from ghrc_inv', headers=headers)
url2_response = url2.json()
#print('url2response',url2_response)

'''Extract these variables for all datasets:
ds_short_name
'''

x = 0
try:
  while True:
    print(url2_response["hits"]["hits"][x]["_source"]["ds_short_name"])
    x = x+1
except:
  print("end of json file")

x = 0
try:
  while True:
    print(url2_response["hits"]["hits"][x]["_source"]["start_date"])
    x = x+1
except:
  print("end of json file")

x = 0
try:
  while True:
    print(url2_response["hits"]["hits"][x]["_source"]["stop_date"])
    x = x+1
except:
  print("end of json file")

x = 0
try:
  while True:
    print(url2_response["hits"]["hits"][x]["_source"]["format"])
    x = x+1
except:
  print("end of json file")

x = 0
try:
  while True:
    print(url2_response["hits"]["hits"][x]["_source"]["granule_name"])
    x = x+1
except:
  print("end of json file")

x = 0
try:
  while True:
    print(url2_response["hits"]["hits"][x]["_source"]["dataset_name"])
    x = x+1
except:
  print("end of json file")

x = 0
try:
  while True:
    print(url2_response["hits"]["hits"][x]["_source"]["data_access"])
    x = x+1
except:
  print("end of json file")

x = 0
try:
  while True:
    print(url2_response["hits"]["hits"][x]["_source"]["checksum"])
    x = x+1
except:
  print("end of json file")

x = 0
try:
  while True:
    print(url2_response["hits"]["hits"][x]["_source"]["file_size"])
    x = x+1
except:
  print("end of json file")