import general_text_responses as GeneralTextResponses

functionDict = {
    'help': GeneralTextResponses.help,
    'welcome': GeneralTextResponses.welcome,
    'say': GeneralTextResponses.say,
    }


def executeCommand(comm, args, user):

    if comm in functionDict.keys():
        return functionDict[comm](args)
    else:
        return 'Command: "{}" received from {} does not exist yet!'.format(comm, user)