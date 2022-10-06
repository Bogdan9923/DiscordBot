import discord

client = discord.Client(intents=discord.Intents.all())

SpecialKey = 'MTAyNzcwOTk5NDk0ODM4Mjc1MA.Gwf79N.lSjBUucTEliIxWAzr2HA8NDgH1G2VkUHUyM0YM'

@client.event
async def on_ready():
    print('Bot logged in as {0.user}'.format(client))

@client.event
async def on_message(msg):
    username = str(msg.author).split('#')[0]
    user_msg = str(msg.content)
    channel = str(msg.channel.name)
    print(f'{username}: {user_msg} ({channel})')

client.run(SpecialKey)