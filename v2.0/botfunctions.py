import json
import random
import urllib.request
import re
import youtube_dl
import os
import praw
import requests
from PIL import Image, ImageDraw, ImageFilter

#MUSIC_MATCH_API_KEY=""

def searchQuery(str,num):
    html=urllib.request.urlopen(f"https://youtube.com/results?search_query={str}")
    video_id=re.findall(r"watch\?v=(\S{11})",html.read().decode())
    for i in range(len(video_id)):
        video_id[i]=f"https://www.youtube.com/watch?v={video_id[i]}"
    return(video_id[num])

def breakMess(str):
    arr=str.split(" ")
    l=len(arr)
    arr.insert(0,l)
    arr[1]=arr[1][1:]
    return arr

def red(subr):
    id=""
    secret=""
    uname=""
    passw=""
    res=[]
    reddit=praw.Reddit(client_id=id,client_secret=secret,username=uname,password=passw,user_agent="")
    subreddit=reddit.subreddit(subr)
    all_subs=[]
    top=subreddit.top(limit=5)
    for submission in top:
        all_subs.append(submission)
    random_sub=random.choice(all_subs)
    res.append(random_sub.title)
    res.append(random_sub.url)
    return res

def joke():   
    url="https://sv443.net/jokeapi/v2/joke/Any?format=txt"
    response = requests.request("GET", url)
    joke=response.text
    arr=joke.split('\n')
    i=0
    ftext=""
    while i<len(arr):
        if arr[i]!="":
            ftext=arr[i]+'\n'
        i=i+1
    return ftext

def downloadImage(filename,url):
    r=requests.get(url, allow_redirects=True)
    print("Downloading Image")
    open (filename,'wb').write(r.content)

def changeImageSize(maxWidth,maxHeight,image):
    widthRatio  = maxWidth/image.size[0]
    heightRatio = maxHeight/image.size[1]

    newWidth    = int(widthRatio*image.size[0])
    newHeight   = int(heightRatio*image.size[1])

    newImage    = image.resize((newWidth, newHeight))
    return newImage
  
def gayThis(url):
    downloadImage("avatar.jpeg",url)
    Av=Image.open("./avatar.jpeg")
    gFlag=Image.open("./pride.jpeg")
    print("Resized Image")
    Image.blend(Av,gFlag,0.5).save('./gayed.jpeg',quality=95)

def capitalistThis(url):
    downloadImage("avatar.jpeg",url)
    Av=Image.open("./avatar.jpeg")
    gFlag=Image.open("./capitalist.jpg")
    print("Resized Image")
    Image.blend(Av,gFlag,0.5).save('./my.jpg',quality=95)

