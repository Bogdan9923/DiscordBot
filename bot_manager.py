import discord
from discord.ext import commands
from projectSecrets import get_discord_bot_token
from commands_descriptions import command_dict
import bot_commands as bc
import constants as const


def start_bot():
    bot = commands.Bot(command_prefix='>', intents=discord.Intents.all())

    @bot.event
    async def on_ready():
        await bot.change_presence(
            activity=discord.Activity(type=discord.ActivityType.listening, name='Puya - Fresh'))
        print('Bot logged in as {0.user}'.format(bot))

    @bot.command(brief=command_dict['hello']['brief'], description=command_dict['hello']['desc'])
    async def hello(ctx):
        await ctx.send(bc.hello())

    @bot.command(brief=command_dict['say']['brief'], description=command_dict['say']['desc'])
    async def say(ctx, *, text: str = commands.parameter(default="my name", description="Text to be said")):
        embed = discord.Embed(title=command_dict['say']['title'], description=bc.say(text), color=const.embed_color)
        await ctx.send(embed=embed)

    @bot.command(brief=command_dict['welcome']['brief'], description=command_dict['welcome']['desc'])
    async def welcome(ctx, *, text: str = commands.parameter(default="everyone", description="Person to be welcomed")):
        await ctx.send(bc.welcome(text))

    @bot.command(brief=command_dict['choose']['brief'], description=command_dict['choose']['desc'])
    async def choose(ctx, *, items: str = commands.parameter(default="You have no choice", description="list of items")):
        await ctx.send(bc.choose(items))

    @bot.command(brief=command_dict['search_img']['brief'], description=command_dict['search_img']['desc'])
    async def search_img(ctx, *, search: str = commands.parameter(default="default", description="picture to be searched")):
        await ctx.send(bc.search_img(search))

    @bot.command(brief=command_dict['askai']['brief'], description=command_dict['askai']['desc'])
    async def askai(ctx, *, prompt: str = commands.parameter(default="hello", description="prompt to generate text")):
        await ctx.send(bc.askai(prompt))

    @bot.command(brief=command_dict['create']['brief'], description=command_dict['create']['desc'])
    async def create(ctx, *, prompt: str = commands.parameter(default="hello", description="prompt to generate image")):
        await ctx.send(bc.create(prompt))

    bot.run(get_discord_bot_token())
