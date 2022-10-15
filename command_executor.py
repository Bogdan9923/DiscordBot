from return_code_dict import returnCodeDict
import general_text_responses as GeneralTextResponses
import general_image_response as GeneralImageResponses


commandDict = {
    'help': GeneralTextResponses.help,
    'welcome': GeneralTextResponses.welcome,
    'say': GeneralTextResponses.say,
    'get_image': GeneralImageResponses.getImageOf,

    }


def executeCommand(comm, args, user):

    if comm in commandDict.keys():
        return commandDict[comm](args)
    else:
        return 'Command: "{}" received from {} does not exist yet!'.format(comm, user), returnCodeDict['text']