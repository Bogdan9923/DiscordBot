
def parseCommand(message):
    val = 'Command: "' + message.content[1:] + '" received from ' + \
          str(message.author).split('#')[0] + ' does not exist yet!'
   # print(val)

    command = message.content[1:].split(' ')[0]
    command_arguments = message.content[1:].split(' ')[1:]
    user = str(message.author).split('#')[0]

    if command == 'help':
        help_text = 'This is help page. To call the bot, use ">" symbol'
        return help_text

    if command == 'say':
        text = ' '.join(command_arguments)
        return text

    if command == 'welcome':
        text = 'Hello ' + ' '.join(command_arguments) + ', welcome to the chat!'
        return  text

    return val
