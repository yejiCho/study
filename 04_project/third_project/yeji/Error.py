import re

def email_error(email):
    regex = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    m = regex.match(email)
    if m :
        return m.group()
    else:
        raise regex_exception()

class regex_exception(Exception):
    def __str__(self):
        return "허용되지 않는 입력입니다."