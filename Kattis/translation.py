m = int(input())
sentence = input().split()
dictionary = {}
for _ in range(int(input())):
    swedish, english = input().split()
    dictionary[swedish] = english
translated_sentence = [dictionary[word] for word in sentence]
print(" ".join(translated_sentence))
