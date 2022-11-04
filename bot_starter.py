import discord
from command_parser import parseCommand
from return_code_dict import returnCodeDict

def startBot():

    client = discord.Client(intents=discord.Intents.all())

    f = open('Token.txt', 'r')

    LOGIN_TOKEN = f.readline()

    @client.event
    async def on_ready():
        await client.change_presence(
            activity=discord.Activity(type=discord.ActivityType.listening, name='Puya - Fresh'))
        print('Bot logged in as {0.user}'.format(client))

    @client.event
    async def on_message(msg):

        if msg.author == client.user: #ignore messages sent from itself
            return

        username = str(msg.author).split('#')[0]  #get data about the sent message
        user_msg = str(msg.content)
        channel = str(msg.channel.name)

        if msg.content.startswith('>'):  #check if the message is a command for the bot. Commands start with '>'
            try:

                content, code = parseCommand(msg)
                if code == returnCodeDict['text']:
                    await msg.channel.send(embed=content)
                if code == returnCodeDict['link']:
                    await msg.channel.send(content)

            except Exception as e:
                print(e)

            #early debug, ignore
            #await msg.channel.send(username + ' said: ' + msg.content);
            #print(f'{username}: {user_msg} ({channel})')

    client.run(LOGIN_TOKEN)