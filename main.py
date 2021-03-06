#Written by Darius Wigglesworth, ECE undergrad at UWaterloo
#Special thanks to Gilbert Chui for all his help

import json, requests
from time import sleep
import subprocess

sleepDuration = 600
dailyCats = [] #array that holds all 24 dicts of cat pictures for the day
#Different sites to exclude due to not displaying the picture the correct way in the browser
exclude1 = 'gif'
exclude2 = 'gfycat'
exclude3 = 'v.redd'
placeHolder = 1

while True:
    #Sends REST GET request to reddit to get the desired .json file and convert it to a dict to parse
    response = requests.get('https://www.reddit.com/user/frubbliness/m/cats/top/.json', headers = {'User-agent': 'Darius cat bot'})
    data = response.json()
    print('The HTTP response code was ', response)

    with open('data.txt', 'w') as outfile:      #Creates a file of the dict from json that it is using as data
        json.dump(data, outfile)

    #Loops through dict from reddit, sees if required parameters are met
    for i in data['data']['children']:
        #if requirements are met then it creates a temp dict with needed information and adds it to daily dict
        if i.get('data').get('over_18') == False and i.get('data').get('is_video') == False:
            #Checks to see if part of the url it found is an excluded one
            if exclude1 in i.get('data').get('url') or exclude2 in i.get('data').get('url') or exclude3 in i.get('data').get('url'):
                placeHolder += 1
                #Placeholder code because an error was caused if there wasn't any code there (C++ doesn't care)
                #Also works as a counter to show how many are itterated through and excluded
            else:
                dailyCats.append({'title':i.get('data').get('title'), 'url':i.get('data').get('url')}) #adds needed data into a dict, adding the dict to the daily array for later use
                #print(dailyCats) #prints array for debugging purposes

    with open('output.txt', 'w') as outfile:    #Create and outfile for easier debugging
        json.dump(dailyCats, outfile)

    print('dict created and appended') #For debugging
    
    #The followingis the display using Popen in subprocess
    i = 0
    while i < 5:
        for item in dailyCats:
            for key in item:
                if key == 'url':
                    p = subprocess.Popen(['chromium-browser', item[key], '--start-fullscreen']) #Create subprocess to open browser at url
                    sleep(sleepDuration)   #Sleep 30s for testing purposes
                    p.terminate() #kill browser
        i += 1