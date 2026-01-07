REDTEXT = "\033[31m" #Wrong
GREENTEXT = "\033[32m" #Success
YELLOWTEXT = "\033[33m" #Errors :(
BLUETEXT = "\033[34m" #I just like this color
RETURNDEFAULTCOLOR = "\033[0m" #Default term color
BARRIER = "#########################################" # I don't want to type my barrier out for block more than once

def block(message):
    """Print a message inside a boxed banner.

    Accepts either a single string (which may contain newlines) or an
    iterable of lines. Each line will be centered within the banner.
    """
    print(BARRIER)
    # Support multi-line messages
    if isinstance(message, str):
        lines = message.splitlines()
    else:
        try:
            lines = list(message)
        except Exception:
            lines = [str(message)]

    for line in lines:
        print(f'##{BLUETEXT}{str(line).center(len(BARRIER)-4)}{RETURNDEFAULTCOLOR}##')
    print(BARRIER)