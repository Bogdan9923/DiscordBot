def help(argument):
    help_text = 'This is help page. To call the bot, use ">" symbol'
    return help_text


def say(argument):
    text = ' '.join(argument)
    return text


def welcome(argument):
    text = 'Hello ' + ' '.join(argument) + ', welcome to the chat!'
    return text

