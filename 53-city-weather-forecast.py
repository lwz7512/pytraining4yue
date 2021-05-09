# Python program to forecast 5 days of
# weather details of any city 
# using openweathermap api 

# import required modules 
import requests, json 

# Enter your API key here 
api_key = ""

# base_url variable to store url 
base_url = "http://api.openweathermap.org/data/2.5/forecast?"

# Give city name 
city_name = input("Enter city name : ") 

print(">>> loading forecast data for city {0}...".format(city_name))

# complete_url variable to store 
# complete url address 
complete_url = base_url + "appid=" + api_key + "&q=" + city_name
print(">>> complete url: {0}".format(complete_url))

# get method of requests module 
# return response object 
response = requests.get(complete_url) 

# json method of response object 
# convert json format data into 
# python format data 
resp = response.json()

if resp["cod"] == 401:
  print(resp["message"])

print("--------------------------------")

# Now x contains list of nested dictionaries 
# Check the value of "cod" key is equal to 
# "404", means city is found otherwise, 
# city is not found 
if resp["cod"] != 404 and resp["cod"] != 401 : 
  results = resp["list"]
  for day in results:
    print(day["dt_txt"])
    print("  Weather    : " + day["weather"][0]["description"])
    print("  Weather main: " + day["weather"][0]["main"])
    print("  Temperature: " + str(round(day["main"]["temp"] - 272, 2)))
    print("  Humitidy   : " + str(day["main"]["humidity"]))
    print("----------------------")
else: 
	print(" City Not Found ") 
