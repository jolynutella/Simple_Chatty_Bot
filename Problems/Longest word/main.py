word1 = input()
word2 = input()

# How many letters does the longest word contain?
word1_length = len(word1)
word2_length = len(word2)
print(max(word1_length, word2_length))