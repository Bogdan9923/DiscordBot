from command_list_and_description import commandDescriptionDict

def help(argument):

    if not argument:
        help_text = 'This is the help page. To access commands use ">" in' \
                ' front of the names.\nList of available commands:\n{} \nTo find ' \
                'out more about a command, type >help "command name"'.format('\n'.join(commandDescriptionDict.keys()))
    else:
        if ''.join(argument) in commandDescriptionDict:
            help_text = commandDescriptionDict.get(''.join(argument))
        else:
            help_text = 'Command does not exist yet!'
    return help_text


def say(argument):
    text = ' '.join(argument)
    return text


def welcome(argument):
    text = 'Hello ' + ' '.join(argument) + ', welcome to the chat!'
    return text

