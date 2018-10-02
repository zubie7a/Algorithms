# https://app.codesignal.com/arcade/code-arcade/book-market/MX94DWTrwQw2gLrTi
import re

def htmlEndTagByStartTag(start_tag):
    # Given a initial HTML tag, return the closing tag. Match the
    # casing and also ignore the extra arguments in the initial tag.
    tag = re.findall(r'<[a-zA-Z0-9]*', start_tag)[0]
    end_tag = tag.replace("<", "</") + ">"
    return end_tag
