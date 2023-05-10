# -*- coding: utf-8 -*-

# -- Sheet --

d={
  "lat": 39.31,
  "lon": -74.5,
  "timezone": "America/New_York",
  "timezone_offset": -18000,
  "current": {
    "dt": 1646318698,
    "sunrise": 1646306882,
    "sunset": 1646347929,
    "temp": 282.21,
    "feels_like": 278.41,
    "pressure": 1014,
    "humidity": 65,
    "dew_point": 275.99,
    "uvi": 2.55,
    "clouds": 40,
    "visibility": 10000,
    "wind_speed": 8.75,
    "wind_deg": 360,
    "wind_gust": 13.89},
    "weather": {
        "id": 802,
        "main": "Clouds"}}

# # How would you access the value of "lat" from the dictionary?


d['lat']

# # How would you access the value of "timezone_offset" from the dictionary?


d['timezone_offset']

# # How would you access the value of "feels_like" from the "current" key?


d["current"]["feels_like"]

# # How would you access the value of "weather" from the "current" key?


d["weather"]

# # How would you access the value of "id" from the first element of the "weather" key?


d["weather"]['id']

# # How would you access the value of "main" from the first element of the "weather" key?


d["weather"]['main']

# # How would you change the value of "humidity" to 70?


d['current']['humidity']=70
d['current']['humidity']

# # How would you add a new key-value pair to the dictionary with key "country" and value "USA"?


d['country']='usa'
d

# # How would you delete the "visibility" key from the "current" key?


d={
  "lat": 39.31,
  "lon": -74.5,
  "timezone": "America/New_York",
  "timezone_offset": -18000,
  "current": {
    "dt": 1646318698,
    "sunrise": 1646306882,
    "sunset": 1646347929,
    "temp": 282.21,
    "feels_like": 278.41,
    "pressure": 1014,
    "humidity": 65,
    "dew_point": 275.99,
    "uvi": 2.55,
    "clouds": 40,
    "visibility": 10000,
    "wind_speed": 8.75,
    "wind_deg": 360,
    "wind_gust": 13.89},
    "weather": {
        "id": 802,
        "main": "Clouds"}}

del d["current"]["visibility"]
print(d)

# # How would you check if the key "pressure" is in the "current" key?


for i in d["current"]:
    if "pressure" in d["current"]:
        print(True)
        break
    else:
        print(False)

# # How would you check if the key "state" is in the dictionary?


for i in d:
    if "state" in d:
        print(True)
        break
    else:
        print(False)

# # How would you loop through all the keys in the dictionary?


for keys in d:
    print(keys)

# # How would you loop through all the values in the dictionary?


for values in d :
   print(d[values])

# # How would you loop through all the key-value pairs in the dictionary?


for values in d :
   print(i,d[values])

# # How would you convert the dictionary to a JSON string?


d_json=json.dumps(d)
d_json.

# # How would you convert the JSON string back to a Python dictionary?


json.loads(j)

# # How would you get a list of all the keys in the dictionary?


# l=[]
# for keys in (d):
#     l.append(keys)

# print(l)

list(d.keys())

# # How would you get a list of all the values in the dictionary?


print(list(d.values()))

# # How would you get the number of key-value pairs in the dictionary?


d


count=0
for keys, values in d.items():
    count+=1
    value= i

print(count)

# # How would you sort the key-value pairs in the dictionary by the value of the "dt" key in the "current" key?


sorted(d)



