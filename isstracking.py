import json 
import turtle 
import urllib.request
import time 
import webbrowser
import geocoder

url = "http://api.open-notify.org/astros.json" #api for counting astronauts 
response = urllib.request.urlopen(url)
result = json.loads(response.read())
file = open("iss.txt", "w")
# file.write("There are currently" + 
#            str (result["number"]) + "astronatus on the ISS: \n\n")
print("There are currently " + str (result["number"]) + " astronatus on the ISS: \n ")

people = result['people']

for p in people:
    # file.write(p ['name'] + " - on board" + "\n")
    print(p ['name'] + " - on board" + "")
print(" ")

# printing long and lat
g = geocoder.ip('me')
# file.write("\n Your current lat / long is: " + str(g.latlng))
print("Your current lat / long is: " + str(g.latlng))
file.close()
# webbrowser.open("iss.txt")

screen = turtle.Screen()
screen.setup(1280, 720)
screen.setworldcoordinates(-180,-90,180,90)

#load the world map image
screen.bgpic("Map.gif")
screen.register_shape("iss-icon.gif")
iss = turtle.Turtle()
iss.shape("iss-icon.gif")
iss.setheading(45)
iss.penup()

# input('stop')

while True:
    
    url  ="http://api.open-notify.org/iss-now.json"
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())
    
    # extracting the iss
    location = result["iss_position"]
    lat = location['latitude']
    lon = location['longitude']
    
    # output 
    lat = float(lat)
    lon = float(lon)
    print("\nLatitude: " + str(lat))
    print("\nLongitude: " + str(lon))
    
    # update 
    iss.goto(lon,lat)
    
    # refresh each 5 secs
    time.sleep(5)

    