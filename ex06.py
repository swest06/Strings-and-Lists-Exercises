w = input()
x = w[::3]
for i in x:
    w = w.replace(i, "", 1)
print(w)
