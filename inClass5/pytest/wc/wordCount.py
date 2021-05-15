def howMany(words):
    num = words.count(" ")
    return num + 1

words = input("Please enter a sentence\n")

val = howMany(words)
print(val)