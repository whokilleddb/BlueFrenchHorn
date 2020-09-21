#!/bin/python3
import random
import discord     
from discord.ext import commands 
#Client
client=commands.Bot(command_prefix='--')

#functions
def isWord(lst,wrd):
    fg=False
    for i in range(len(lst)):
        if lst[i]==wrd :
            fg=True
    return fg


#Lists
himym=["https://youtu.be/MYnhPtsRQjA", "https://youtu.be/v73s7SCWzvs","https://youtu.be/HpLsYgXpIws","https://youtu.be/xWa-QVAd7gM","https://youtu.be/zwYOXsb7FbI","https://youtu.be/UImXzJsId2w","https://youtu.be/Dcngel9VyIU","https://youtu.be/fiuu245RpwQ","https://youtu.be/8Bw5Z0rBteY","https://youtu.be/I90B8tQ9qRA","https://youtu.be/yvXIpvh9hvI","https://youtu.be/6b2AGAB2pA0"]

brocode=["""Article 1 : Bro’s before ho’s
The bond between two men is stronger than the bond between a man and a woman because, on average, men are stronger than women. That’s just science.
""",
'Article 2: A Bro is always entitled to do something stupid, as long as the rest of his Bros are all doing it.',
"""
Article 3 : If a Bro gets a dog, it must be at least as tall as his knee when full-grown.
Corollary: Naming a lapdog after a pro wrestler or a character from a Steve McQueen movie does not absolve a Bro from the spirit of this article.
""",
"""
Article 4 : A Bro never divulges the existance of The Bro Code to a woman. It is a sacred document not to be shared with chicks for any reason… no, not even that reason.
Note:
If you are a woman reading this, first, let me apologize: it was never my intention for this book to contain so much math.
Second, I urge you to look at this document for what it is – a piece of fiction meant to entertain a broad audience though the prism if stereotypical gender differences. I mean, sometimes it really is like we’re from different planets! Clearly, no real person would actually believe or adhere to the vulgar rules contained within. *Those boots are adorable, b-t-dub.
""",
'ARTICLE 24: "When wearing a baseball cap, a Bro may position the brim at either 12 or 6 o’clock. All other angles are reserved for rappers and the handicapped.”',
"""
ARTICLE 100: "When pulling up to a stoplight, a Bro lowers his window so that all might enjoy his music selection."
COROLLARY : "If there happens to be a hot chick driving the car next to the Bro, the Bro shall put his sunglasses down to get a better look. If he's not wearing his sunglasses, he will first put them on, then pull down to get a better look.”
""",
'ARTICLE 54 : "A Bro is required to go out with his Bros on St. Patty’s Day and other official Bro holidays, including Halloween, New Year’s Eve, and Desperation Day (February 13).”',
'ARTICLE 85 : "If a Bro buys a new car, he is required to pop the hood when showing it off to his Bros."\nCOROLLARY: "His Bros are required to whistle, even if they have no idea what they’re whistling at.” ',
'ARTICLE 41 : "A Bro never cries."\nEXCEPTIONS: "Watching Field of Dreams, E.T., or a sports legend retire."',
'ARTICLE 120 : "A Bro always calls another Bro by his last name."   \nEXCEPTION: "If a Bro’s last name is also a racial epithet.” ',
'ARTICLE 130 : "If a Bro learns another Bro has been in a traffic accident, he must first ask what type of car he collided with and whether it got totaled before asking if his Bro is okay.” '
]

sunflowers=['Aah , _sunflowers_ !', "It's funny how something as delicate as Sunflowers could hurt so much :)", "Life's been such a mess of Sunflowers and Daffodils :)" ]
daffodils=['Aah , "_If Daffodils Were A Person_ !"', "It's funny how something as delicate as Daffodils could hurt so much :)", "Life's been such a mess of Sunflowers and Daffodils :)" ]


#Functionality
@client.event
async def on_ready():
    general_channel=client.get_channel(757471535446622303)
    await general_channel.send("Welcome To MacLaren's Pub ! We are now Open !")

@client.event
async def on_message(message):
    general_channel=client.get_channel(757471535446622303)
    mess=message.content
    if message.author != client.user :
        mess=mess.lower()
        getcmd=mess.split()
        if isWord(getcmd,"sad") :
            await general_channel.send("Did I just hear sad ? Wtf do you mean by that <@{}>? When I am sad , I just stop being sad and be awesome instead !".format(message.author.id))
            await message.author.send("Bro You Okay ?\n I know we don't talk much but I love you okay ? You are important to me ! And This is not just the Bot saying :)\n Here Have A Playlist : https://spoti.fi/3kAUwcN")
        
        if isWord(getcmd,"sunflowers") or isWord(getcmd,"sunflower") :
            if (random.randint(3, 9))%3==0:
                await message.channel.send(random.choice(sunflowers))
        
        if isWord(getcmd,"daffodils") or isWord(getcmd,"daffodil") or isWord(getcmd,"shreya") or isWord(getcmd,"bose") :
            if (random.randint(3, 9))%3==0:
                await message.channel.send(random.choice(daffodils))
        await client.process_commands(message)


@client.event
async def on_member_join(member):
    general_channel=client.get_channel(757471535446622303)
    guild=member.guild
    message ='Hello {}, Welcome to {}. We will teach you how to live. Type in : Bro Help to get help from Bro. Please adhere to the Brocode. '.format(member.mention, guild.name)
    await general_channel.send(message)


@client.event 
async def on_disconnect():
        general_channel=client.get_channel(757471535446622303)
        await general_channel.send("MacLaren's Pub is now Closed ! See You Again !")


@client.command(name='bruh')
async def bruh(context):

    my_embed= discord.Embed(title="All About Bro", description="Blue French Horn Is An Awesome Bot coded by the even more awesome @whokilleddb.\nHe likes to be called Bro.",color=0x00ff00)
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

@client.command(name='there',pass_context=True)
async def there(ctx):
        if (random.randint(1,2))%2==0:
            await ctx.send("Yup")
        else :
            await ctx.send("Always There For You :) <@{}>".format(ctx.author.id))            

@client.command(name='vids',pass_context=True)
async def vids(ctx):
        await ctx.send(random.choice(himym))
   


#Run The Bot
client.run("")
#enter Secret key
