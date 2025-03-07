# By Ethan Reed 2025/2/27, with help from ChatGPT for the regex.

import re
import html

def html_strip(s="sample1<main>sample2</main>sample3"):
    # Cleanup formatting
    s = s.replace("\n", "")

    # Parse newlines
    for i in ['br', 'p', 'article', 'aside', 'section', 'div', 'head', 'body']:
        regex = re.compile('<' + i + '.*?>')
        s = re.sub(regex, '\n', s)

    # Parse underlines
    for i in ['hr', 'h1', 'h2', 'h3']:
        regex = re.compile('<' + i + '.*?>')
        s = re.sub(regex, '\n-----\n', s)

    # Parse formatting
    for i in ['button']:
        regex = re.compile('<' + i + '.*?>')
        s = re.sub(regex, ' ', s)

    # Strip CSS & JS & HTML
    regex = re.compile('<style.*?>.*?</style>|<script.*?>.*?</script>|<.*?>', re.S)
    s = re.sub(regex, '', s)

    # Convert Character Entities
    s = html.unescape(s)

    return s

if __name__ == "__main__":
    # path = input("Filepath:")
    path = "Wikipedia-Curl.html"
    with open(path, "r", errors='ignore') as f:
        text = f.read()
    text = html_strip(text)
    print(text)
    with open("o.txt", "w", errors='ignore') as f:
        f.write(text)
