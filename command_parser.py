from command_executor import executeCommand
def parseCommand(message):

    command = message.content[1:].split(' ')[0]
    command_arguments = message.content[1:].split(' ')[1:]
    user = str(message.author).split('#')[0]

    val = executeCommand(command, command_arguments, user)

    return val
