 # Reddit Picture Frame
 Automatic digital picture frame that gets pictures from reddit through .json data daily and displays them on the screen of the raspberry pi.
 
 ## Prerequisites 
 Requires PILLOW for the picture display
 
 ## Description
 Sends a get request to a certain reddit url to get data in .json format. Then, data is then converted to a dictionary and then parsed for appropriate parameters. These are by default that the post is not a video and not marked "Not Safe for Work" (NSFW). Posts meeting these critera are then added to the daily picutre array. Throughout the day it goes through this array, displaying the picture from the url gotten from the .json. After these are all done it loops
 
 ## Modifications
 To change the url to that of a different subreddit, change url in requests.get("url")
 To change parameters for the pictures or videos, change the if statement within the for loop
