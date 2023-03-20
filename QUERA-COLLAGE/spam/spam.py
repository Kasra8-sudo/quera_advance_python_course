import re


def valid_sender(sender: str) -> bool:
    if not sender.isdigit():
        return True
    return False

def has_spam(s):
    return len(re.findall('spam', s.lower())) != 0


def valid_message(message: str) -> bool:
    
    if (((len(re.findall('[\w]', message)) < len(message) / 2) is True) and (has_spam(message) is True)):
        return False
    return True


sender = input()
message = input()

if valid_sender(sender) and valid_message(message):
    print('Not Spam')

elif (valid_sender(sender) is False) and (valid_message(message) is True):
    print('Invalid Sender')

elif (valid_sender(sender) is True) and (valid_message(message) is False):
    print('Invalid Content')

elif valid_message(message) is False and valid_sender(sender) is False:
    print('Fully Invalid')
