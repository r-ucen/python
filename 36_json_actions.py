import json

# string representation of dict or list
my_dict = {"data":
           {"car":"Skoda",
            "parameters":[1,1.415,(1,1),"automatic",True]}}
print(my_dict)

# string representation of dict or list (dumps)
json_dict = json.dumps(my_dict)
print(json_dict)

# # loading back (loads)
dict_again = json.loads(json_dict)
print(dict_again)

#       -----------------

with open("examples/exampleJSON.json","r") as json_file:
    my_dict = json.load(json_file)

print(my_dict)
#my_dict['weather'][0]['id'] # 501

'''
{'coord': {'lon': 10.99, 'lat': 44.34}, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'base': 'stations', 'main': {'temp': 298.48, 'feels_like': 298.74, 'temp_min': 297.56, 'temp_max': 300.05, 'pressure': 1015, 'humidity': 64, 'sea_level': 1015, 'grnd_level': 933}, 'visibility': 10000, 'wind': {'speed': 0.62, 'deg': 349, 'gust': 1.18}, 'rain': {'1h': 3.16}, 'clouds': {'all': 100}, 'dt': 1661870592, 'sys': {'type': 2, 'id': 2075663, 'country': 'IT', 'sunrise': 1661834187, 'sunset': 1661882248}, 'timezone': 7200, 'id': 3163858, 'name': 'Zocca', 'cod': 200}
'''

# if we have a dictionary and want to save this dictionary into a json file:

data = {
    "car": {
        "model": "Octavia",
        "make": "Skoda"
    }
}

with open("examples/myfile.json","w") as json_file:
    json.dump(data,json_file)

