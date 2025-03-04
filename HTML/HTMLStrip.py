# By Ethan Reed 2025/2/27, with help from ChatGPT for the regex.

import re
import html

def html_strip(s="sample1<main>sample2</main>sample3"):
    # Cleanup formatting
    s = s.replace("\n", "")
    s = s.replace("<hr>", "-----")

    # Parse newlines
    for i in ['br', 'p', 'article', 'aside', 'section', 'div', 'head', 'body']:
        regex = re.compile('<' + i + '.*?>')
        s = re.sub(regex, '\n', s)

    # Parse formatting
    for i in ['button']:
        regex = re.compile('<' + i + '.*?>')
        s = re.sub(regex, ' ', s)

    # Strip CSS & HTML
    regex = re.compile('<style.*?>.*?</style>|<.*?>', re.S)
    s = re.sub(regex, '', s)

    # Convert Character Entities
    s = html.unescape(s)

    return s

if __name__ == "__main__":
    # path = input("Filepath:")
    path = "grid.html"
    with open(path, "r") as f:
        text = f.read()
    print(html_strip(text))
