def palin(word):
    l = len(word)
    first = 0
    last = l - 1
    while last > first:
        if word[first] != word[last]:
            return False
        first += 1
        last -= 1

    return True

input_word = input('Enter a word\n')
#input_word = ['R','A','C','E','C','A','R']
if palin(input_word):
    print('Palindrome')
else:
    print('Not a palindrome')