from urllib.request import urlopen
with urlopen("http://sixty-north.com/c/t.txt") as story:
    story_words = []
    for line in story:
        line_words = line.decode('utf-8').split()
        for word in line_words:
            story_words.append(word)
print(story_words)

### with url request - always bytes returned. we need to get that as String. so use decode(utf-8) while splitting of linewords