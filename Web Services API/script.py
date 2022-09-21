import requests

london = "london?nTqu&lang=en"
svo = "svo?nTqu&lang=en"
cherepovets = "Череповец?MnTq&lang=ru"
list_cities = [london, svo, cherepovets]

for city in list_cities:
    requests.get("https://wttr.in/{}".format(city)).raise_for_status()
    print(requests.get("https://wttr.in/{}".format(city)).text)
