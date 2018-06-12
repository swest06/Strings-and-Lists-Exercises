word = input()
a = word.find("h") + 1
b = word.rfind("h")
x = word[:a] + word[b-1:a-1:-1] + word[b:]
print(x)

