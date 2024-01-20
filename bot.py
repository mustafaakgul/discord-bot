import os

import discord
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client(intents=discord.Intents.default())

# Event: on_ready
# Description: This event is called when the bot is ready. on_ready handles the event when the Client has established
# a connection to Discord and it has finished preparing the data that Discord has sent, such as login state, guild
# and channel data, etc.
# Parameters: None
# Returns: None
@client.event
async def on_ready():
    for guild in client.guilds:
        print(guild)
        print(GUILD)
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

client.run(TOKEN)
