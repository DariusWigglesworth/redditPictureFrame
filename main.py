#First Phase
#Get top 100 from past 24 hours in .json format
#Parse out non pictures
#parse out everything remaining before 24th
#Display pic, sleep next hour, display next from json data

#json data order: over_18, url, is_video

import json, requests
from time import sleep

sleepDuration = 3600
dailyCatDict = {}
tempDict = {}

#while True:
    #if midnight parse
response = requests.get('https://www.reddit.com/r/Catloaf/top/.json?sort=top&t=day', headers = {'User-agent': 'Darius cat bot'})
data = response.json()
print('The HTTP response code was ', response)

for i in data['data']['children']:
    print('The is_video data is ', i.get('data').get('is_video'))
    if i.get('data').get('over_18') == False and i.get('data').get('is_video') == False:
        tempDict['title'] = i.get('data').get('title')
        tempDict['url'] = i.get('data').get('url')
        dailyCatDict.update(tempDict)
        print(tempDict)

with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)

with open('output.txt', 'w') as outfile:
    json.dump(dailyCatDict, outfile)

#else display
