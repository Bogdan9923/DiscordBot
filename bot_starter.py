import discord
from command_parser import parseCommand

def startBot():

    client = discord.Client(intents=discord.Intents.all())

    f = open('Token.txt','r')

    LOGIN_TOKEN = f.readline()

    @client.event
    async def on_ready():
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

                val = parseCommand(msg)
                await msg.channel.send(val)

            except Exception as e:
                print(e)

            #early debug, ignore
            #await msg.channel.send(username + ' said: ' + msg.content);
            #print(f'{username}: {user_msg} ({channel})')

    client.run(LOGIN_TOKEN)