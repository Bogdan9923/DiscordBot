import discord
from discord.ext import commands
from projectSecrets import get_discord_bot_token
from commands_descriptions import command_dict
import bot_commands as bc
import constants as const
from musicplayer import MusicPlayer


def start_bot():
    bot = commands.Bot(command_prefix='>', intents=discord.Intents.all())

    @bot.event
    async def on_ready():
        await bot.change_presence(
            activity=discord.Activity(type=discord.ActivityType.listening, name='Puya - Fresh'))
        await bot.add_cog(MusicPlayer(bot))
        print('Bot logged in as {0.user}'.format(bot))

    @bot.command(brief=command_dict['hello']['brief'], description=command_dict['hello']['desc'])
    async def hello(ctx):
        await ctx.send(bc.hello())

    @bot.command(brief=command_dict['say']['brief'], description=command_dict['say']['desc'], default="my name")
    async def say(ctx, *, text: str = "my name"):
        embed = discord.Embed(title=command_dict['say']['title'], description=bc.say(text), color=const.embed_color)
        await ctx.send(embed=embed)

    @bot.command(brief=command_dict['welcome']['brief'], description=command_dict['welcome']['desc'])
    async def welcome(ctx, *, text: str = "everyone"):
        await ctx.send(bc.welcome(text))

    @bot.command(brief=command_dict['choose']['brief'], description=command_dict['choose']['desc'])
    async def choose(ctx, *, items: str = "You have no choice"):
        await ctx.send(bc.choose(items))

    @bot.command(brief=command_dict['search_img']['brief'], description=command_dict['search_img']['desc'])
    async def search_img(ctx, *, search: str = "default"):
        await ctx.send(bc.search_img(search))

    @bot.command(brief=command_dict['askai']['brief'], description=command_dict['askai']['desc'])
    async def askai(ctx, *, prompt: str = "hello"):
        await ctx.send(bc.askai(prompt))

    @bot.command(brief=command_dict['create']['brief'], description=command_dict['create']['desc'])
    async def create(ctx, *, prompt: str = "hello"):
        await ctx.send(bc.create(prompt))

    bot.run(get_discord_bot_token())
