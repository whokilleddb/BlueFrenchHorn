#!/bin/python3
#importing libraries
import random
import discord
import urllib.request
import re
import youtube_dl
from discord.ext import commands
import os
from discord.utils import get
from botfunctions import *
from itemlists import *

#Globals
TOKEN=""
CHANNEL_ID=int()
VERSION=2.0
client=discord.Client()
PREFIX="~"
#Functionality


@client.event
async def on_ready():
    general_channel=client.get_channel(CHANNEL_ID)
    await general_channel.send("Daddy's Home !")
    print("BOT IS LIVE !")
    print(f"Version : {VERSION}")

@client.event
async def on_member_join(member):
    general_channel=client.get_channel(CHANNEL_ID)
    guild=member.guild
    message ='Hi {}, we will teach you how to live....Barney , we met at the Urinal.\nGet A Suit ! Suits are cool. Exhibit "A" ;) ! '.format(member.mention)
    await general_channel.send(message)

@client.event
async def on_message(message):
    general_channel=client.get_channel(message.channel.category_id)
    ids = [member.id for member in message.guild.members]
    print(ids)
    auth_avatar=message.author.avatar_url_as(format='jpeg')
    print(auth_avatar)
    print(message.content)

    cmd=(message.content)[:1]
    if cmd[0]==PREFIX :
        mess=breakMess((message.content).lower())   
        print("Received Command : ", mess)
        
        #print(mess)
        if mess[1]=="help":
                my_embed = discord.Embed(title="All About Me", description="Lorenzo Von Matterhorn Is An Awesome Bot coded by the even more awesome @whokilleddb.\nHe likes to be called Bro.",color=0x00ff00)
                my_embed.add_field(name="Version:",value=VERSION,inline=False)
                my_embed.set_footer(text="Suit Up !")
                my_embed.set_author(name="WhoKilledDB")
                await message.channel.send(embed=my_embed)

        if mess[1]=="makemesad":
            await message.channel.send("Remember , You asked for this !")
            await message.channel.send(random.choice(himym))

        if mess[1]=="gay":
            if int(mess[0])==2 :
                if mess[2][2] != '!':
                    userid=int(mess[2][2:len(mess[2])-1])
                if mess[2][2] == '!':
                    userid=int(mess[2][3:len(mess[2])-1])
                print(f"User Tag : {userid}")
                user = client.get_user(userid)
                if not user:
                    print("User Not Found")
                else :
                    gayThis(user.avatar_url_as(format='jpeg',size=256))
                    await message.channel.send(file=discord.File("./gayed.jpeg"))
                    os.remove('./gayed.jpeg')
                    os.remove('./avatar.jpeg')

        if mess[1]=="capitalist":
            if int(mess[0])==2 :
                if mess[2][2] != '!':
                    userid=int(mess[2][2:len(mess[2])-1])
                if mess[2][2] == '!':
                    userid=int(mess[2][3:len(mess[2])-1])
                print(f"User Tag : {userid}")
                user = client.get_user(userid)
                if not user:
                    print("User Not Found")
                else :
                    capitalistThis(user.avatar_url_as(format='jpeg',size=256))
                    await message.channel.send(file=discord.File("./my.jpg"))
                    os.remove('./my.jpg')
                    os.remove('./avatar.jpeg')

        if mess[1][:5]=="there" :
                    if (random.randint(1,2))%2==0:
                        await message.channel.send("Yup")

                    else :
                        await message.channel.send("Always There For You :) <@{}>".format(message.author.id))
        
        if mess[1]=="quote":
            if int(mess[0])==1:
                await message.channel.send("Bro ! What do you even wanna know ? The Brocode or The Playbook ?")
            if int(mess[0])==3 or int(mess[0])==2 :
                if mess[2]=="playbook":
                    await message.channel.send(random.choice(playbook))
                if mess[2]=="brocode":
                    if ( int(mess[0])==3 and int(mess[3])>0 and int(mess[3])<=82 ):
                        await message.channel.send(brocode[int(mess[3]-1)])
                    else :
                        await message.channel.send(random.choice(brocode))
        
        if mess[1]=="meme":
            if int(mess[0])==1:
                lst=red(random.choice(subs))
                my_embed = discord.Embed(title=lst[0])
                my_embed.set_image(url=lst[1])
                await message.channel.send(embed=my_embed)
            else :
                lst=red(((message.content)[6:]).replace(" ", "") )
                em=discord.Embed(title=lst[0])
                em.set_image(url=lst[1])
                await message.channel.send(embed=em)
        
        if mess[1]=="join":
                channel=""
                print(channel)
                if (message.author.voice) != None:
                    channel=message.author.voice.channel
                    voice=get(client.voice_clients, guild=message.guild)
                    if voice and voice.is_connected():
                        await voice.move_to(channel)
                    else:
                        voice = await channel.connect()
                    await voice.disconnect()
                    if voice and voice.is_connected():
                        await voice.move_to(channel)
                        await  message.channel.send("I am in {} bitches".format(channel))
                    else:
                        voice = await channel.connect()
                        await  message.channel.send("I am in {} Voice bitches".format(channel))
                else :
                     await  message.channel.send("Bro You Need To Join A Voice Channel Yourself First !")
                    
        if mess[1]=="leave":
                voice=get(client.voice_clients, guild=message.guild)
                
                if voice and voice.is_connected():
                    await voice.disconnect()
                    VOICE_FLAG=False
                    await message.channel.send(f"Imma Ight Head Out Of Voice")
                else:
                    voice = await  message.channel.send("Bruh am not even in a Voice Channel !")
        
        if mess[1]=="joke":
                await message.channel.send(joke())
                                
        if mess[1]=="play":
            voice=get(client.voice_clients, guild=message.guild)
            if (message.author.voice) == None:
                await  message.channel.send("Bruh You Are not even in a Voice Channel !")
                await  message.channel.send("Add Yourself In First")
            else :
                if not (voice and voice.is_connected()):
                    channel=message.author.voice.channel
                    voice=get(client.voice_clients, guild=message.guild)
                    if voice and voice.is_connected():
                        await voice.move_to(channel)
                    else:
                        voice = await channel.connect()
                    await voice.disconnect()
                    
                    if voice and voice.is_connected():
                        await voice.move_to(channel)
                        await  message.channel.send("I Let Myself In That Voice Channel ")
                    else:
                        voice = await channel.connect()
                        await  message.channel.send("I Helped Myself In")
                
                if int(mess[0])>2 and not mess[3].isnumeric():
                    str1=(message.content[6:]).replace(" ","+")
                elif int(mess[0])==1:
                    str1="NeverGonnaGiveYouUp"
                else :
                    str1=mess[2]
                name=""
                song_there=os.path.isfile("song.mp3")
                try:
                    if song_there:
                        os.remove("song.mp3")
                        print("Removed Song File")
                except PermissionError:
                    print("The Song Is On")
                    await message.channel.send("Bro I think the song is already playing !")
                    return

                await message.channel.send("Firing That Up Now !")

                voice = get(client.voice_clients, guild=message.guild)
                ydl_opts={
                    'format': 'bestaudio/best',
                    'postprocessors':[{
                        'key':'FFmpegExtractAudio',
                        'preferredcodec':'mp3',
                        'preferredquality':'192',
                    }],
                }
                    
                if int(mess[0])==3 and mess[3].isnumeric():
                    v_url=searchQuery(str1,int(mess[3]))
                else :
                    v_url=searchQuery(str1,0)

                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    print("Downloading Song")
                    ydl.download([v_url])

                for file in os.listdir("./"):
                    if file.endswith(".mp3"):
                        name=file
                        print(f"Renamed File {file}")
                        os.rename(file,"song.mp3")
                try:
                    voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: print("Vibing"))
                    voice.souce=discord.PCMVolumeTransformer(voice.source)
                    voice.souce.volume=0.07
                    await message.channel.send(f"Playing {v_url}")
                except ClientException:
                    await message.channel.send("Looks like I am out of the voice channel !")
                    if (message.author.voice) != None:
                        channel=message.author.voice.channel
                        voice=get(client.voice_clients, guild=message.guild)
                        if voice and voice.is_connected():
                            await voice.move_to(channel)
                        else:
                            voice = await channel.connect()
                        await voice.disconnect()
                        if voice and voice.is_connected():
                            await voice.move_to(channel)
                            await  message.channel.send("I am back in {} bitches".format(channel))
                        else:
                            voice = await channel.connect()
                            await  message.channel.send("I am back in {} Voice bitches".format(channel))
                        await message.channel.send("Let Me Play That Again !")
                        await message.channel.send(f"~play {(message.content)[6:]}")   
                    else :
                         await  message.channel.send("Bro You Need To Join A Voice Channel As Well!")

client.run(TOKEN)
