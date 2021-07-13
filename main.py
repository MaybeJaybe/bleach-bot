import discord
import requests
import json

# creating a client variable using discord library
client = discord.Client()

# function for outputting inspirational quotes
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

# prints to console that bot is active
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# events for commands typed by users in discord channel
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    
    # command for inspirational quotes
    if message.content.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)

# running the bot with its code
client.run('ODYyNzUwNzgwMDQ1NjU2MDk0.YOc5Rw.zrWiNQb6IW9EXbYizOqMD3BcHoo')
