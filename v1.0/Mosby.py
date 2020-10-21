#!/bin/python3
import random
import discord
import urllib.request
import re
import youtube_dl
from discord.ext import commands
import os
from discord.utils import get

#Globals
TOKEN=""
CHANNEL_ID=0000000


#Client aka our Bot
client=commands.Bot(command_prefix='--')

#functions
def searchQuery(str,num):
    html=urllib.request.urlopen(f"https://youtube.com/results?search_query={str}")
    video_id=re.findall(r"watch\?v=(\S{11})",html.read().decode())
    for i in range(len(video_id)):
        video_id[i]=f"https://www.youtube.com/watch?v={video_id[i]}"
    return(video_id[num])

def isWord(lst,wrd):
    fg=False
    for i in range(len(lst)):
        if lst[i]==wrd :
            fg=True
    return fg


#Lists
himym=["https://youtu.be/MYnhPtsRQjA", "https://youtu.be/v73s7SCWzvs","https://youtu.be/HpLsYgXpIws","https://youtu.be/xWa-QVAd7gM","https://youtu.be/zwYOXsb7FbI","https://youtu.be/UImXzJsId2w","https://youtu.be/Dcngel9VyIU","https://youtu.be/fiuu245RpwQ","https://youtu.be/8Bw5Z0rBteY","https://youtu.be/I90B8tQ9qRA","https://youtu.be/yvXIpvh9hvI","https://youtu.be/6b2AGAB2pA0"]

brocode=['Article I : Bros before hoes.',
'Article II : A bro is always entitled to do something stupid as long as the rest of his bros are all doing it.',
'Article III : If a bro gets a dog, it must be at least as tall as his knee when full grown.\nCorollary: Naming a lap dog after a pro wrestler or character from an action flick does not absolve said bro from this article.',
'Article IV : A bro never divulges the existence of the bro code to a woman. It is a sacred document not to be shared with chicks for any reason. No, not even that reason.\nNote:\nIf you are a woman reading this, first, let me apologize: it was never my intention for this book to contain so much math.\nSecond, I urge you to look at this document for what it is – a piece of fiction meant to entertain a broad audience though the prism if stereotypical gender differences. I mean, sometimes it really is like we’re from different planets! Clearly, no real person would actually believe or adhere to the vulgar rules contained within. *Those boots are adorable, b-t-dub.',
'Article V : Whether a bro cares about sports or not, a bro cares about sports.',
'Article VI : A bro shall not lollygag if he must get naked in front of other bros, such as in a gym locker room. Corollary: If a bro gets naked in a locker room all other bros shall pretend that nothing out of the ordinary is happening, while at the same time immediately averting their eyes. When in doubt, remember the old adage, if a towel drops to the floor, so should your eyes.',
"""
Article VII : A bro never sends a greeting card to another bro.

EMAILS FOR ANY BROCASSION:

SYMPATHY
To: Bro
From: Bro
Subject: Dude

Sorry, Bro.
----------------------------------

CONGRATULATIONS
To: Bro
From: Bro
Subject: Bro!

Nice, Bro!
----------------------------------

GET WELL SOON
To: Bro
From: Bro
Subject: Bro…

Don’t give up, Bro.
----------------------------------

HAPPY BIRTHDAY
To: Bro
From: Bro
Subject: Dude

Drinks on me, Bro.
----------------------------------

THINKING OF YOU
To: N/A
From: N/A
Subject: N/A

N/A
----------------------------------
""",
'Article VIII : A bro never admits he can’t drive stick, even after an accident.',
'Article IX : Should a Bro lose a body part due to an accident or illness, his fellow Bros will not make lame jokes such as “Gimme three!” or “Wowm quitting your job like that really took a lot of ball”. It’s still a high five and that Bro still has a lot of balls… metaphorically speaking, of course',
"""
Article X : A Bro will drop whatever he’s doing and rush to help his Bro dump a chick

It’s normal for a Bro to get confused and disorientated when dumping a chick. For some reason he’s worried she’ll become agitated or even violent after he calmly explains his desire to have sex with her friends. This is when a Bro most needs his Bro to remind him that there are plenty more chicks in the ocean, and that a breakup need not be hazardous, stressful, or even time-consuming.

SIDE-BRO: HOW TO DUMP A CHICK IN SIX WORDS OR LESS

“Maybe try a side salad instead”
“Cute! You’re growing a mustache, too!”
“She looks like a younger you”
“I will finance a boob job”
“Sorry I threw out your shoes”
“Your sister let me do that”
""",
"Article XI : A Bro may ask his Bro(s) to help him move, but only after first disclosing an honest estimate on both time commitment and number of large pieces of furniture. If the Bro has vastly underestimated either, his Bros retain the right to leave his possessions where they are – in most cases, stuck in the doorway.",
'Article XII : Bros do not share desert.', 'Article XIII : All bros shall dub one of their bros their wingman.', 'Article XIV : If a chick inquires about a bros sexual history, a bro shall honor the ‘Brode of Silence’ and play dumb. Better to have women think all men are dumb than to tell the truth.', 'Article XV : A bro never dances with his hands above his head.', 'Article XVI : A bro should be able to at any time recite the following reigning champions: Super Bowl and World Series.', 'Article XVII : A bro shall be kind and courteous to his coworkers, unless they are beneath him on the pyramid of screaming.', 'Article XVIII : If a bro spearheads a beverage run, he is entitled to any extra money accrued after canvassing the group.', 'Article XIX : A bro shall not sleep with another bro’s sister. However, a bro shall not get angry if another bro says “dude, your sister’s hot!”. Corollary: it’s probably better for everyone if bros just hide pictures of their sister/s when other bros are coming over.', 'Article XX : A bro respects his bros in the military because they have chosen to defend the nation, but more to the point because they can kick his @/$ six ways to Sunday.', 'Article XXI : A bro never exchanges notes about an antithetical bro’s smoking hot girlfriend, even if the bro with the hot girlfriend attempts to bait the bro by saying “She’s hot, huh?”. A bro shall remain silent on the subject because, in this situation, he should be the only one bateing.', 'Article XXII : There is no law that prohibits a woman from being a bro.', 'Article XXIII : When flipping through channels with his bros, a bro is not allowed to skip past a program featuring sports.', 'Article XXIV : When wearing a baseball cap, a bro way position the brim at either twelve or six o’clock. All other angles are reserved for rappers and the handicapped. If a bro fits under either of these classifications, he is excused from this article.', 'Article XXV : A bro doesn’t let another bro get a tattoo. Including but not limited to a girls name or tramp stamp.', 'Article XXVI : Unless he has children, a bro shall not wear his cellphone on a belt clip.', 'Article XXVII : A bro never removes his shirt in front of another bro unless at a resort, pool, or beach.', 'Article XXVIII : A bro will, in a timely manner, alert his bro to the existence of a girl fight.', 'Article XXIX : If two bros decide to catch a movie together, they may not attend a screening that begins after 4:40 PM. Also, despite cost saving, they shall not share a tub of popcorn.', 'Article XXX : A bro doesn’t comparison shop.', 'Article XXXI : When on the prowl, a bro hits on the hottest girl first because you just never know.', 'Article XXXII : A bro doesn’t allow another bro to get married until he is at least 30.', 'Article XXXIII : When in a public restroom, a bro:\n1.) looks straight ahead while using the urinal,\n2.) makes the obligatory comment ‘what is this, a chick’s restroom?’ if there are more than two dudes waiting to pee, and\n3.) Attempts to basketball toss his used paper towels into the trash can (rebounding is optional).', 'Article XXXIV : Bros cannot make eye contact during a devil’s three way (two dudes).', 'Article XXXV : A bro never rents a chick flick.', 'Article XXXVI : When questioned in the company of women, a bro always decries fake breasts.', 'Article XXXVII : A bro is under no obligation to open a door for anyone.', 'Article XXXVIII : Even in a fight to the death, a bro never punches another bro in the groin.', 'Article XXXIX : When a bro gets a chick’s number, he waits at least 96 hours before calling her.', 'Article XL : Should a bro become stricken with engagement, his bros shall stage an intervention and attempt to heal him.', 'Article XLI : A bro never cries. Exceptions: watching Field of Dreams, ET, or a sports legend retire.', 'Article XLII : Upon greeting another bro, a bro may engage a high five, fist bump, or bro hug, but never a full embrace.', 'Article XLIII : A bro loves his country, unless that country isn’t America.', 'Article XLIV : A bro never applies sunscreen on another bro.', 'Article XLV : A bro never wears jeans to a strip club.',
"""Article XLVI : If a bro is seated next to some dude stuck in the middle seat on an airplane, he shall yield him all of their shared armrests unless the dude has:
A) Taken his shoes off
B) Is snoring
C) Makes the bro get up more than once to use the lavatory
D) Purchased headphones after they announced the in flight movie is 27 dresses.""", 'Article XLVII : A bro never wears pink. Corollary: when wearing a shirt to save the boobs.', 'Article XLVIII : A bro never publicly reveals how many chicks he or another bro has banged.', 'Article IL : When asked ‘do you need help’ a bro automatically responds with ‘no’. Exceptions: when involving and expensive car or TV.', 'Article L : If a bro should accidentally stroke another bro’s undercarriage with his arm while walking, both bros silently agree to continue walking as if it never happened.', 'Article LI : A bro checks out another bro’s blind date and reports back with a thumbs up or thumbs down.', 'Article LII : A bro is not required to remember another bro’s birthday.', 'Article LIII : Even in a drought, a bro flushes.', 'Article LIV : A bro is required to go out with his bros on St. Party’s day and other official bro holidays.', 'Article LV : Even in an emergency that requires a tourniquet, a bro never borrows from or lends clothes to another bro.', 'Article LVI : A bro is required to alert one and only one bro if the bro-chick ratio at a party falls below 1:1', 'Article LVII : A bro never reveals to score of a sporting event to a bro unless that bro has thrice confirmed he wants to hear it.', 'Article LVIII : A bro doesn’t grow a mustache.', 'Article LIX : A bro always posts bail for another bro unless its out if state or like crazy expensive.', 'Article LX : A bro shall honor thy mother and father for they were once bro and chick. However, a bro never thinks of his parents as bro and chick.', 'Article LXI : If for any reason a bro becomes aware of a bro and chick’s anniversary he will endeavor to make this information to the bro in the relationship whether the first bro thinks the second bro is aware of this or not.', 'Article LXII : In the event that two bros lock on to the same target, the bro who calls dubs first has dibs.', 'Article LXIII : A bro will make any and all efforts to provide his bro with protection.', 'Article LXIV : A bro must provide must provide a ticket to an event he is attending if said event involves the second bro’s favorite sports team in a playoff scenario.', 'Article LXV : A bro must always reciprocate a round of drinks among bros.', 'Article LXVI : If a bro suffers pain due to the permanent dissolution of a relationship with his lady friend, his bros shall offer no more than an ‘aw, that sucks man.’ And copious quantities of a preferred beverage.', 'Article LXVII : Should a bro pick up a guitar at a party and begin to play, another bro shall point out that he is a tool.', 'Article LXVIII : If a bro is on a ‘hot streak’ another bro will do anything he can to ensure its longevity, even if that includes jeopardizing his own records, the missing of work, or generating the imminent fear the world will soon end. Exception: Dry spell trumps hot streak.', 'Article LXIX : Duh.', 'Article LXX : A bro will drive another bro to the airport or pick him up, but never both for the same trip.', 'Article LXXI : As a courtesy to bros the world over, a bro never brings more than two other bros to a party.', 'Article LXXII : A bro never spellchecks.', 'Article LXXIII : When a group of bros are in a restaurant, each shall engage in jockeying the bill, regardless of affordability.', 'Article LXXIV : At a red light, a bro inches as close to the rear bumper of the car in front of him.', 'Article LXXV : A bro automatically promotes another bro’s job status when introducing him to a chick.', 'Article LXXVI : If a bro is on the phone with a chick in front of his bros and for whatever reason desires to day ‘I love you’ he must first excuse himself from the room or deploy a subsonic tone.', 'Article LXXVII : Bros don’t cuddle.', 'Article LXXVIII : A bro shall never rack jack his wingman.', 'Article LXXIX : At a wedding, a bro always first seeks out an open bar for his group of bros.', 'Article LXXX : A bro shall make every effort possible to aid a bro in ‘riding the tricycle’ short of completing the tricycle.', 'Article LXXXI : A bro leaves the toilet seat up for his bros.', 'Article LXXXII : If two bros get into a heated argument about something and one says something out of line, the other shall not expect him to take it back or apologize.']

sunflowers=['Aah , _sunflowers_ !', "It's funny how something as delicate as Sunflowers could hurt so much :)", "Life's been such a mess of Sunflowers and Daffodils :)" ]
daffodils=['Aah , "_If Daffodils Were A Person_ !"', "It's funny how something as delicate as Daffodils could hurt so much :)", "Life's been such a mess of Sunflowers and Daffodils :)" ]


playbook=['The SNASA (page 3): Barney goes up to a girl and claims he works for a secret government agency called "SNASA", or "Secret NASA", and claims to have been to the identically-named "SMoon".','The Cheap Trick (page 86): Barney claims that he is the bass player of a rock band with the ironic name of "Cheap Trick" (a real-life band).','The My Penis Grants Wishes (page 31): Dressed as a genie, Barney claims that his penis, like a magic lamp, grants wishes if one rubs it hard enough.']

#Functionality

@client.event
async def on_ready():
    general_channel=client.get_channel(CHANNEL_ID)
    await general_channel.send("Daddy's Home !")

@client.event
async def on_message(message):
    general_channel=client.get_channel(message.channel.category_id)
    #print(message)
    mess=message.content
    if message.author != client.user :
        mess=mess.lower()
        getcmd=mess.split()
        if mess=="who is lorenzo von matterhorn ?":
            await general_channel.send("Lorenzo Von Matterhorn was born somewhere in Switzerland in the spring of 1974. The exact date and circumstances of his birth are unknown since he was immediately placed in a basket and tossed in a river.\nTo Know More , Read : http://www.lorenzovonmatterhorn.com")
        if isWord(getcmd,"sad") and (isWord(getcmd,"feel") or isWord(getcmd,"feeling")) :
            await general_channel.send("Did I just hear sad ? Wtf do you mean by that <@{}>? When I am sad , I just stop being sad and be awesome instead !".format(message.author.id))
            await message.author.send("Bro You Okay ?\nI know we don't talk much but I love you okay ? You are important to me ! And This is not just the Bot saying :)\n Here Have A Playlist : https://spoti.fi/3kAUwcN")
        if isWord(getcmd,"sunflowers") or isWord(getcmd,"sunflower") :
            if (random.randint(3, 9))%3==0:
                await message.channel.send(random.choice(sunflowers))
        if isWord(getcmd,"daffodils") or isWord(getcmd,"daffodil") :
            if (random.randint(3, 9))%3==0:
                await message.channel.send(random.choice(daffodils))
        await client.process_commands(message)

@client.event
async def on_member_join(member):
    general_channel=client.get_channel(CHANNEL_ID)
    guild=member.guild
    message ='Hello {}, Welcome to {}. We will teach you how to live. Type in : Bro Help to get help from Bro. Please adhere to the Brocode. '.format(member.mention, guild.name)
    await general_channel.send(message)

"""
@client.event
async def on_disconnect():
        general_channel=client.get_channel(757471535446622303)
        await general_channel.send("MacLaren's Pub is now Closed ! See You Again !")
"""

#Bot Commands
@client.command(name='bruh')
async def bruh(context):

    my_embed= discord.Embed(title="All About Me", description="Lorenzo Von Matterhorn Is An Awesome Bot coded by the even more awesome @whokilleddb.\nHe likes to be called Bro.",color=0x00ff00)
    my_embed.add_field(name="Version:",value="v69.420",inline=False)
    my_embed.add_field(name="Commands:",value="bro quote brocode",inline=False)
    my_embed.set_footer(text="Suit Up !")
    my_embed.set_author(name="WhoKilledDB")

    await context.message.channel.send(embed=my_embed)


@client.command(name='quote')
async def quote(context,*str):
    if len(str)==0:
        await context.message.channel.send("Bruh")
    if str[0]=="brocode":
        await context.message.channel.send(random.choice(brocode))
    if str[0]=="playbook":
        await context.message.channel.send(random.choice(playbook))


@client.command(name='there',pass_context=True)
async def there(ctx):
        if (random.randint(1,2))%2==0:
            await ctx.send("Yup. Suit up!")
        else :
            await ctx.send("Always There For You :) <@{}>".format(ctx.author.id))

@client.command(name='makemesad',pass_context=True)
async def makemesad(ctx):
        await ctx.send(random.choice(himym))

@client.command(name="join",pass_context=True)
async def join(ctx):
    global voice
    channel=""
    channel=ctx.message.author.voice.channel
    voice=get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

    await voice.disconnect()

    if voice and voice.is_connected():
        await voice.move_to(channel)
        await ctx.send("I am in {} bitches".format(channel))
    else:
        voice = await channel.connect()
        await ctx.send("I am in {} Voice bitches".format(channel))

@client.command(name="leave",pass_context=True)
async def leave(ctx):
    global voice
    channel=""
    channel=ctx.message.author.voice.channel
    voice=get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.disconnect()
        await ctx.send(f"Imma Ight Head Out Of {channel} Voice")
    else:
        voice = await ctx.send("Bruh am not even in a Voice Channel !")

@client.command(name="playsong", pass_context=True)
async def playsong(ctx,str1,n):
    name=""
    song_there=os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
            print("Removed Song File")
    except PermissionError:
        print("The Song Is On")
        await ctx.send("Bro I think the song is already playing !")
        return

    await ctx.send("Firing That Up Now !")

    voice = get(client.voice_clients, guild=ctx.guild)
    ydl_opts={
        'format': 'bestaudio/best',
        'postprocessors':[{
            'key':'FFmpegExtractAudio',
            'preferredcodec':'mp3',
            'preferredquality':'192',
        }],
    }
    v_url=searchQuery(str1,int(n))

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
          print("Downloading Song")
          ydl.download([v_url])

    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            name=file
            print(f"Renamed File {file}")
            os.rename(file,"song.mp3")

    voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: print("Vibing"))
    voice.souce=discord.PCMVolumeTransformer(voice.source)
    voice.souce.volume=0.07

    await ctx.send(f"Playing {v_url}")

#Run The Bot
client.run(TOKEN)
#enter Secret key
