 # Reddit Picture Frame
 Automatic digital picture frame that gets pictures from reddit through .json data daily and displays them on the screen of the raspberry pi.
 
 ## Prerequisites 
 The current itteration requires no additional libraries or software to run. All code tested and run on Python 3 IDLE on a Raspberry Pi 3 Model B
 
 ## Description
 Sends a get request to a certain reddit url to get data in .json format. Then, data is then converted to a dictionary and then parsed for appropriate parameters. These are by default that the post is not a video and not marked "Not Safe for Work" (NSFW). Posts meeting these critera are then added to the daily picutre array. Throughout the day it goes through this array, displaying the picture from the url gotten from the .json for a duration of 10 minutes. After it has gone through all pictures in the array it loops through the whole array 4  more times (5 times total).
 
 The assumption is that there will be 18-24 pictures in the array, and displaying each for 10min allows it to display 6 per hour. Once this is done it will get a new set of pictures, roughly every 15-20 hours.
 
 The pictures are displayed using the Chromium browser in fullscreen mode, using only certain sites so that it only displays the picture.
 
 ## Modifications
 To change the url to that of a different subreddit, change url in requests.get("url")
 To change parameters for the pictures or videos, change the if statement within the for loop
