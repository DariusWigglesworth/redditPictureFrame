#Written by Darius Wigglesworth, ECE undergrad at UWaterloo
#Special thanks to Gilbert Chui for all his help with Python dicts

#First Phase
#Get top 100 from past 24 hours in .json format
#Parse out non pictures
#parse out everything remaining before 24th
#Display pic, sleep next hour, display next from json data

#json data order: over_18, url, is_video

import json, requests
from time import sleep

sleepDuration = 3600
dailyCatDict = {}      #Dict with all other temp dicts that will be appended, to be used throughout the day
tempDict = {}   #Create a temp dict to hold the necessary parts if it fits criteria

#while True:
    #if midnight parse

#Sends REST GET request to reddit to get the desired .json file and convert it to a dict to parse
response = requests.get('https://www.reddit.com/r/Catloaf/top/.json?sort=top&t=day', headers = {'User-agent': 'Darius cat bot'})
data = response.json()
print('The HTTP response code was ', response)


#Loops through dict from reddit, sees if required parameters are met
for i in data['data']['children']:
    print('The is_video data is ', i.get('data').get('is_video'))
    #if requirements are met then it creates a temp dict with needed information and adds it to daily dict
    if i.get('data').get('over_18') == False and i.get('data').get('is_video') == False:
        tempDict['title'] = i.get('data').get('title')
        tempDict['url'] = i.get('data').get('url')
        dailyCatDict.update(tempDict)
        print(tempDict)

with open('data.txt', 'w') as outfile:      #Creates a file of the dict from json that it is using as data
    json.dump(data, outfile)

with open('output.txt', 'w') as outfile:    #Create and outfile for easier debugging
    json.dump(dailyCatDict, outfile)

#else display
