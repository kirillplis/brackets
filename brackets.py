x = input()
a, b, c = 0, 0, 0
i = 1
if len(x) < 2:
    print(False)
    exit()

for i in range(len(x)):
    if i == len(x):
        print(False)
        exit()
    elif x[i] == '(' and (x[i+1] == ']' or x[i+1] == '}'):
        print(False)
        exit()
    elif x[i] == '(':
        a += 1
    elif x[i] == ')':
        a -= 1
    if a < 0:
        print(False)
        exit()

if a != 0:
    print(False)
    exit()

for i in range(len(x)):
    if i == len(x):
        print(False)
        exit()
    elif x[i] == '[' and (x[i + 1] == ')' or x[i + 1] == '}'):
        print(False)
        exit()
    elif x[i] == '[':
        b += 1
    elif x[i] == ']':
        b -= 1
    if b < 0:
        print(False)
        exit()

if b != 0:
    print(False)
    exit()

for i in range(len(x)):
    if i == len(x):
        print(False)
        exit()
    elif x[i] == '{' and (x[i + 1] == ']' or x[i + 1] == ')'):
        print(False)
        exit()
    elif x[i] == '{':
        c += 1
    elif x[i] == '}':
        c -= 1
    if c < 0:
        print(False)
        exit()

if c != 0:
    print(False)
    exit()

print(True)
