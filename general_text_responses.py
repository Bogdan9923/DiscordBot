import random

import discord

from Constants import *
from command_list_and_description import commandDescriptionDict
from return_code_dict import returnCodeDict
from openAI_chat import query_response

def help(argument):
    if not argument:
        help_text = 'This is the help page. To access commands use ">" in' \
                    ' front of the names.\nList of available commands:\n\n{} \n\nTo find ' \
                    'out more about a command, type >help "command name"'.format(
            '\n'.join(commandDescriptionDict.keys()))
        embed = discord.Embed(title=str_help_title, description=help_text, color=embed_color)
    else:
        if ''.join(argument) in commandDescriptionDict:
            help_text = commandDescriptionDict.get(''.join(argument))
            embed = discord.Embed(title='Help '.join(argument), description=help_text[0], color=embed_color)
            embed.add_field(name=help_text[1], value='\u200b', inline=False)
        else:
            help_text = 'Command does not exist yet!'
            embed = discord.Embed(title='Oops ', description=help_text, color=embed_color)

    return embed, returnCodeDict['text']


def say(argument):
    text = ' '.join(argument)
    embed = discord.Embed(title=str_say_title, description=text, color=embed_color)
    return embed, returnCodeDict['text']


def welcome(argument):
    text = 'Hello {}, welcome to the chat!'.format(argument)
    embed = discord.Embed(title=str_welcome_title, description=text, color=embed_color)
    return embed, returnCodeDict['text']


def choose(argument):
    if not argument:
        text = 'I think you forgot to give me a choice'
        embed = discord.Embed(title='Oops', description=text, color=embed_color)
    else:
        random_idx = random.randint(0, len(argument) - 1)
        text = 'I think "{}" is the way to go.'.format(argument[random_idx])
        embed = discord.Embed(title=str_choose_title, description=text, color=embed_color)
    return embed, returnCodeDict['text']


def askai(argument):
    if not argument:
        text = 'Maybe you forgot your words. Try again.'
        embed = discord.Embed(title='Oops', description=text, color=embed_color)
    else:
        response = query_response(argument)
        embed = discord.Embed(title=str_aichat_title, description=response, color=embed_color)
    return embed, returnCodeDict['text']