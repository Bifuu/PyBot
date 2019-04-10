import discord
from discord.ext import commands
import json

#defines the prefix the bot is looking for
bot = commands.Bot(command_prefix='!')

#List of all cogs to load their commands
cogsToLoad = ['testCommands', 'randomCommands']
#Loop through list of cogs to load them
for c in cogsToLoad:
    bot.load_extension(c)

#Listen for the on_ready event to log that we are connected
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

#Get Discord token from tokens.json
discordToken = ''
with open('tokens.json') as json_file:
    data = json.load(json_file)
    discordToken = data['discordToken']

#Start the bot
bot.run(discordToken)