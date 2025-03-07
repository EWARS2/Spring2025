# By Ethan Reed 2025/2/27, with help from ChatGPT for the regex.
"""
TODO: See if it's possible to keep links, but remove buttons,
 since they're nonfunctional and only clutter pages.
"""

import re
import html

def html_strip(s="sample1<main>sample2</main>sample3"):
    # Cleanup formatting
    s = s.replace("\n", "")

    # Cleanup links
    # TODO: This half works
    s = re.sub(r'<a[^>]*href=["\']([^"\']+)["\'][^>]*>', r' \1 ', s, flags=re.S)

    # Remove buttons
    regex = re.compile('<button.*?>.*?</button>|<body.*?>.*?</a>', re.S)
    s = re.sub(regex, ' ', s)

    # Parse newlines
    for i in ['br', 'p', 'article', 'aside', 'section', 'div', 'head', 'body', 'h1', 'h2', 'h3']:
        regex = re.compile('<' + i + '.*?>')
        s = re.sub(regex, '\n', s)

    # Parse underlines
    for i in ['hr', '/h1', '/h2', '/h3']:
        regex = re.compile('<' + i + '.*?>')
        s = re.sub(regex, '\n-----\n', s)

    # Strip CSS & JS & HTML
    regex = re.compile('<style.*?>.*?</style>|<script.*?>.*?</script>|<.*?>', re.S)
    s = re.sub(regex, '', s)

    # Convert Character Entities
    s = html.unescape(s)

    return s

# Simple strip
def tag_strip(s="sample1<main>sample2</main>sample3"):
    # Strip HTML Tags
    # s = s.replace("\n", "")
    regex = re.compile('<.*?>', re.S)
    return re.sub(regex, '', s)

if __name__ == "__main__":
    # path = input("Filepath:")
    path = "curl-wikipedia.html"
    with open(path, "r", errors='ignore') as f:
        text = f.read()
    o = html_strip(text)
    o2 = tag_strip(text)
    # print(text)
    with open("o.txt", "w", errors='ignore') as f:
        f.write(o)
    with open("o2.txt", "w", errors='ignore') as f:
        f.write(o2)
