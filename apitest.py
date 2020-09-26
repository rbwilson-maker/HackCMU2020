#this file takes data from a covid api and returns the amt of active cases in the state

import requests

r = requests.get(' https://api.covidtracking.com/v1/states/pa/current.json')
d = r.json()
positive = d['positive']
recovered = d['recovered']
active = positive - recovered

print(positive)
print(recovered)
print("the active amount of cases in PA is: " + str(active) )
