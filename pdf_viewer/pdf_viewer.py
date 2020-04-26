_size = '1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5'
_word = 'abc'
size = [int(i) for i in _size.split()]
word = [size[ord(c)-ord('a')] for c in _word]
print(max(word)*len(word))