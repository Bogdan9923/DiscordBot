from bot_operations.bot_starter import bot5
from data.command_list_and_description import commandDescriptionDict


@bot5.command()
async def help(context, argument):
    if not argument:
        help_text = 'This is the help page. To access commands use ">" in' \
                    ' front of the names.\nList of available commands:\n{} \nTo find ' \
                    'out more about a command, type >help "command name"'.format(
            '\n'.join(commandDescriptionDict.keys()))
    else:
        if ''.join(argument) in commandDescriptionDict:
            help_text = commandDescriptionDict.get(''.join(argument))
        else:
            help_text = 'Command does not exist yet!'
    # return help_text, returnCodeDict['text']
    await context.send(help_text)

@bot5.command()
def say(context, argument):
    text = ' '.join(argument)
    # return text, returnCodeDict['text']
    context.send(text)

@bot5.command()
def welcome(context, argument):
    text = 'Hello ' + ' '.join(argument) + ', welcome to the chat!'
    context.send(text)
