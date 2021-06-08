import requests
import math
import json
userId = int(input("Start ID: "))
Stop = int(input("End ID: "))



def find():
   global userId
   global Stop
   while userId <= Stop:
           r = requests.get(f"https://users.roblox.com/v1/users/{userId}").json()
           userId += 1
           print("{name}".format(**r))
           print("{name}".format(**r), file=open("output.txt", "a"))





a = None
while a is None:
   try:
       find()
   except:
        pass
