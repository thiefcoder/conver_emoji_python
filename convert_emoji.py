Message = input('>')
words = Message.split(' ')
emojis = {
    ':)': '😀',
    ':D': '😀',
    ':P': '😛',
    ':(': '😞',
    }
for word in words:
    for emoji in emojis:
        if emoji in word:
            print(emojis[emoji], end='')
            word = word.replace(emoji, '')
    print(word, end=' ')