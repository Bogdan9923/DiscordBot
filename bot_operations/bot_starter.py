import discord
from discord.ext import commands

bot5 = commands.Bot(command_prefix='>', intents=discord.Intents.all())


def startBot():
    # client = discord.Client(intents=discord.Intents.all())


    @bot5.command()
    async def testureanu(ctx, arg):
        await ctx.send(arg)

    @bot5.command()
    async def welcome(ctx, *args):
        await ctx.send('Welcome {}'.format(' '.join(args)))


    f = open('Token.txt', 'r')

    LOGIN_TOKEN = f.readline()

    @bot5.event
    async def on_ready():
        await bot5.load_extension('general_text_responses')

    # @client.event
    # async def on_message(msg):
    #
    #     if msg.author == client.user:  # ignore messages sent from itself
    #         return
    #
    #     print(msg.content)
    #
    #     username = str(msg.author).split('#')[0]  # get data about the sent message
    #     user_msg = str(msg.content)
    #     channel = str(msg.channel.name)
    #
    #     if msg.content.startswith('>'):  # check if the message is a command for the bot. Commands start with '>'
    #         try:
    #
    #             content, code = parseCommand(msg)
    #             if code == returnCodeDict['text']:
    #                 await msg.channel.send(content)
    #             if code == returnCodeDict['image']:
    #                 await msg.channel.send(file=discord.File(content))
    #
    #         except Exception as e:
    #             print(e)
    #
    #         # early debug, ignore
    #         # await msg.channel.send(username + ' said: ' + msg.content);
    #         # print(f'{username}: {user_msg} ({channel})')
    #
    # client.run(LOGIN_TOKEN)
    bot5.run(LOGIN_TOKEN)


