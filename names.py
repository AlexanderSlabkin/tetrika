file = open('names.txt').read()
names = sorted(i.strip('"').lower() for i in file.split(','))
result = 0
for index, i in enumerate(names, start=1):
    result += sum(ord(j)-96 for j in i) * index


print(result)
