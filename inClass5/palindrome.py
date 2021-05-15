def isPalindrome(word):
    length = len(word)
    y = length - 1
    for x in range(0, len(word)):
        if x <= y:
            if word[x] != word[y]:
                return False
            y = y - 1
    return True

word = input("Please enter a word\n")

val = isPalindrome(word)
print(val)