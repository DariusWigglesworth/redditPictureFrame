# redditPictureFrame
 Raspberry Pi run picture frame that gets pictures from reddit API daily and displays them
 
 Sends a get request to a certain reddit url to get data in .json format
 Data is then converted to a dictionary and then parsed for appropriate parameters
 These are by default that the post is not a video and not marked NSFW
 Posts meeting these critera are then added to the daily picutre array
 Throughout the day it goes through this array, displaying the picture from the url gotten from the .json
 After these are all done it loops
 
 To make modifications:
 
 To change the url, change url in requests.get("url")
 To change parameters, change the if statement within the for loop
