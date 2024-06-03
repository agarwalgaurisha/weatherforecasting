import requests
import json
import pyttsx3

engine = pyttsx3.init()

engine.say("welcome to weatherforecasting application")
engine.runAndWait()
city = input("enter your city")
url = f"https://api.weatherapi.com/v1/current.json?key=086e02960a374c7892c73933240306&q={city}"
r = requests.get(url)

wdic=json.loads(r.text)
m=wdic["location"]["region"]
engine.say(f"the region of the {city} is {m}")
engine.runAndWait()

print(wdic["location"]["region"])
n=wdic["current"]["temp_c"]
engine.say(f"the temperature of the {city} is {n}")
engine.runAndWait()

print(wdic["current"]["temp_c"])

engine.say("thanks for using the weatherforecasting application")
engine.runAndWait()
