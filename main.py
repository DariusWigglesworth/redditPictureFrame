#First phase
#GET top 100 from past 24 hours in .JSON format
#Parse out non-pictures
#Parse out everything remaining below 24th
#Sleep 1 hour, display next using JSON data

#json data order: over_18, url, is_video

import json, requests
from time import sleep

sleepDuration = 3600
dailyCatDict = {}
tempDict = {}
isOver18 = False
isVideo = False

#while True:

    #if midnight parse
response = requests.get('https://www.reddit.com/r/Catloaf/top/.json?sort=top&t=day', headers = {'User-agent': 'Darius cat bot'})
print('The HTTP response code was ', response)
data = response.json()

for i in data['data']['children']:
    for j in i:
        if j == 'over_18' and i[j] == 'false':
            isOver18 = False
        elif j == 'is_video' and i[j] == 'true':
            isVideo = True
            
    if (isOver18 == False) and (isVideo == False):
        tempDict = {
            #'title': data['data']['children'][i]['title'],
            #'url': data['data']['children'][i]['url'],
            'title': i['title'],
            'url': i['url'],
        }
        print('entered here')
    dailyCatDict.update(tempDict)
    isOver18 = True
    isVideo = False
        
    
with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)

with open('output.txt', 'w') as outfile:
    json.dump(dailyCatDict, outfile)

    #else display
