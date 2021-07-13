import discord
import requests
import json
import webbrowser

# creating a client variable using discord library
client = discord.Client()

# function for outputting inspirational quotes
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

# function for random cat picture
def getCatPicture():
    catPicture = requests.get('http://thecatapi.com/api/images/get.php')
    if catPicture.status_code == 200:
        catPicture = catPicture.url
        return catPicture

    else:
        return 'Error 404. Website may be down.'

# function for random dog picture
def getDogPicture():
    dogPicture = requests.get('https://thedogapi.com/api/images/get.php')
    if dogPicture.status_code == 200:
        dogPicture = dogPicture.url
        return dogPicture
    
    else:
        return 'Error 404. Website may be down.'


# prints to console that bot is active
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# events for commands typed by users in discord channel
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')
    
    # command for inspirational quotes
    if message.content.startswith('!inspire'):
        quote = get_quote()
        await message.channel.send(quote)

    # command for random cat picture
    if message.content.startswith('!cat'):
        catpic = getCatPicture()
        await message.channel.send(catpic)

    # command for random dog picture
    if message.content.startswith('!dog'):
        dogpic = getDogPicture()
        await message.channel.send(dogpic)

# running the bot with its code
client.run('ODYyNzUwNzgwMDQ1NjU2MDk0.YOc5Rw.zrWiNQb6IW9EXbYizOqMD3BcHoo')
