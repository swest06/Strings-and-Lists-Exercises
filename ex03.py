w = input()
a = str(w.find("f"))
b = str(w.rfind("f"))
if int(a) < 0:
    print("")
elif a == b:
    print(a)
else:
    print(a + " " + b)
