# Python program to find current 
# weather details of any city 
# using openweathermap api 

# import required modules 
import requests, json 

# Enter your API key here 
api_key = ""

# base_url variable to store url 
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Give city name 
city_name = input("Enter city name : ") 

print(">>> loading today weather for city {0} ...".format(city_name))

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
x = response.json()

if x["cod"] == 401:
  print(x["message"])

print("--------------------------------")

# Now x contains list of nested dictionaries 
# Check the value of "cod" key is equal to 
# "404", means city is found otherwise, 
# city is not found 
if x["cod"] != 404 and x["cod"] != 401 : 

	# store the value of "main" 
	# key in variable y 
	y = x["main"] 

	# store the value corresponding 
	# to the "temp" key of y 
	current_temperature = y["temp"] 

	# store the value corresponding 
	# to the "pressure" key of y 
	current_pressure = y["pressure"] 

	# store the value corresponding 
	# to the "humidity" key of y 
	current_humidiy = y["humidity"] 

	# store the value of "weather" 
	# key in variable z 
	z = x["weather"] 

	# store the value corresponding 
	# to the "description" key at 
	# the 0th index of z 
	weather_description = z[0]["description"] 

	# print following values 
	print(
    " Temperatrue in Celsius degree : " + 
          str(round(current_temperature - 272.15, 2)) +
		"\n Atmospheric pressure (in hPa unit) : " +
					str(current_pressure) +
		"\n Humidity (in percentage) : " +
					str(current_humidiy) +
		"\n Description : " +
					str(weather_description) +
    "\n"
  ) 

else: 
	print(" City Not Found ") 
