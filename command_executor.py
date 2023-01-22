import discord
import Constants
from return_code_dict import returnCodeDict
import general_text_responses as GeneralTextResponses
import general_image_response as GeneralImageResponses


commandDict = {
    'help': GeneralTextResponses.help,
    'welcome': GeneralTextResponses.welcome,
    'say': GeneralTextResponses.say,
    'choose': GeneralTextResponses.choose,
    'get_image': GeneralImageResponses.getImageOf,
    'askai': GeneralTextResponses.askai,

    }


def executeCommand(comm, args, user):

    if comm in commandDict.keys():
        return commandDict[comm](args)
    else:
        text = 'Command: "{}" received from {} does not exist yet!'.format(comm, user)
        embed = discord.Embed(title=Constants.str_error_title, description=text, color=Constants.embed_color)
        return embed, returnCodeDict['text']