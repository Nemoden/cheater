import re

_punct_re = re.compile(r'[ \t!"#$%^&~`@()*<=>?\[\\\]{|},.]+')


def slugify(text, delim='-'):
    result = []
    for word in _punct_re.split(text.lower()):
    #word = word.encode('translit/long')
        if word:
            result.append(word)
    return unicode(delim.join(result))
