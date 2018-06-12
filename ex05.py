w = input()
a = w.find("h") + 1
b = w.rfind("h")
c = w[:a] + w[a:b].replace("h", "H") + w[b:]
print(c)
